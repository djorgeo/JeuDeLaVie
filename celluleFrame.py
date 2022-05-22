#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import List
from cellule import Cellule
import tkinter as tk



class CelluleFrame(tk.Frame, Cellule):
    """ classe CelluleFrame pour la version graphique du Jeu de la vie """

    def __init__(self: CelluleFrame, master, height, width) -> None:
        """ Constructeur de la classe CelluleFrame """
        self.DEATH_CELL_BG = "#E8F9FD"
        self.LIVING_CELL_BG = "#2155CD"
        self.HOVER_CELL_BG = "#79DAE8"
        
        super().__init__(master=master, height=height, width=width, bg=self.DEATH_CELL_BG,
                         highlightbackground=self.HOVER_CELL_BG, highlightthickness="1")
        Cellule.__init__(self)
        self.bg = self.DEATH_CELL_BG
    

    def basculer(self: CelluleFrame) -> None:
        """ affecte l'état futur de la cellule à l'état actuel """
        self.actuel = self.futur
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
