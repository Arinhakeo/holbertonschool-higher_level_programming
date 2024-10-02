#!/usr/bin/python3
"""Module pour convertir un objet en chaîne JSON"""


def to_json_string(my_obj):
    """Convertit un objet en sa représentation JSON"""
    import json
    return json.dumps(my_obj)
