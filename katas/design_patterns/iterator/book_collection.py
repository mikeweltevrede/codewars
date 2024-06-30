"""Instructions:

- Create a `BookCollection` class to hold a list of `Book` objects.
- Implement methods to add a book (`add_book(book: Book)`) and remove a book by title (`remove_book(title: str)`).
- Ensure the class can return an iterator object for traversing the collection.
"""
from katas.design_patterns.iterator.book import Book
from katas.design_patterns.iterator.book_iterator import BookIterator


class BookCollection:
    def __init__(self) -> None:
        """Collection of books."""
        self.books: dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        """Add book to the collection.

        :param book: A book to add to the collection.
        :raises KeyError: When the title of the book is already in the collection.
        """
        if (title := book.title) in self.books:
            raise KeyError(f"Book with title '{title}' is already in the collection.")

        self.books[title] = book

    def remove_book(self, title: str) -> None:
        """Remove a book from the collection by title.

        :param title: Title of the book to remove.
        """
        self.books.pop(title, None)

    def iterator(self) -> BookIterator:
        """Return an iterator to traverse the book collection.

        :return: Book iterator instance.
        """
        return self.__iter__()

    def __iter__(self) -> BookIterator:
        """Return an iterator to traverse the book collection.

        :return: Book iterator instance.
        """
        return BookIterator(books=list(self.books.values()))
