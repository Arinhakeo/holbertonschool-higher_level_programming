#!/usr/bin/env python3
"""Classes Animal, Dog et Cat."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite Animal."""

    @abstractmethod
    def sound(self):
        """Méthode abstraite son."""
        pass


class Dog(Animal):
    """Classe Dog."""

    def sound(self):
        """Son du chien."""
        return "Bark"


class Cat(Animal):
    """Classe Cat."""

    def sound(self):
        """Son du chat."""
        return "Meow"
