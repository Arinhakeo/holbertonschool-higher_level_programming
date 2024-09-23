#!/usr/bin/python3
"""Module définissant la classe Square."""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Classe représentant un carré."""

    def __init__(self, size):
        """Initialise un carré."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
