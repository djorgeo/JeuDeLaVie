#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
grilleFrame est un module utilisé uniquement par la version graphique du jeu.
Ce module contient l'implémentation de la classe GrilleFrame qui est très importante
pour la version graphique du projet, car il s'agit en quelque sorte du terrain sur lequel
se déroule le jeu de la vie.
"""

from __future__ import annotations
from celluleFrame import CelluleFrame
from grille import Grille
from typing import List
from random import random
import tkinter as tk


class GrilleFrame(tk.Frame, Grille):
    """
    Cette classe hérite de la classe Grille et permet d'implémenter la grille sur laquelle
    se déroule le jeu de la vie qui peut être plane ou torique.
    master: il s'agit du composant graphique parent de la grille.
    nbLignes: nombre de lignes de la grille.
    nbColonnes: nombre de colonnes de la grille.
    typeg: type de grille (plane ou torique).
    """

    def __init__(self: GrilleFrame, master, nbLignes: int, nbColonnes: int, typeg: str) -> None:
        """ Constructeur de la classe CelluleFrame """
        super().__init__(master=master, bg="#E8F9FD",
                         highlightbackground="#2155CD", highlightthickness="1")
        Grille.__init__(self, nbLignes, nbColonnes, typeg)

        # Initialisation des cellules
        self.matrix = []
        for i in range(self.nbLignes):
            self.grid_rowconfigure(i, weight=1)
            row = []
            for j in range(self.nbColonnes):
                self.grid_columnconfigure(j, weight=1)
                cell = CelluleFrame(master=self,
                                    height=self.winfo_height() // self.nbLignes,
                                    width=self.winfo_width() // self.nbColonnes)
                cell.grid(row=i, column=j, sticky="NSEW")
                # Associer le click gauche de la souris sur la cellule à un changement d'etat de la cellule
                cell.bind("<Button-1>", self.on_cell_click)
                # Associer le survol de la souris sur la cellule à un changement de couleur de fond
                cell.bind("<Enter>", self.on_cell_hover)
                # Quand on arrete de survoler une cellule, sa couleur de fond est rétablie
                cell.bind("<Leave>", self.on_cell_leave)
                row.append(cell)
            self.matrix.append(row)

        # Initialisation des voisins
        self.affecte_voisins()

    def remplir_alea(self, taux=10):
        """ Méthode qui permet de remplir aléatoirement la Grille avec un certain taux de cellules vivantes.
        Le paramètre "taux" représente le pourcentage de cellules vivantes à créer sur la grille. """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.mourir()
                cellule.basculer()
                if random() <= (taux / 100):
                    cellule.naitre()
                    cellule.basculer()

    @staticmethod
    def on_cell_click(event):
        """ Méthode qui permet de changer l'état d'une cellule de la grille lorsqu'on clique dessus. """
        if event.widget.est_vivant():
            event.widget.mourir()
            event.widget.basculer()
        else:
            event.widget.naitre()
            event.widget.basculer()
        # Réinitialiser le compteur d'itération de l'application
        event.widget.winfo_toplevel().currentIter.set("0")

    def on_cell_hover(self, event):
        """ Méthode qui permet de changer la couleur de fond d'une cellule de la grille
        lorsqu'elle est survolée. """
        cell = event.widget
        cell["bg"] = cell.HOVER_CELL_BG

    @staticmethod
    def on_cell_leave(event):
        """ Méthode qui permet de rétablir la couleur de fond d'une cellule lorsqu'elle n'est plus survolée. """
        cell = event.widget
        cell["bg"] = cell.bg


if __name__ == "__main__":
    maGrille = GrilleFrame(master=None, nbLignes=15, nbColonnes=10, typeg='plane')

    # test d'accès au attributs
    assert maGrille.nbLignes == 15
    assert maGrille.nbColonnes == 10
    assert maGrille.get_nbLignes() == 15
    assert maGrille.get_nbColonnes() == 10

    # test de la méthode dans_grille()
    assert maGrille.dans_grille(0, 0) == True
    assert maGrille.dans_grille(15, 10) == False
    assert maGrille.dans_grille(8, 8) == True

    # test de la méthode get_voisins()
    assert len(maGrille.get_voisins(0, 0)) == 3
    assert len(maGrille.get_voisins(0, 1)) == 5
    assert len(maGrille.get_voisins(1, 0)) == 5
    assert len(maGrille.get_voisins(1, 1)) == 8

    # répétition des tests avec une grille torique
    maGrille2 = GrilleFrame(master=None, nbLignes=15, nbColonnes=10, typeg='torique')

    # test d'accès au attributs
    assert maGrille2.nbLignes == 15
    assert maGrille2.nbColonnes == 10
    assert maGrille2.get_nbLignes() == 15
    assert maGrille2.get_nbColonnes() == 10

    # test de la méthode dans_grille()
    assert maGrille2.dans_grille(0, 0) == True
    assert maGrille2.dans_grille(15, 10) == False
    assert maGrille2.dans_grille(8, 8) == True

    # test de la méthode get_voisins()
    assert len(maGrille2.get_voisins(0, 0)) == 8
    assert len(maGrille2.get_voisins(0, 1)) == 8
    assert len(maGrille2.get_voisins(1, 0)) == 8
    assert len(maGrille2.get_voisins(1, 1)) == 8
