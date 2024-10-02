#!/usr/bin/python3
"""Module définissant la classe Student"""


class Student:
    """Représente un étudiant"""

    def __init__(self, first_name, last_name, age):
        """Initialise un nouvel étudiant"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retourne un dictionnaire représentant l'étudiant"""
        return self.__dict__
