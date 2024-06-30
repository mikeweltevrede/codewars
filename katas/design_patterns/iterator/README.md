# Iterator Design Pattern Kata: Book Collection
I asked ChatGPT to generate a kata to practise implementing the Iterator design pattern.

## Objective
Implement the Iterator design pattern to traverse a collection of books in a sequential manner without exposing the underlying structure of the collection.

## Requirements
- **Book Class**:
    - Create a `Book` class with the following attributes:
        - `title`: The title of the book.
        - `author`: The author of the book.
        - `year`: The publication year of the book.

- **BookCollection Class**:
    - Create a `BookCollection` class to hold a list of `Book` objects.
    - Implement methods to add a book (`add_book(book: Book)`) and remove a book by title (`remove_book(title: str)`).
    - Ensure the class can return an iterator object for traversing the collection.

- **Iterator Interface**:
    - Define an `Iterator` interface with the following methods:
        - `has_next()`: Returns `True` if there are more books to iterate over, otherwise returns `False`.
        - `next()`: Returns the next book in the collection. If no more books are available, raise a `StopIteration` exception.

- **BookIterator Class**:
    - Create a `BookIterator` class that implements the `Iterator` interface.
    - The iterator should be able to traverse the `BookCollection` sequentially.
    - The `BookIterator` should keep track of the current position in the collection and provide the next book when requested.

- **Client Code**:
    - Demonstrate the use of the iterator by creating a `BookCollection`, adding several `Book` objects, and then using the `BookIterator` to iterate through the collection.
    - Print the title and author of each book during the iteration.

## Additional Requirements
- The iterator should support iteration over an empty collection without errors.
- Ensure the `BookCollection` class does not expose its internal list directly to the client code.
- Provide meaningful error messages or exceptions for invalid operations, such as trying to iterate beyond the end of the collection.

## Example Usage
```python
# Create a collection of books
book_collection = BookCollection()
book_collection.add_book(Book("1984", "George Orwell", 1949))
book_collection.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
book_collection.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))

# Get an iterator for the collection
iterator = book_collection.iterator()

# Iterate through the collection
while iterator.has_next():
    book = iterator.next()
    print(f"Title: {book.title}, Author: {book.author}")
```

This kata will help you practice implementing the Iterator design pattern while working with a real-world scenario involving a collection of books.
