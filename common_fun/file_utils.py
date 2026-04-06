"""File and serialization utilities."""

from __future__ import annotations

import csv
import json
from collections.abc import Sequence
from pathlib import Path
from typing import Any

__all__ = [
    "read_file",
    "write_file",
    "count_lines",
    "count_words",
    "file_exists",
    "delete_file",
    "append_to_file",
    "read_csv",
    "write_csv",
    "read_json",
    "write_json",
    "read_lines",
    "write_lines",
]


def _as_path(file_path: str | Path) -> Path:
    if not isinstance(file_path, (str, Path)):
        raise TypeError("file_path must be a string or Path.")
    return Path(file_path)


def read_file(file_path: str | Path) -> str:
    """Read entire text file with UTF-8 encoding."""
    path = _as_path(file_path)
    return path.read_text(encoding="utf-8")


def write_file(file_path: str | Path, content: str) -> None:
    """Write UTF-8 text to file, creating parent directories when needed."""
    path = _as_path(file_path)
    if not isinstance(content, str):
        raise TypeError("content must be a string.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def count_lines(file_path: str | Path) -> int:
    """Count lines in a UTF-8 text file."""
    path = _as_path(file_path)
    with path.open("r", encoding="utf-8") as handle:
        return sum(1 for _ in handle)


def count_words(file_path: str | Path) -> int:
    """Count whitespace-separated words in a UTF-8 text file."""
    path = _as_path(file_path)
    with path.open("r", encoding="utf-8") as handle:
        return sum(len(line.split()) for line in handle)


def file_exists(file_path: str | Path) -> bool:
    """Return True if file_path exists and is a file."""
    path = _as_path(file_path)
    return path.is_file()


def delete_file(file_path: str | Path) -> None:
    """Delete file if it exists."""
    path = _as_path(file_path)
    try:
        path.unlink()
    except FileNotFoundError:
        return


def append_to_file(file_path: str | Path, content: str) -> None:
    """Append UTF-8 text to file."""
    path = _as_path(file_path)
    if not isinstance(content, str):
        raise TypeError("content must be a string.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(content)


def read_csv(file_path: str | Path) -> list[list[str]]:
    """Read CSV file into list of rows."""
    path = _as_path(file_path)
    with path.open("r", encoding="utf-8", newline="") as handle:
        return [row for row in csv.reader(handle)]


def write_csv(file_path: str | Path, data: Sequence[Sequence[Any]]) -> None:
    """Write sequence of rows to CSV file."""
    path = _as_path(file_path)
    if not isinstance(data, Sequence):
        raise TypeError("data must be a sequence of rows.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        for row in data:
            if not isinstance(row, Sequence):
                raise TypeError("each row must be a sequence.")
            writer.writerow(row)


def read_json(file_path: str | Path) -> Any:
    """Read JSON file and return parsed data."""
    path = _as_path(file_path)
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(file_path: str | Path, data: Any) -> None:
    """Write JSON-serializable data to file."""
    path = _as_path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)


def read_lines(file_path: str | Path) -> list[str]:
    """Read file into a list of lines."""
    path = _as_path(file_path)
    with path.open("r", encoding="utf-8") as handle:
        return handle.readlines()


def write_lines(file_path: str | Path, lines: Sequence[str]) -> None:
    """Write line sequence to file."""
    path = _as_path(file_path)
    if not isinstance(lines, Sequence):
        raise TypeError("lines must be a sequence of strings.")
    if not all(isinstance(line, str) for line in lines):
        raise TypeError("all entries in lines must be strings.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        handle.writelines(lines)
