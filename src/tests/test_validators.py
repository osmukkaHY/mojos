"""Unit tests for validators"""

import unittest
from datetime import date

from validators import MIN_YEAR, parse_year


class TestParseYear(unittest.TestCase):
    def setUp(self):
        self.this_year = date.today().year

    def test_valid_year_returned_as_int(self):
        self.assertEqual(parse_year("2000"), 2000)

    def test_lower_limit_accepted(self):
        self.assertEqual(parse_year(str(MIN_YEAR)), MIN_YEAR)

    def test_upper_limit_accepted(self):
        self.assertEqual(parse_year(str(self.this_year)), self.this_year)

    def test_year_below_limit_error(self):
        with self.assertRaises(ValueError):
            parse_year(str(MIN_YEAR - 1))

    def test_year_above_limit_error(self):
        with self.assertRaises(ValueError):
            parse_year(str(self.this_year + 1))

    def test_non_int_input_error(self):
        for value in ["", "kirja", "2000.5", None]:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_year(value)
