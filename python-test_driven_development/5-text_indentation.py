#!/usr/bin/python3
"""
This module defines a function `text_indentation` that prints a text
with 2 new lines after each of these characters: `.`, `?`, and `:`.
"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text:
        print("")
        return

    result = ""
    skip_space = False
    for char in text:
        if char in ['.', '?', ':']:
            result += char + "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            result += char
            skip_space = False

    print(result.strip(), end="")
