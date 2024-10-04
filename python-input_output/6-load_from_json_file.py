#!/usr/bin/python3
"""Module pour convertir une chaîne JSON en objet Python"""
import json


def load_from_json_string(my_str):
    """Convertit une chaîne JSON en objet Python"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
