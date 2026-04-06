"""Validation helpers for common user input formats."""

from __future__ import annotations

import re
from datetime import datetime
from decimal import Decimal, InvalidOperation
from urllib.parse import urlparse

__all__ = [
    "is_email",
    "is_url",
    "is_phone_number",
    "is_strong_password",
    "is_numeric",
    "is_valid_date",
    "is_valid_time",
]

_EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
_PASSWORD_RE = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d])[\S]{8,}$"
)


def _validate_str(value: str, name: str) -> None:
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string.")


def is_email(s: str) -> bool:
    """Return True if s is a syntactically valid email."""
    _validate_str(s, "s")
    return _EMAIL_RE.match(s) is not None


def is_url(s: str) -> bool:
    """Return True if s is an HTTP/HTTPS URL with a hostname."""
    _validate_str(s, "s")
    parsed = urlparse(s)
    if parsed.scheme in ("http", "https") and parsed.netloc:
        return True
    parsed_with_scheme = urlparse(f"https://{s}")
    return bool(parsed_with_scheme.netloc and "." in parsed_with_scheme.netloc)


def is_phone_number(s: str) -> bool:
    """Return True if s looks like an international phone number."""
    _validate_str(s, "s")
    cleaned = re.sub(r"[\s().-]", "", s)
    if cleaned.startswith("+"):
        cleaned = cleaned[1:]
    return cleaned.isdigit() and 9 <= len(cleaned) <= 15


def is_strong_password(s: str) -> bool:
    """Return True if s meets strong password requirements."""
    _validate_str(s, "s")
    return _PASSWORD_RE.match(s) is not None


def is_numeric(s: str) -> bool:
    """Return True if s is parseable as a finite decimal number."""
    _validate_str(s, "s")
    value = s.strip()
    if not value:
        return False
    try:
        parsed = Decimal(value)
    except InvalidOperation:
        return False
    return parsed.is_finite()


def is_valid_date(s: str) -> bool:
    """Return True if s is in YYYY-MM-DD format and valid."""
    _validate_str(s, "s")
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_time(s: str) -> bool:
    """Return True if s is in HH:MM:SS format and valid."""
    _validate_str(s, "s")
    try:
        datetime.strptime(s, "%H:%M:%S")
        return True
    except ValueError:
        return False
    