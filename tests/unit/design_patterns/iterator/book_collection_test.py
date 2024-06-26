import pytest

from katas.design_patterns.iterator.book import Book
from katas.design_patterns.iterator.book_collection import BookCollection


class TestBookCollection:
    @pytest.fixture()
    def book_collection(self) -> BookCollection:
        return BookCollection()

    @pytest.fixture()
    def book(self) -> Book:
        return Book(title="Foo", author="Bar", year=2024)

    def test_no_books_upon_initialization(self):
        assert BookCollection().books == []

    def test_add_book_adds_book_to_books_attribute(self, book_collection, book):
        book_collection.add_book(book)

        assert book in book_collection.books

    def test_remove_book_can_remove_a_book_by_title_from_collection(self, book_collection, book):
        book_collection.add_book(book)
        book_collection.remove_book(title=book.title)

        assert book not in book_collection.books
