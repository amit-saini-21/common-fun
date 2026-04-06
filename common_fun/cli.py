"""Command-line interface for common_fun."""

from __future__ import annotations

import argparse
import ast
import inspect
from types import ModuleType
from typing import Any

from . import arrays, converters, decorators, file_utils, numbers, strings, utils, validators

MODULES: dict[str, ModuleType] = {
    "numbers": numbers,
    "strings": strings,
    "arrays": arrays,
    "validators": validators,
    "converters": converters,
    "file_utils": file_utils,
    "utils": utils,
    "decorators": decorators,
}


def _safe_parse_arg(value: str) -> Any:
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value


def _public_functions(module: ModuleType) -> dict[str, Any]:
    functions = {
        name: obj
        for name, obj in inspect.getmembers(module, inspect.isfunction)
        if obj.__module__ == module.__name__ and not name.startswith("_")
    }
    if hasattr(module, "__all__"):
        exported = set(getattr(module, "__all__"))
        functions = {name: fn for name, fn in functions.items() if name in exported}
    return functions


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="common-fun",
        description="Run common_fun module utilities from the command line.",
    )
    parser.add_argument("module", nargs="?", help="Module name (e.g., numbers)")
    parser.add_argument("function", nargs="?", help="Function name in the module")
    parser.add_argument("args", nargs="*", help="Function arguments")
    return parser


def _print_modules() -> None:
    print("Available modules:")
    for module_name in sorted(MODULES):
        print(f"  {module_name}")


def _print_module_functions(module_name: str, module: ModuleType) -> None:
    print(f"Functions in {module_name}:")
    functions = _public_functions(module)
    for name in sorted(functions):
        print(f"  {name}")


def _invoke(module_name: str, function_name: str, raw_args: list[str]) -> int:
    module = MODULES[module_name]
    functions = _public_functions(module)
    if function_name not in functions:
        print(f"Function '{function_name}' not found in module '{module_name}'.")
        return 2

    function = functions[function_name]
    parsed_args = [_safe_parse_arg(value) for value in raw_args]
    try:
        result = function(*parsed_args)
    except TypeError as exc:
        signature = inspect.signature(function)
        print(f"Argument error: {exc}")
        print(f"Usage: common-fun {module_name} {function_name} {signature}")
        return 2
    except Exception as exc:  # pragma: no cover - safety net for CLI
        print(f"Error: {exc}")
        return 1

    if result is not None:
        print(result)
    return 0


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = _build_parser()
    parsed = parser.parse_args(argv)

    if parsed.module in (None, "help"):
        parser.print_help()
        print()
        _print_modules()
        return 0

    if parsed.module not in MODULES:
        print(f"Unknown module '{parsed.module}'.")
        _print_modules()
        return 2

    module_name = parsed.module
    module = MODULES[module_name]

    if parsed.function is None:
        _print_module_functions(module_name, module)
        return 0

    return _invoke(module_name, parsed.function, parsed.args)


if __name__ == "__main__":
    raise SystemExit(main())