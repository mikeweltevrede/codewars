import pytest

from katas.design_patterns.iterator.book import Book


class TestBook:
    @pytest.fixture()
    def book(self) -> Book:
        return Book(title="Foo", author="Mike Weltevrede", year=2024)

    def test_attribute_title_is_present(self, book):
        assert hasattr(book, "title")

    def test_attribute_author_is_present(self, book):
        assert hasattr(book, "author")

    def test_attribute_year_is_present(self, book):
        assert hasattr(book, "year")
