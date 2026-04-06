"""General utility helpers."""

from __future__ import annotations

import copy
import time
from collections.abc import Callable
from typing import Any, TypeVar

__all__ = ["flatten_dict", "deep_copy", "benchmark", "flatten_linked_list"]

T = TypeVar("T")


def flatten_dict(d: dict[str, Any], parent_key: str = "", sep: str = ".") -> dict[str, Any]:
    """Flatten a nested dictionary using compound keys.

    Example:
        >>> flatten_dict({"a": {"b": 1}})
        {'a.b': 1}
    """
    if not isinstance(d, dict):
        raise TypeError("d must be a dictionary.")
    if not isinstance(parent_key, str):
        raise TypeError("parent_key must be a string.")
    if not isinstance(sep, str):
        raise TypeError("sep must be a string.")

    result: dict[str, Any] = {}
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict):
            result.update(flatten_dict(value, new_key, sep=sep))
        else:
            result[new_key] = value
    return result


def deep_copy(obj: T) -> T:
    """Return a deep copy of obj."""
    return copy.deepcopy(obj)


def benchmark(func: Callable[..., T], *args: Any, **kwargs: Any) -> T:
    """Run func and print elapsed execution time."""
    if not callable(func):
        raise TypeError("func must be callable.")
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    print(f"{func.__name__} executed in {elapsed:.6f} seconds")
    return result


def flatten_linked_list(head: Any) -> Any:
    """Flatten a linked list where nodes expose a `next` attribute."""
    if head is None:
        return None

    stack = [head]
    prev = None
    while stack:
        node = stack.pop()
        if prev is not None:
            prev.next = node
        prev = node
        next_node = getattr(node, "next", None)
        if next_node is not None:
            stack.append(next_node)
            node.next = None
    return head

