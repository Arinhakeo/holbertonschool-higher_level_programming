#!/usr/bin/python3
"""Module pour ajouter une chaîne à un fichier."""

def append_write(filename="", text=""):
       """Ajoute une chaîne à la fin d'un fichier et retourne le nombre de caractères ajoutés."""
       with open(filename, 'a', encoding='utf-8') as file:
           return file.write(text)
