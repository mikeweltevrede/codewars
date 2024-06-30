"""Instructions:

- Create a `BookIterator` class that implements the `Iterator` interface.
- The iterator should be able to traverse the `BookCollection` sequentially.
- The `BookIterator` should keep track of the current position in the collection and provide the next book when requested.
"""
from typing import Self, override

from katas.design_patterns.iterator.book import Book
from katas.design_patterns.iterator.iterator import Iterator


class BookIterator(Iterator):
    def __init__(self, books: list[Book]):
        """Iterator for traversing a book collection.

        :param books: List of books to traverse.
        """
        self.books = books
        self.index = 0

    @override
    def __iter__(self: Self) -> Self:
        return self

    @override
    def __next__(self) -> Book:
        if not self.has_next():
            raise StopIteration
        book = self.books.pop(0)
        self.index += 1
        return book

    @override
    def has_next(self) -> bool:
        return len(self.books) > 0
