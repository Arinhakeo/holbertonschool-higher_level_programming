#!/usr/bin/python3
"""Module pour convertir une chaîne JSON en objet Python"""


def load_from_json_string(my_str):
    """Convertit une chaîne JSON en objet Python"""
    import json
    return json.loads(my_str)
