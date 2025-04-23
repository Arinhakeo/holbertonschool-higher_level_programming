#!/usr/bin/python3
"""Module PoissonVolant

Ce module définit les classes Poisson, Oiseau et PoissonVolant,
démontrant l'héritage multiple.
"""


class Poisson:
    """Classe Poisson représentant un poisson."""

    def nager(self):
        """Affiche que le poisson nage."""
        print("Le poisson nage")

    def habitat(self):
        """Affiche l'habitat du poisson."""
        print("Le poisson vit dans l'eau")


class Oiseau:
    """Classe Oiseau représentant un oiseau."""

    def voler(self):
        """Affiche que l'oiseau vole."""
        print("L'oiseau vole")

    def habitat(self):
        """Affiche l'habitat de l'oiseau."""
        print("L'oiseau vit dans le ciel")


class PoissonVolant(Poisson, Oiseau):
    """Classe PoissonVolant héritant de Poisson et Oiseau."""

    def nager(self):
        """Affiche que le poisson volant nage."""
        print("Le poisson volant nage !")

    def voler(self):
        """Affiche que le poisson volant plane."""
        print("Le poisson volant plane !")

    def habitat(self):
        """Affiche l'habitat du poisson volant."""
        print("Le poisson volant vit dans l'eau et le ciel !")


if __name__ == "__main__":
    # Test des fonctionnalités de PoissonVolant
    poisson_volant = PoissonVolant()
    poisson_volant.nager()
    poisson_volant.voler()
    poisson_volant.habitat()

    # Affichage de l'ordre de résolution des méthodes (MRO)
    print(PoissonVolant.mro())
