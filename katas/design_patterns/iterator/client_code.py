from katas.design_patterns.iterator.book import Book
from katas.design_patterns.iterator.book_collection import BookCollection


def main() -> None:
    """Example client code.

    - Demonstrate the use of the iterator by creating a `BookCollection`, adding several `Book` objects, and then using
        the `BookIterator` to iterate through the collection.
    - Print the title and author of each book during the iteration.
    """
    book_collection = BookCollection()
    book_collection.add_book(Book(title="Percy Jackson and the Lightning Thief", author="Rick Riordan", year=2005))
    book_collection.add_book(Book(title="Et Heanige Preenske", author="Herman Finkers", year=2023))
    book_collection.add_book(Book(title="East", author="Meera Sodha", year=2019))

    for book in book_collection.iterator():
        print(f"{book.title=} | {book.author=}")


if __name__ == "__main__":
    main()
