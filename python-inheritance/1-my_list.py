#!/usr/bin/python3
"""Module définissant la classe MyList."""


class MyList(list):
    """Classe héritant de list avec méthode d'impression triée."""

    def print_sorted(self):
        """Imprime la liste triée."""
        print(sorted(self))
