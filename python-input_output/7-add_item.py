#!/usr/bin/python3
"""Script pour ajouter des arguments à une liste et sauvegarder en JSON"""


import sys
import os

# Dynamically import the required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Main function to add command line arguments to a list and save to a
    file."""
    filename = "add_item.json"

    # Initialise la list si elle n'existe pas
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Prend une ligne d'argument
    my_list.extend(sys.argv[1:])

    # Met a jour le json
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()