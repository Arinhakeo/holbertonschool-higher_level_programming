#!/usr/bin/python3
"""Module Mixins

Ce module démontre l'utilisation des Mixins en Python avec deux classes
de mixin et une classe Dragon qui les utilise.
"""


class MixinNager:
    """Mixin fournissant la fonctionnalité de nage."""

    def nager(self):
        """Affiche que la créature nage."""
        print("La créature nage !")


class MixinVoler:
    """Mixin fournissant la fonctionnalité de vol."""

    def voler(self):
        """Affiche que la créature vole."""
        print("La créature vole !")


class Dragon(MixinNager, MixinVoler):
    """Classe Dragon héritant de MixinNager et MixinVoler."""

    def rugir(self):
        """Affiche que le dragon rugit."""
        print("Le dragon rugit !")


if __name__ == "__main__":
    # Test des fonctionnalités du Dragon
    draco = Dragon()
    draco.nager()  # Affiche: La créature nage !
    draco.voler()  # Affiche: La créature vole !
    draco.rugir()  # Affiche: Le dragon rugit !
