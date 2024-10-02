#!/usr/bin/python3
"""Module pour écrire une chaîne dans un fichier."""

def write_file(filename="", text=""):
    """Écrit une chaîne dans un fichier et retourne le nombre de caractères écrits."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
