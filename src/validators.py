"""Checking if years are valid"""

from datetime import date

MIN_YEAR = 1800


def parse_year(value):
    """Return the year as an integer or raise ValueError, if it's invalid."""
    max_year = date.today().year
    message = f"Vuoden pitää olla kokonaisluku väliltä {MIN_YEAR}-{max_year}"

    try:
        year = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(message) from exc

    if MIN_YEAR > year or max_year < year:
        raise ValueError(message)
    return year
