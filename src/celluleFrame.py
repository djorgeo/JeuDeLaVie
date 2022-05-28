#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
celluleFrame est un module utilisé uniquement par la version graphique du jeu.
Ce module contient l'implémentation de la classe CelluleFrame qui est au centre
de la version graphique du projet, car il s'agit de l'élément de base de l'interface graphique
du jeu.
"""

from __future__ import annotations
from typing import List
from cellule import Cellule
import tkinter as tk


class CelluleFrame(tk.Frame, Cellule):
    """
    Classe de base de l'interface graphique. Elle hérite de la classe Cellule et permet d'implémenter 
    les caractéristiques graphiques d'une cellule du jeu de la vie. 
    master: il s'agit du composant graphique parent de la cellule.
    height: hauteur de la cellule.
    width: largeur de la cellule.
    """

    DEATH_CELL_BG = "#E8F9FD"
    """Couleur de fond à utilisée pour les cellules mortes"""
    LIVING_CELL_BG = "#2155CD"
    """Couleur de fond à utilisée pour les cellules vivantes"""
    HOVER_CELL_BG = "#79DAE8"
    """Couleur de fond à utiliser lorsqu'on survole une cellule"""

    def __init__(self: CelluleFrame, master, height, width) -> None:
        """ Constructeur de la classe CelluleFrame """

        super().__init__(master=master, height=height, width=width, bg=self.DEATH_CELL_BG,
                         highlightbackground=self.HOVER_CELL_BG, highlightthickness="1")
        Cellule.__init__(self)
        self.bg = self.DEATH_CELL_BG

    def basculer(self: CelluleFrame) -> None:
        """ Méthode qui permet de mettre à jour l'état actuel de la cellule en lui affectant
        la valeur de l'état futur. Cette Méthode permet également de changer la couleur de fond
        en fonction de l'état courant de la cellule."""
        Cellule.basculer(self)
        if self.actuel:
            self.bg = self.LIVING_CELL_BG
            self["bg"] = self.LIVING_CELL_BG
        else:
            self.bg = self.DEATH_CELL_BG
            self["bg"] = self.DEATH_CELL_BG


if __name__ == "__main__":
    """
    Test de la classe Cellule

    +------------+------------+------------+
    | c11 en vie | c12 morte  | c13 morte  |
    +------------+------------+------------+
    | c21 morte  | c22 morte  | c23 morte  |
    +------------+------------+------------+
    | c31 en vie | c32 en vie | c33 morte  |
    +------------+------------+------------+

    qui doit évoluer en 

    +------------+------------+------------+
    | c11 morte  | c12 morte  | c13 morte  |
    +------------+------------+------------+
    | c21 en vie | c22 en vie | c23 morte  |
    +------------+------------+------------+
    | c31 morte  | c32 morte  | c33 morte  |
    +------------+------------+------------+

    """

    # création des cellules
    c11 = CelluleFrame(master=None, height=10, width=10)
    c12 = CelluleFrame(master=None, height=10, width=10)
    c13 = CelluleFrame(master=None, height=10, width=10)
    c21 = CelluleFrame(master=None, height=10, width=10)
    c22 = CelluleFrame(master=None, height=10, width=10)
    c23 = CelluleFrame(master=None, height=10, width=10)
    c31 = CelluleFrame(master=None, height=10, width=10)
    c32 = CelluleFrame(master=None, height=10, width=10)
    c33 = CelluleFrame(master=None, height=10, width=10)
    c11.actuel = True
    c31.actuel = True
    c32.actuel = True

    # test de la cellule c11
    assert c11.actuel == True
    assert c11.futur == False
    assert c11.voisins == []
    # test de la cellule c22
    assert c22.actuel == False
    assert c22.futur == False
    assert c22.voisins == []

    # test de la méthode est_vivant()
    assert c33.est_vivant() == False
    assert c31.est_vivant() == True

    # test de la méthode set_voisins()
    c11.set_voisins([c12, c21, c22])
    c12.set_voisins([c11, c13, c21, c22, c23])
    c13.set_voisins([c12, c22, c23])
    c21.set_voisins([c11, c12, c22, c31, c32])
    c22.set_voisins([c11, c12, c13, c21, c23, c31, c32, c33])
    c23.set_voisins([c12, c22, c23])
    c31.set_voisins([c21, c22, c32])
    c32.set_voisins([c21, c22, c23, c31, c33])
    c33.set_voisins([c22, c23, c32])

    # test de la méthode get_voisins()
    assert c22.get_voisins() == [c11, c12, c13, c21, c23, c31, c32, c33]
    assert c33.get_voisins() == [c22, c23, c32]

    # tests de la méthode calcule_etat_futur
    for cel in [c11, c12, c13, c21, c22, c23, c31, c32, c33]:
        cel.calcule_etat_futur()

    for cel in [c11, c12, c13, c21, c22, c23, c31, c32, c33]:
        cel.basculer()

    assert c11.actuel == False
    assert c12.actuel == False
    assert c13.actuel == False
    assert c21.actuel == True
    assert c22.actuel == True
    assert c23.actuel == False
    assert c31.actuel == False
    assert c32.actuel == False
    assert c33.actuel == False
