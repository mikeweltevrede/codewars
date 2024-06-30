"""Instructions

- Define an `Iterator` interface with the following methods:
    - `has_next()`: Returns `True` if there are more books to iterate over, otherwise returns `False`.
    - `next()`: Returns the next book in the collection. If no more books are available, raise a `StopIteration`
        exception.
"""
import collections
from abc import abstractmethod


class Iterator[T](collections.abc.Iterator):
    @abstractmethod
    def __next__(self) -> T:
        """Yields next element in the iterable object."""

    @abstractmethod
    def has_next(self) -> bool:
        """Determine is there are more items to iterate over.

        :return: Whether the iterable has more items.
        """
