#!/usr/bin/env python3
"""Classes Fish, Bird et FlyingFish."""


class Fish:
    """Classe Fish."""

    def swim(self):
        """Nage."""
        print("The fish is swimming")

    def habitat(self):
        """Habitat."""
        print("The fish lives in water")


class Bird:
    """Classe Bird."""

    def fly(self):
        """Vole."""
        print("The bird is flying")

    def habitat(self):
        """Habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Classe FlyingFish."""

    def fly(self):
        """Vole."""
        print("The flying fish is soaring!")

    def swim(self):
        """Nage."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Habitat."""
        print("The flying fish lives both in water and the sky!")
