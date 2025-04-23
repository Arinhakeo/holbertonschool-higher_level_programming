#!/usr/bin/python3
"""Module contenant une fonction pour lire un fichier."""


def read_file(filename=""):
    """Lit un fichier et imprime son contenu."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
