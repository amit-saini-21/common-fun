"""String utility functions.

Examples:
    >>> is_anagram("listen", "silent")
    True
    >>> slugify("Hello, World!")
    'hello-world'
"""

from __future__ import annotations

import re
from collections import Counter

__all__ = [
    "is_palindrome",
    "is_anagram",
    "is_pangram",
    "count_vowels",
    "count_consonants",
    "remove_duplicates",
    "reverse_string",
    "word_count",
    "slugify",
    "remove_special_char",
    "longest_common_prefix",
    "longest_common_suffix",
    "longest_common_substring",
    "longest_common_subsequence",
]

_NON_ALNUM_RE = re.compile(r"[^a-z0-9\s-]+")
_WHITESPACE_RE = re.compile(r"[\s_-]+")


def _validate_str(value: str, name: str) -> None:
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string.")


def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome (ignores non-alphanumeric chars)."""
    _validate_str(s, "s")
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def is_anagram(s1: str, s2: str) -> bool:
    """Return True if s1 and s2 are anagrams (case-insensitive, alnum-only)."""
    _validate_str(s1, "s1")
    _validate_str(s2, "s2")
    normalized_1 = "".join(c.lower() for c in s1 if c.isalnum())
    normalized_2 = "".join(c.lower() for c in s2 if c.isalnum())
    return Counter(normalized_1) == Counter(normalized_2)


def is_pangram(s: str) -> bool:
    """Return True if s contains every English letter at least once."""
    _validate_str(s, "s")
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(s.lower()))


def count_vowels(s: str) -> int:
    """Return vowel count in s."""
    _validate_str(s, "s")
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)


def count_consonants(s: str) -> int:
    """Return consonant count in s."""
    _validate_str(s, "s")
    return sum(1 for char in s if char.isalpha() and char.lower() not in "aeiou")


def remove_duplicates(s: str) -> str:
    """Return s with duplicate characters removed, preserving order."""
    _validate_str(s, "s")
    seen: set[str] = set()
    result: list[str] = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)


def reverse_string(s: str) -> str:
    """Return reversed s."""
    _validate_str(s, "s")
    return s[::-1]


def word_count(s: str) -> int:
    """Return number of whitespace-separated words in s."""
    _validate_str(s, "s")
    return len(s.split())


def slugify(s: str) -> str:
    """Convert s into a URL slug."""
    _validate_str(s, "s")
    lowered = s.strip().lower()
    cleaned = _NON_ALNUM_RE.sub("", lowered)
    return _WHITESPACE_RE.sub("-", cleaned).strip("-")


def remove_special_char(s: str) -> str:
    """Return s with punctuation removed while preserving spaces."""
    _validate_str(s, "s")
    return "".join(c for c in s if c.isalnum() or c.isspace())


def longest_common_prefix(s1: str, s2: str) -> str:
    """Return the longest common prefix of s1 and s2."""
    _validate_str(s1, "s1")
    _validate_str(s2, "s2")
    limit = min(len(s1), len(s2))
    for i in range(limit):
        if s1[i] != s2[i]:
            return s1[:i]
    return s1[:limit]


def longest_common_suffix(s1: str, s2: str) -> str:
    """Return the longest common suffix of s1 and s2."""
    _validate_str(s1, "s1")
    _validate_str(s2, "s2")
    i = 0
    limit = min(len(s1), len(s2))
    while i < limit and s1[-(i + 1)] == s2[-(i + 1)]:
        i += 1
    return s1[len(s1) - i :] if i else ""


def longest_common_substring(s1: str, s2: str) -> str:
    """Return the longest contiguous common substring of s1 and s2."""
    _validate_str(s1, "s1")
    _validate_str(s2, "s2")
    if not s1 or not s2:
        return ""

    prev = [0] * (len(s2) + 1)
    longest = 0
    end_pos = 0
    for i, ch1 in enumerate(s1, start=1):
        curr = [0] * (len(s2) + 1)
        for j, ch2 in enumerate(s2, start=1):
            if ch1 == ch2:
                curr[j] = prev[j - 1] + 1
                if curr[j] > longest:
                    longest = curr[j]
                    end_pos = i
        prev = curr
    return s1[end_pos - longest : end_pos]


def longest_common_subsequence(s1: str, s2: str) -> str:
    """Return the longest common subsequence of s1 and s2."""
    _validate_str(s1, "s1")
    _validate_str(s2, "s2")
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    result: list[str] = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))
