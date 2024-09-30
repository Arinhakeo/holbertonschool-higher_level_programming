#!/usr/bin/python3
def read_file(filename=""):
    """Lit un fichier et imprime son contenu."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())