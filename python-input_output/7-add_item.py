#!/usr/bin/python3
"""Script pour ajouter des arguments à une liste et sauvegarder en JSON"""


import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
my_list = load_from_json_file(filename) if exists(filename) else []
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
