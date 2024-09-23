#!/usr/bin/python3
"""Module pour la fonction is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Vérifie si obj est une instance ou hérite de a_class."""
    return isinstance(obj, a_class)
