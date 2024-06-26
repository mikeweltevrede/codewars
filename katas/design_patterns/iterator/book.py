"""Instructions:

- Create a `Book` class with the following attributes:
    - `title`: The title of the book.
    - `author`: The author of the book.
    - `year`: The publication year of the book.
"""


class Book:
    def __init__(self, title: str, author: str, year: int):
        """Simulate behaviour for a book.

        :param title: Title of the book.
        :param author: Author of the book.
        :param year: Year that the book was published.
        """
        self.title = title
        self.author = author
        self.year = year
