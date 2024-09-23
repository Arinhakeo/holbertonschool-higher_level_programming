#!/usr/bin/env python3
"""Classe VerboseList."""


class VerboseList(list):
    """Liste avec notifications."""

    def append(self, item):
        """Ajoute un élément."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Étend la liste."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Supprime un élément."""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """Retire et renvoie un élément."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
