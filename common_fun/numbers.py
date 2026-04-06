"""Utilities for common integer operations.

Examples:
    >>> is_prime(7)
    True
    >>> generate_primes(10)
    [2, 3, 5, 7]
"""

from __future__ import annotations

from math import isqrt

__all__ = [
    "is_prime",
    "is_even",
    "is_odd",
    "factorial",
    "fibonacci_n",
    "gcd",
    "lcm",
    "is_perfect",
    "is_armstrong",
    "sum_of_digits",
    "digit_sum",
    "reverse_number",
    "count_digits",
    "is_palindrome",
    "is_power_of",
    "is_multiple_of",
    "is_factor_of",
    "is_between",
    "is_positive",
    "is_negative",
    "is_zero",
    "generate_primes",
    "generate_fibonacci",
    "sum_of_natural_numbers",
    "get_divisors",
]


def _validate_int(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer.")


def is_prime(n: int) -> bool:
    """Return True if n is prime, otherwise False."""
    _validate_int(n, "n")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_even(n: int) -> bool:
    """Return True if n is even."""
    _validate_int(n, "n")
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Return True if n is odd."""
    _validate_int(n, "n")
    return n % 2 != 0


def factorial(n: int) -> int:
    """Return n! for a non-negative integer n."""
    _validate_int(n, "n")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci_n(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed)."""
    _validate_int(n, "n")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def gcd(a: int, b: int) -> int:
    """Return greatest common divisor of a and b."""
    _validate_int(a, "a")
    _validate_int(b, "b")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return least common multiple of a and b."""
    _validate_int(a, "a")
    _validate_int(b, "b")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def is_perfect(n: int) -> bool:
    """Return True if n is a perfect number."""
    _validate_int(n, "n")
    if n <= 1:
        return False
    total = 1
    root = isqrt(n)
    for i in range(2, root + 1):
        if n % i == 0:
            total += i
            pair = n // i
            if pair != i:
                total += pair
    return total == n


def is_armstrong(n: int) -> bool:
    """Return True if n is an Armstrong number."""
    _validate_int(n, "n")
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n


def is_palindrome(n: int) -> bool:
    """Return True if the absolute value of n is a palindrome."""
    _validate_int(n, "n")
    s = str(abs(n))
    return s == s[::-1]


def is_power_of(n: int, base: int) -> bool:
    """Return True if n is an exact integer power of base."""
    _validate_int(n, "n")
    _validate_int(base, "base")

    if base == 0:
        return n == 0
    if base == 1:
        return n == 1
    if base == -1:
        return n in (1, -1)
    if n == 0:
        return False

    current = n
    while current % base == 0:
        current //= base
    return current == 1


def reverse_number(n: int) -> int:
    """Return n with reversed digits, preserving sign."""
    _validate_int(n, "n")
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])


def count_digits(n: int) -> int:
    """Return number of decimal digits in n."""
    _validate_int(n, "n")
    return len(str(abs(n)))


def sum_of_digits(n: int) -> int:
    """Return the sum of decimal digits in n."""
    _validate_int(n, "n")
    return sum(int(d) for d in str(abs(n)))


def digit_sum(n: int) -> int:
    """Backward-compatible alias for sum_of_digits."""
    return sum_of_digits(n)


def is_multiple_of(n: int, divisor: int) -> bool:
    """Return True if n is a multiple of divisor."""
    _validate_int(n, "n")
    _validate_int(divisor, "divisor")
    if divisor == 0:
        return n == 0
    return n % divisor == 0


def is_factor_of(n: int, multiple: int) -> bool:
    """Return True if n is a factor of multiple."""
    _validate_int(n, "n")
    _validate_int(multiple, "multiple")
    if n == 0:
        return multiple == 0
    return multiple % n == 0


def is_between(n: int, low: int, high: int) -> bool:
    """Return True if low <= n <= high."""
    _validate_int(n, "n")
    _validate_int(low, "low")
    _validate_int(high, "high")
    if low > high:
        low, high = high, low
    return low <= n <= high


def is_positive(n: int) -> bool:
    """Return True if n > 0."""
    _validate_int(n, "n")
    return n > 0


def is_negative(n: int) -> bool:
    """Return True if n < 0."""
    _validate_int(n, "n")
    return n < 0


def is_zero(n: int) -> bool:
    """Return True if n == 0."""
    _validate_int(n, "n")
    return n == 0


def generate_primes(limit: int) -> list[int]:
    """Return all prime numbers <= limit using a sieve."""
    _validate_int(limit, "limit")
    if limit < 2:
        return []

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            start = i * i
            step = i
            sieve[start : limit + 1 : step] = b"\x00" * (((limit - start) // step) + 1)
    return [n for n in range(2, limit + 1) if sieve[n]]


def generate_fibonacci(limit: int) -> list[int]:
    """Return Fibonacci numbers less than or equal to limit."""
    _validate_int(limit, "limit")
    if limit < 0:
        raise ValueError("limit must be non-negative.")

    result: list[int] = []
    a, b = 0, 1
    while a <= limit:
        result.append(a)
        a, b = b, a + b
    return result


def sum_of_natural_numbers(n: int) -> int:
    """Return sum of first n natural numbers."""
    _validate_int(n, "n")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return n * (n + 1) // 2


def get_divisors(n: int) -> list[int]:
    """Return positive divisors of n in ascending order."""
    _validate_int(n, "n")
    if n == 0:
        raise ValueError("n must be non-zero.")

    target = abs(n)
    small: list[int] = []
    large: list[int] = []
    for i in range(1, isqrt(target) + 1):
        if target % i == 0:
            small.append(i)
            pair = target // i
            if pair != i:
                large.append(pair)
    return small + large[::-1]