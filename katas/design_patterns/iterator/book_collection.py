"""Instructions:

- Create a `BookCollection` class to hold a list of `Book` objects.
- Implement methods to add a book (`add_book(book: Book)`) and remove a book by title (`remove_book(title: str)`).
- Ensure the class can return an iterator object for traversing the collection.
"""
from katas.design_patterns.iterator.book import Book


class BookCollection:
    def __init__(self) -> None:
        """Collection of books."""
        self.books: dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        """Add book to the collection.

        :param book: A book to add to the collection.
        """
        if (title := book.title) in self.books:
            raise KeyError(f"Book with title '{title}' is already in the collection.")

        self.books[title] = book

    def remove_book(self, title: str) -> None:
        """Remove a book from the collection by title.

        :param title: Title of the book to remove.
        """
        self.books = dict(filter(lambda book_title: book_title != title, self.books.keys()))
