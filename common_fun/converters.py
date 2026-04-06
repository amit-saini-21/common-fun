"""Unit and format conversion helpers."""

from __future__ import annotations

import csv
import io
import json
from numbers import Real
from typing import Any

__all__ = [
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius",
    "miles_to_kilometers",
    "kilometers_to_miles",
    "pounds_to_kilograms",
    "kilograms_to_pounds",
    "json_to_dict",
    "dict_to_json",
    "csv_to_list",
    "list_to_csv",
    "celsius_to_kelvin",
    "kelvin_to_celsius",
    "fahrenheit_to_kelvin",
    "kelvin_to_fahrenheit",
    "inches_to_centimeters",
    "centimeters_to_inches",
    "feet_to_meters",
    "meters_to_feet",
    "pounds_to_ounces",
    "ounces_to_pounds",
    "gallons_to_liters",
    "liters_to_gallons",
]


def _validate_number(value: Real, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} must be a real number.")
    return float(value)


def celsius_to_fahrenheit(c: Real) -> float:
    """Convert Celsius to Fahrenheit."""
    c_value = _validate_number(c, "c")
    return (c_value * 9 / 5) + 32


def fahrenheit_to_celsius(f: Real) -> float:
    """Convert Fahrenheit to Celsius."""
    f_value = _validate_number(f, "f")
    return (f_value - 32) * 5 / 9


def miles_to_kilometers(miles: Real) -> float:
    """Convert miles to kilometers."""
    miles_value = _validate_number(miles, "miles")
    return miles_value * 1.60934


def kilometers_to_miles(km: Real) -> float:
    """Convert kilometers to miles."""
    km_value = _validate_number(km, "km")
    return km_value / 1.60934


def pounds_to_kilograms(pounds: Real) -> float:
    """Convert pounds to kilograms."""
    pounds_value = _validate_number(pounds, "pounds")
    return pounds_value * 0.453592


def kilograms_to_pounds(kg: Real) -> float:
    """Convert kilograms to pounds."""
    kg_value = _validate_number(kg, "kg")
    return kg_value / 0.453592


def json_to_dict(json_str: str) -> dict[str, Any]:
    """Parse JSON string into a dictionary."""
    if not isinstance(json_str, str):
        raise TypeError("json_str must be a string.")
    try:
        parsed = json.loads(json_str)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON string: {exc}") from exc
    if not isinstance(parsed, dict):
        raise ValueError("JSON must represent an object (dictionary).")
    return parsed


def dict_to_json(d: dict[str, Any]) -> str:
    """Serialize dictionary into JSON string."""
    if not isinstance(d, dict):
        raise TypeError("d must be a dictionary.")
    try:
        return json.dumps(d)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Dictionary contains non-serializable data: {exc}") from exc


def csv_to_list(csv_str: str) -> list[list[str]]:
    """Parse CSV text into a list of rows."""
    if not isinstance(csv_str, str):
        raise TypeError("csv_str must be a string.")
    with io.StringIO(csv_str) as buffer:
        return [row for row in csv.reader(buffer)]


def list_to_csv(lst: list[list[Any]]) -> str:
    """Serialize list-of-rows data to CSV text."""
    if not isinstance(lst, list):
        raise TypeError("lst must be a list of rows.")
    with io.StringIO() as buffer:
        writer = csv.writer(buffer)
        for row in lst:
            if not isinstance(row, list):
                raise TypeError("each row in lst must be a list.")
            writer.writerow(row)
        return buffer.getvalue().rstrip("\r\n")


def celsius_to_kelvin(c: Real) -> float:
    """Convert Celsius to Kelvin."""
    c_value = _validate_number(c, "c")
    result = c_value + 273.15
    if result < 0:
        raise ValueError("temperature below absolute zero is invalid.")
    return result


def kelvin_to_celsius(k: Real) -> float:
    """Convert Kelvin to Celsius."""
    k_value = _validate_number(k, "k")
    if k_value < 0:
        raise ValueError("kelvin cannot be negative.")
    return k_value - 273.15


def fahrenheit_to_kelvin(f: Real) -> float:
    """Convert Fahrenheit to Kelvin."""
    k_value = celsius_to_kelvin(fahrenheit_to_celsius(f))
    return k_value


def kelvin_to_fahrenheit(k: Real) -> float:
    """Convert Kelvin to Fahrenheit."""
    c_value = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c_value)


def inches_to_centimeters(inches: Real) -> float:
    """Convert inches to centimeters."""
    inches_value = _validate_number(inches, "inches")
    return inches_value * 2.54


def centimeters_to_inches(cm: Real) -> float:
    """Convert centimeters to inches."""
    cm_value = _validate_number(cm, "cm")
    return cm_value / 2.54


def feet_to_meters(feet: Real) -> float:
    """Convert feet to meters."""
    feet_value = _validate_number(feet, "feet")
    return feet_value * 0.3048


def meters_to_feet(meters: Real) -> float:
    """Convert meters to feet."""
    meters_value = _validate_number(meters, "meters")
    return meters_value / 0.3048


def pounds_to_ounces(pounds: Real) -> float:
    """Convert pounds to ounces."""
    pounds_value = _validate_number(pounds, "pounds")
    return pounds_value * 16


def ounces_to_pounds(ounces: Real) -> float:
    """Convert ounces to pounds."""
    ounces_value = _validate_number(ounces, "ounces")
    return ounces_value / 16


def gallons_to_liters(gallons: Real) -> float:
    """Convert gallons to liters."""
    gallons_value = _validate_number(gallons, "gallons")
    return gallons_value * 3.78541


def liters_to_gallons(liters: Real) -> float:
    """Convert liters to gallons."""
    liters_value = _validate_number(liters, "liters")
    return liters_value / 3.78541

