#!/usr/bin/python3
"""Module pour convertir une chaîne JSON en objet Python"""
import json


def load_to_json_file(my_obj, filename):
    """
my_obj:
objet à convertir
    filename:
pour mettre l'objet dedans
"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
