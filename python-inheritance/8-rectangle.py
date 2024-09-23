#!/usr/bin/python3
"""Module définissant la classe Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Classe représentant un rectangle."""

    def __init__(self, width, height):
        """Initialise un rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
