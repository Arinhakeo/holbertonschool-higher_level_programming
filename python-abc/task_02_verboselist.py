#!/usr/bin/python3
"""Module ListeVerbose

Ce module définit la classe ListeVerbose, qui étend la classe list native
et affiche des messages pour certaines opérations de liste.
"""


class ListeVerbose(list):
    """Classe ListeVerbose

    Étend la classe list native et affiche des messages pour les opérations
    ajouter, étendre, supprimer et retirer.
    """

    def ajouter(self, element):
        """Ajoute un élément à la liste et affiche un message.

        Args:
            element: L'élément à ajouter à la liste.
        """
        super().append(element)
        print(f"Ajouté [{element}] à la liste.")

    def etendre(self, iterable):
        """Étend la liste avec les éléments de l'itérable et affiche un message.

        Args:
            iterable: Un itérable dont les éléments seront ajoutés à la liste.
        """
        nombre = len(iterable)
        super().extend(iterable)
        print(f"Étendu la liste avec [{nombre}] éléments.")

    def supprimer(self, element):
        """Supprime la première occurrence de l'élément et affiche un message.

        Args:
            element: L'élément à supprimer de la liste.
        """
        super().remove(element)
        print(f"Supprimé [{element}] de la liste.")

    def retirer(self, index=-1):
        """Retire et renvoie l'élément à l'index donné et affiche un message.

        Args:
            index: L'index de l'élément à retirer (par défaut, le dernier).

        Returns:
            L'élément qui a été retiré.
        """
        element = super().pop(index)
        print(f"Retiré [{element}] de la liste.")
        return element
