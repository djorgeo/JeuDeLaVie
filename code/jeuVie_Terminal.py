#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Le module jeuVie_Terminal permet de lancer la version non graphique du jeu de la vie.
"""

from grille import Grille
import time


def efface_ecran():
    """ Cette fonction permet d'effacer l'écran dans un terminal ANSI. """
    print("\u001B[H\u001B[J")


def main():
    """ C'est la fonction principale du module. Elle permet de lancer une simulation du jeu de la vie
    sur le terminal en partant d'une configuration initiale aléatoire avec 50% de cellules vivantes. """
    vie = Grille(10, 15, 'torique')
    vie.remplir_alea(50)
    vie.affecte_voisins()
    while True:
        efface_ecran()
        print(vie)
        print("\n")
        time.sleep(0.2)
        vie.jeu()
        vie.actualise()


if __name__ == "__main__":
    main()
