#!/usr/bin/python3
"""Module pour la fonction is_same_class."""


def is_same_class(obj, a_class):
    """Vérifie si obj est une instance exacte de a_class."""
    return type(obj) is a_class
