from katas.design_patterns.iterator.book import Book
from katas.design_patterns.iterator.book_iterator import BookIterator


class TestBookIterator:
    def test_next_returns_first_element_in_books(self):
        book_iterator = BookIterator(
            books=[
                book1 := Book(title="Title1", author="Author1", year=2024),
                Book(title="Title2", author="Author2", year=2024),
            ]
        )

        assert book_iterator.__next__() == book1

    def test_has_next_returns_true_if_there_is_one_book_left(self):
        book_iterator = BookIterator(books=[Book(title="Title1", author="Author1", year=2024)])

        assert book_iterator.has_next() is True

    def test_has_next_returns_true_if_there_are_two_books_left(self):
        book_iterator = BookIterator(
            books=[
                Book(title="Title1", author="Author1", year=2024),
                Book(title="Title2", author="Author2", year=2024),
            ]
        )

        assert book_iterator.has_next() is True

    def test_has_next_returns_false_if_there_are_no_books_left(self):
        assert BookIterator(books=[]).has_next() is False
