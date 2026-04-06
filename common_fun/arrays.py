"""Array and list utilities."""

from __future__ import annotations

from collections.abc import Iterator
from numbers import Real
from typing import Any

__all__ = [
    "flatten_list",
    "remove_duplicates",
    "second_largest",
    "unique_elements",
    "rotate_list",
    "chunk_list",
]


def flatten_list(nested_list: list[Any]) -> list[Any]:
    """Flatten an arbitrarily nested list iteratively."""
    if not isinstance(nested_list, list):
        raise TypeError("nested_list must be a list.")

    result: list[Any] = []
    stack: list[Any] = [iter(nested_list)]
    while stack:
        for item in stack[-1]:
            if isinstance(item, list):
                stack.append(iter(item))
                break
            result.append(item)
        else:
            stack.pop()
    return result


def remove_duplicates(lst: list[Any]) -> list[Any]:
    """Return list with duplicates removed, preserving order."""
    if not isinstance(lst, list):
        raise TypeError("lst must be a list.")

    seen_hashable: set[Any] = set()
    seen_unhashable: list[Any] = []
    result: list[Any] = []

    for item in lst:
        try:
            if item in seen_hashable:
                continue
            seen_hashable.add(item)
            result.append(item)
        except TypeError:
            if any(item == existing for existing in seen_unhashable):
                continue
            seen_unhashable.append(item)
            result.append(item)

    return result


def second_largest(lst: list[Real]) -> Real:
    """Return the second largest distinct numeric value."""
    if not isinstance(lst, list):
        raise TypeError("lst must be a list.")
    if len(lst) < 2:
        raise ValueError("lst must contain at least two elements.")

    first: Real | None = None
    second: Real | None = None
    for num in lst:
        if isinstance(num, bool) or not isinstance(num, Real):
            raise TypeError("all elements in lst must be numeric.")
        if first is None or num > first:
            if first != num:
                second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num

    if second is None:
        raise ValueError("lst does not contain two distinct values.")
    return second


def unique_elements(lst: list[Any]) -> list[Any]:
    """Alias of remove_duplicates for backward compatibility."""
    return remove_duplicates(lst)


def rotate_list(lst: list[Any], k: int) -> list[Any]:
    """Rotate a list to the right by k positions."""
    if not isinstance(lst, list):
        raise TypeError("lst must be a list.")
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k must be an integer.")
    if not lst:
        return []
    k %= len(lst)
    if k == 0:
        return lst.copy()
    return lst[-k:] + lst[:-k]


def chunk_list(lst: list[Any], chunk_size: int) -> Iterator[list[Any]]:
    """Yield fixed-size chunks from lst."""
    if not isinstance(lst, list):
        raise TypeError("lst must be a list.")
    if isinstance(chunk_size, bool) or not isinstance(chunk_size, int):
        raise TypeError("chunk_size must be an integer.")
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer.")

    for i in range(0, len(lst), chunk_size):
        yield lst[i : i + chunk_size]

