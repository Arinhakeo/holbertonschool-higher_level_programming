#!/usr/bin/env python3
"""Classe CountedIterator."""


class CountedIterator:
    """Itérateur avec compteur."""

    def __init__(self, iterable):
        """Initialisation."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Renvoie l'élément suivant."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Renvoie le nombre d'éléments itérés."""
        return self.count
