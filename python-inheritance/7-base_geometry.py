#!/usr/bin/python3
"""Module définissant la classe BaseGeometry."""


class BaseGeometry:
    """Classe de base pour la géométrie."""

    def area(self):
        """Calcule l'aire."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que value est un entier positif."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
