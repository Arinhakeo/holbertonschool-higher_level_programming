#!/usr/bin/python3
"""
This module defines a Square class with printing functionality.
"""

class Square:
    """
    A class that defines a square with printing functionality.
    
    Attributes:
       __size (int): The size of the square's side.
    """

    def __init__(self, size=0):
       """
       Initializes a new Square instance with optional size.

       Args:
           size (int, optional): The size of the square. Defaults to 0.
       """
       self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
