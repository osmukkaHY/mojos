"""Unit tests for BibTeX generation functions"""

import unittest
from unittest.mock import patch
from app import bibtex_format_book, bibtex_format_article, bibtex_format_inproceeding

class TestBibtexFormatBook(unittest.TestCase):
    def setUp(self):
        self.data = {"id": 67,
                     "reference_name": "TEST",
                     "title": "Test-title",
                     "author": "Test-author",
                     "year": 1967,
                     "publisher": "Test-pub",
                     "tag": "Test-Tag"}

    def test_bibtex_format_generated_correctly(self):
        expected_bibtex = """@book{TEST,
    author = {Test-author},
    title = {Test-title},
    year = {1967},
    publisher = {Test-pub}
}"""
        with patch("app.get_book", return_value=self.data):
            result = bibtex_format_book(self.data["id"])

        self.assertEqual(result["string"], expected_bibtex)

    def test_return_dict_reference_type_is_correct(self):
        with patch("app.get_book", return_value=self.data):
            result = bibtex_format_book(self.data["id"])

        self.assertEqual(result["reference_type"], "book")

    def test_return_dict_reference_id_is_correct(self):
        with patch("app.get_book", return_value=self.data):
            result = bibtex_format_book(self.data["id"])

        self.assertEqual(result["reference_id"], self.data["id"])
