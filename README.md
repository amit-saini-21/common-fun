# common-fun

common-fun is a modular Python utility library for common day-to-day tasks:

- Number operations and generators
- String and text utilities
- Array/list transformations
- Input validators
- Unit and format converters
- File helpers
- Reusable decorators
- General-purpose utility helpers
- CLI access to all public module functions

## Installation

```bash
pip install common-fun
```

For local development:

```bash
pip install -e .
```

## Quick Start

```python
from common_fun.numbers import is_prime, generate_primes
from common_fun.strings import slugify

print(is_prime(7))
print(generate_primes(20))
print(slugify("Hello, Production Python!"))
```

## CLI Usage

The package exposes a CLI command:

```bash
common-fun help
common-fun numbers
common-fun numbers is_prime 7
common-fun strings slugify "Hello CLI World"
```

Behavior:

- `common-fun help`: displays global help and available modules
- `common-fun <module>`: lists public functions in the module
- `common-fun <module> <function> [args...]`: executes the function

Arguments are parsed with Python literal parsing where possible.
Examples: `7`, `3.14`, `True`, `[1, 2, 3]`, `{"a": 1}`.

## Modules and Public Functions

### numbers

- is_prime
- is_even
- is_odd
- factorial
- fibonacci_n
- gcd
- lcm
- is_perfect
- is_armstrong
- sum_of_digits
- digit_sum
- reverse_number
- count_digits
- is_palindrome
- is_power_of
- is_multiple_of
- is_factor_of
- is_between
- is_positive
- is_negative
- is_zero
- generate_primes
- generate_fibonacci
- sum_of_natural_numbers
- get_divisors

### strings

- is_palindrome
- is_anagram
- is_pangram
- count_vowels
- count_consonants
- remove_duplicates
- reverse_string
- word_count
- slugify
- remove_special_char
- longest_common_prefix
- longest_common_suffix
- longest_common_substring
- longest_common_subsequence

### arrays

- flatten_list
- remove_duplicates
- second_largest
- unique_elements
- rotate_list
- chunk_list

### validators

- is_email
- is_url
- is_phone_number
- is_strong_password
- is_numeric
- is_valid_date
- is_valid_time

### converters

- celsius_to_fahrenheit
- fahrenheit_to_celsius
- miles_to_kilometers
- kilometers_to_miles
- pounds_to_kilograms
- kilograms_to_pounds
- json_to_dict
- dict_to_json
- csv_to_list
- list_to_csv
- celsius_to_kelvin
- kelvin_to_celsius
- fahrenheit_to_kelvin
- kelvin_to_fahrenheit
- inches_to_centimeters
- centimeters_to_inches
- feet_to_meters
- meters_to_feet
- pounds_to_ounces
- ounces_to_pounds
- gallons_to_liters
- liters_to_gallons

### file_utils

- read_file
- write_file
- count_lines
- count_words
- file_exists
- delete_file
- append_to_file
- read_csv
- write_csv
- read_json
- write_json
- read_lines
- write_lines

### decorators

- timer
- retry
- cache
- log_calls

### utils

- flatten_dict
- deep_copy
- benchmark
- flatten_linked_list

## Project Structure

```text
common_fun/
	common_fun/
		__init__.py
		arrays.py
		cli.py
		converters.py
		decorators.py
		file_utils.py
		numbers.py
		strings.py
		utils.py
		validators.py
	cli.py
	LICENSE
	pyproject.toml
	README.md
```

## Development Notes

- Python: `>=3.9`
- Packaging: PEP 621 via `pyproject.toml`
- CLI entry point: `common-fun = common_fun.cli:main`

## Contributing

Contributions are welcome.

Suggested workflow:

1. Fork and clone the repository.
2. Create a feature branch.
3. Add or update code and tests.
4. Run local validation checks.
5. Open a pull request with a clear description.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
