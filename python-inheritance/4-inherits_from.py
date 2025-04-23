#!/usr/bin/python3
"""Module pour la fonction inherits_from."""


def inherits_from(obj, a_class):
    """Vérifie si obj hérite de a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
