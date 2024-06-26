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
        assert BookCollection().books == {}

    def test_add_book_adds_book_to_books_attribute(self, book_collection, book):
        book_collection.add_book(book)

        assert book in book_collection.books.values()

    def test_add_book_raises_error_when_book_is_added_with_same_title_as_existing_book(self, book_collection):
        book_collection.add_book(Book(title="Foo", author="Bar", year=2024))

        with pytest.raises(KeyError, match="Book with title 'Foo' is already in the collection."):
            book_collection.add_book(Book(title="Foo", author="Baz", year=2020))

    def test_remove_book_can_remove_a_book_by_title_from_collection(self, book_collection, book):
        book_collection.add_book(book)
        book_collection.remove_book(title=book.title)

        assert book not in book_collection.books.values()

    def test_remove_book_passes_silently_if_book_is_removed_that_is_not_in_the_collection(self, book_collection):
        book_collection.remove_book(title="FooBar")
