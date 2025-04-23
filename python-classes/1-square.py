#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""

class Square:
    """
    This class defines a square with a private size attribute.

    Attributes:
        __size (int): The size of the square's side.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
