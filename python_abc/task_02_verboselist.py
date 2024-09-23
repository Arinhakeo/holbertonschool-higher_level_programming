#!/usr/bin/env python3
"""Classes Shape, Circle, Rectangle et fonction shape_info."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite Shape."""

    @abstractmethod
    def area(self):
        """Méthode abstraite aire."""
        pass

    @abstractmethod
    def perimeter(self):
        """Méthode abstraite périmètre."""
        pass


class Circle(Shape):
    """Classe Circle."""

    def __init__(self, radius):
        """Initialisation avec rayon."""
        self.radius = radius

    def area(self):
        """Calcul de l'aire."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calcul du périmètre."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Classe Rectangle."""

    def __init__(self, width, height):
        """Initialisation avec largeur et hauteur."""
        self.width = width
        self.height = height

    def area(self):
        """Calcul de l'aire."""
        return self.width * self.height

    def perimeter(self):
        """Calcul du périmètre."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'une forme."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
