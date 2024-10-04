#!/usr/bin/python3
"""
in this mosule a function to uncode a format json to abject
"""


import json


def from_json_string(my_str):
    """
    my_str:
      the string json to convert
    objecs:
        returned as abject type
    """

    objecs = json.loads(my_str)
    return objecs
