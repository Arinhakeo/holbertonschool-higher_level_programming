#!/usr/bin/python3
"""Module pour la fonction class_to_json"""


def class_to_json(obj):
    """Retourne la description dictionnaire d'un objet pour JSON"""
    return obj.__dict__
