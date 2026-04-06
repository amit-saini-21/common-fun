"""Reusable decorators for timing, retries, caching, and call logging."""

from __future__ import annotations

import logging
import time
from collections.abc import Callable
from functools import wraps
from typing import Any, ParamSpec, TypeVar

__all__ = ["timer", "retry", "cache", "log_calls"]

P = ParamSpec("P")
R = TypeVar("R")


def timer(func: Callable[P, R]) -> Callable[P, R]:
    """Print execution time and return the wrapped function result."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} executed in {elapsed:.6f} seconds")
        return result

    return wrapper


def retry(
    times: int,
    exceptions: tuple[type[Exception], ...] = (Exception,),
    delay: float = 0.0,
    backoff: float = 1.0,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Retry a function call up to times attempts for selected exceptions."""
    if isinstance(times, bool) or not isinstance(times, int):
        raise TypeError("times must be an integer.")
    if times < 1:
        raise ValueError("times must be at least 1.")
    if delay < 0:
        raise ValueError("delay must be non-negative.")
    if backoff < 1.0:
        raise ValueError("backoff must be at least 1.0.")

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            current_delay = delay
            last_error: Exception | None = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:  # type: ignore[misc]
                    last_error = exc
                    if attempt == times:
                        break
                    if current_delay > 0:
                        time.sleep(current_delay)
                        current_delay *= backoff
            if last_error is not None:
                raise last_error
            raise RuntimeError("retry failed without capturing an exception.")

        return wrapper

    return decorator


def cache(func: Callable[P, R]) -> Callable[P, R]:
    """Cache function results for hashable arguments."""
    store: dict[tuple[Any, ...], R] = {}

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        key = args + tuple(sorted(kwargs.items()))
        try:
            if key in store:
                return store[key]
        except TypeError:
            return func(*args, **kwargs)
        result = func(*args, **kwargs)
        store[key] = result
        return result

    return wrapper


def log_calls(func: Callable[P, R]) -> Callable[P, R]:
    """Log function calls at INFO level."""
    logger = logging.getLogger(func.__module__)

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        logger.info("Calling %s args=%s kwargs=%s", func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return wrapper

