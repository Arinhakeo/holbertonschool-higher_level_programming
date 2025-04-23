#!/usr/bin/python3
'''
fonction sérialize et désérialise
'''

import json


def serialize_and_save_to_file(data, filename):
    '''
    Fonction pour sérialiser et sauvegarder le dictionnaire dans un fichier JSON
    '''
    with open(filename, 'w') as file:
        json.dump(data, file)
        print(f"Data serialized and saved to '{filename}'.")

def load_and_deserialize(filename):
    '''
    Fonction pour désérialiser 
    '''
    with open(filename, 'r') as file:
        data = json.load(file)
        return data