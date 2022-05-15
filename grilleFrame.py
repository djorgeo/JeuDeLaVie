#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from celluleFrame import CelluleFrame
from typing import List
from random import random
import tkinter as tk


class GrilleFrame(tk.Frame):
    """ classe GrilleFrame pour la version graphique du le Jeu de la vie """

    def __init__(self: GrilleFrame, master, nbLignes: int, nbColonnes: int) -> None:
        """ Constructeur de la classe CelluleFrame """
        super().__init__(master=master, bg="#E8F9FD",
                         highlightbackground="#2155CD", highlightthickness="1")
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes
        self.HOVER_CELL_BG = "#79DAE8"
        self.gridType = "Grille plane"

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

    def dans_grille(self: GrilleFrame, i: int, j: int) -> bool:
        """ teste si le point de coordonnées (i,j) est dans la grille """
        return 0 <= i < self.nbLignes and 0 <= j < self.nbColonnes

    def setXY(self: GrilleFrame, i: int, j: int, cellule: CelluleFrame) -> None:
        """ affecte une nouvelle cellule à la case (i, j) de la grille """
        if self.dans_grille(i, j):
            self.matrix[i][j] = cellule
        else:
            raise IndexError(str(i, j))

    def getXY(self: GrilleFrame, i: int, j: int) -> CelluleFrame:
        """ renvoie la cellule située dans la case (i, j) de la grille """
        if self.dans_grille(i, j):
            return self.matrix[i][j]
        else:
            return None

    def get_nbColonnes(self: GrilleFrame) -> int:
        """ renvoie le nombre de colonnes de la grille """
        return self.nbColonnes

    def get_nbLignes(self: GrilleFrame) -> int:
        """ renvoie le nombre de lignes de la grille """
        return self.nbLignes

    def est_voisin(self, i: int, j: int, x: int, y: int) -> bool:
        """ teste si les cases (i, j) et (x, y) sont voisines dans la grille """
        if self.gridType == "Grille plane":
            return max(abs(x - i), abs(y - j)) == 1
        elif self.gridType == "Grille torique":
            x_dist = abs(x - i)
            if x_dist == self.nbLignes - 1: x_dist = 1
            y_dist = abs(y - j)
            if y_dist == self.nbColonnes - 1: y_dist = 1
            return max(x_dist, y_dist) == 1

    def get_voisins(self: GrilleFrame, x: int, y: int) -> List[CelluleFrame]:
        """ renvoie la liste des voisins d’une cellule """
        voisins = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                i_new = i
                j_new = j
                if i == -1: i_new = self.nbLignes - 1
                if i == self.nbLignes: i_new = 0
                if j == -1: j_new = self.nbColonnes - 1
                if j == self.nbColonnes: j_new = 0

                if self.dans_grille(i_new, j_new) and self.est_voisin(x, y, i_new, j_new):
                    voisins.append(self.getXY(i_new, j_new))
        return voisins

    def affecte_voisins(self: GrilleFrame) -> None:
        """ affecte à chaque cellule de la grille la liste de ses voisins """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.set_voisins(self.get_voisins(i, j))

    def __str__(self: GrilleFrame) -> str:
        """ méthode spéciale pour afficher l'objet sous forme d'une chaîne de caractères """
        chaine = ""
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                chaine += str(self.getXY(i, j))
            chaine += "\n"
        return chaine

    def remplir_alea(self, taux=10):
        """ remplit aléatoirement la Grille avec un certain taux de Cellule vivantes """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.mourir()
                cellule.basculer()
                if random() <= (taux / 100):
                    cellule.naitre()
                    cellule.basculer()

    def jeu(self: GrilleFrame) -> None:
        """ passe en revue toutes les Cellule de la Grille, calcule leur état futur """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.calcule_etat_futur()

    def actualise(self: GrilleFrame) -> None:
        """ bascule toutes les Cellule de la Grille dans leur état futur """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.basculer()

    @staticmethod
    def on_cell_click(event):
        """change l'état d'une cellule lorsqu'on clique dessus"""
        if event.widget.est_vivant():
            event.widget.mourir()
            event.widget.basculer()
        else:
            event.widget.naitre()
            event.widget.basculer()
        # Réinitialiser le compteur d'itération de l'application
        event.widget.winfo_toplevel().currentIter.set("0")

    def on_cell_hover(self, event):
        """change la couleur de fond d'une cellule lorsqu'elle est survolée"""
        cell = event.widget
        cell["bg"] = self.HOVER_CELL_BG

    @staticmethod
    def on_cell_leave(event):
        """rétabli la couleur de fond d'une cellule lorsqu'elle n'est plus survolée"""
        cell = event.widget
        cell["bg"] = cell.bg

    def clignotant(self):
        """initialise la grille pour simuler le clignotant"""
        self.remplir_alea(0)
        i = self.nbLignes // 2 - 1
        j = self.nbColonnes // 2 - 1

        self.matrix[i][j].naitre()
        self.matrix[i][j].basculer()

        self.matrix[i][j + 1].naitre()
        self.matrix[i][j + 1].basculer()

        self.matrix[i][j - 1].naitre()
        self.matrix[i][j - 1].basculer()

        self.winfo_toplevel().currentIter.set("0")
        self.winfo_toplevel().nIteration.set("10")

    def ruche1(self):
        """initialise la grille pour simuler la ruche"""
        self.remplir_alea(0)
        i = self.nbLignes // 2 - 1
        j = self.nbColonnes // 2 - 1

        self.matrix[i][j].naitre()
        self.matrix[i][j].basculer()

        self.matrix[i][j + 1].naitre()
        self.matrix[i][j + 1].basculer()

        self.matrix[i][j + 2].naitre()
        self.matrix[i][j + 2].basculer()

        self.matrix[i][j - 1].naitre()
        self.matrix[i][j - 1].basculer()

        self.winfo_toplevel().currentIter.set("0")
        self.winfo_toplevel().nIteration.set("4")

    def ruche2(self):
        """initialise la grille pour simuler la génération de 4 ruches"""
        self.remplir_alea(0)
        i = self.nbLignes // 2 - 1
        j = self.nbColonnes // 2 - 1

        self.matrix[i][j].naitre()
        self.matrix[i][j].basculer()

        self.matrix[i][j + 1].naitre()
        self.matrix[i][j + 1].basculer()

        self.matrix[i + 1][j + 1].naitre()
        self.matrix[i + 1][j + 1].basculer()

        self.matrix[i + 2][j + 1].naitre()
        self.matrix[i + 2][j + 1].basculer()

        self.matrix[i + 1][j - 1].naitre()
        self.matrix[i + 1][j - 1].basculer()

        self.matrix[i + 2][j - 1].naitre()
        self.matrix[i + 2][j - 1].basculer()

        self.matrix[i + 3][j].naitre()
        self.matrix[i + 3][j].basculer()

        self.winfo_toplevel().currentIter.set("0")
        self.winfo_toplevel().nIteration.set("17")

    def balise(self):
        """initialise la grille pour simuler la balise"""
        self.remplir_alea(0)
        i = self.nbLignes // 2 - 1
        j = self.nbColonnes // 2 - 1

        self.matrix[i][j].naitre()
        self.matrix[i][j].basculer()

        self.matrix[i][j + 1].naitre()
        self.matrix[i][j + 1].basculer()

        self.matrix[i + 1][j + 1].naitre()
        self.matrix[i + 1][j + 1].basculer()

        self.matrix[i + 2][j - 2].naitre()
        self.matrix[i + 2][j - 2].basculer()

        self.matrix[i + 3][j - 2].naitre()
        self.matrix[i + 3][j - 2].basculer()

        self.matrix[i + 3][j - 1].naitre()
        self.matrix[i + 3][j - 1].basculer()

        self.winfo_toplevel().currentIter.set("0")
        self.winfo_toplevel().nIteration.set("10")

    def crapeau(self):
        """initialise la grille pour simuler le crapeau"""
        self.remplir_alea(0)
        i = self.nbLignes // 2 - 1
        j = self.nbColonnes // 2 - 1

        self.matrix[i][j].naitre()
        self.matrix[i][j].basculer()

        self.matrix[i][j + 1].naitre()
        self.matrix[i][j + 1].basculer()

        self.matrix[i][j - 1].naitre()
        self.matrix[i][j - 1].basculer()

        self.matrix[i + 1][j].naitre()
        self.matrix[i + 1][j].basculer()

        self.matrix[i + 1][j + 1].naitre()
        self.matrix[i + 1][j + 1].basculer()

        self.matrix[i + 1][j + 2].naitre()
        self.matrix[i + 1][j + 2].basculer()

        self.winfo_toplevel().currentIter.set("0")
        self.winfo_toplevel().nIteration.set("10")

    def escalier(self):
        """initialise la grille pour simuler l'escalier qui se transforme en 4 blocs stables"""
        self.remplir_alea(0)
        i = self.nbLignes // 2 - 1
        j = self.nbColonnes // 2 - 1

        self.matrix[i][j].naitre()
        self.matrix[i][j].basculer()

        self.matrix[i][j + 1].naitre()
        self.matrix[i][j + 1].basculer()

        self.matrix[i + 1][j].naitre()
        self.matrix[i + 1][j].basculer()

        self.matrix[i + 1][j - 1].naitre()
        self.matrix[i + 1][j - 1].basculer()

        self.matrix[i + 2][j - 1].naitre()
        self.matrix[i + 2][j - 1].basculer()

        self.matrix[i + 2][j - 2].naitre()
        self.matrix[i + 2][j - 2].basculer()

        self.winfo_toplevel().currentIter.set("0")
        self.winfo_toplevel().nIteration.set("63")

    def pulsard(self):
        """initialise la grille pour simuler le pulsard qui oscille avec une période de 3"""
        self.remplir_alea(0)
        i = self.nbLignes // 2 - 1
        j = self.nbColonnes // 2 - 1

        self.matrix[i][j].naitre()
        self.matrix[i][j].basculer()

        self.matrix[i + 4][j].naitre()
        self.matrix[i + 4][j].basculer()

        for k in range(5):
            self.matrix[i + k][j - 2].naitre()
            self.matrix[i + k][j - 2].basculer()

            self.matrix[i + k][j + 2].naitre()
            self.matrix[i + k][j + 2].basculer()

        self.winfo_toplevel().currentIter.set("0")
        self.winfo_toplevel().nIteration.set("50")

    def pentadecathlon(self):
        """initialise la grille pour simuler le pentadecathlon qui oscille avec une période de 15"""
        self.remplir_alea(0)
        i = self.nbLignes // 2 - 1
        j = self.nbColonnes // 2 - 1

        self.matrix[i][j].naitre()
        self.matrix[i][j].basculer()

        for k in range(1, 5):
            self.matrix[i][j - k].naitre()
            self.matrix[i][j - k].basculer()

        for k in range(1, 6):
            self.matrix[i][j + k].naitre()
            self.matrix[i][j + k].basculer()

        self.winfo_toplevel().currentIter.set("0")
        self.winfo_toplevel().nIteration.set("45")

    def vaisseau_spatial(self):
        """initialise la grille pour simuler le vaisseau spatial capable de se déplacer"""
        self.remplir_alea(0)
        i = self.nbLignes // 2 - 1
        j = 2

        self.matrix[i + 1][j].naitre()
        self.matrix[i + 1][j].basculer()

        self.matrix[i + 3][j].naitre()
        self.matrix[i + 3][j].basculer()

        self.matrix[i][j + 1].naitre()
        self.matrix[i][j + 1].basculer()

        self.matrix[i][j + 2].naitre()
        self.matrix[i][j + 2].basculer()

        self.matrix[i + 4][j + 2].naitre()
        self.matrix[i + 4][j + 2].basculer()

        self.matrix[i][j + 3].naitre()
        self.matrix[i][j + 3].basculer()

        self.matrix[i + 4][j + 3].naitre()
        self.matrix[i + 4][j + 3].basculer()

        self.matrix[i][j + 4].naitre()
        self.matrix[i][j + 4].basculer()

        self.matrix[i][j + 5].naitre()
        self.matrix[i][j + 5].basculer()

        self.matrix[i + 3][j + 5].naitre()
        self.matrix[i + 3][j + 5].basculer()

        self.matrix[i][j + 6].naitre()
        self.matrix[i][j + 6].basculer()

        self.matrix[i + 1][j + 6].naitre()
        self.matrix[i + 1][j + 6].basculer()

        self.matrix[i + 2][j + 6].naitre()
        self.matrix[i + 2][j + 6].basculer()

        self.winfo_toplevel().currentIter.set("0")
        self.winfo_toplevel().nIteration.set("60")


if __name__ == "__main__":

    maGrille = GrilleFrame(master=None, nbLignes=15, nbColonnes=10)

    # test d'accès au attributs
    assert maGrille.nbLignes == 15
    assert maGrille.nbColonnes == 10
    assert maGrille.get_nbLignes() == 15
    assert maGrille.get_nbColonnes() == 10

    # test de la méthode dans_grille()
    assert maGrille.dans_grille(0, 0) == True
    assert maGrille.dans_grille(15, 10) == False
    assert maGrille.dans_grille(8, 8) == True

    # test de la méthode est_voisin()
    assert maGrille.est_voisin(1, 2, 3, 3) == False
    assert maGrille.est_voisin(8, 8, 8, 7) == True
    assert maGrille.est_voisin(5, 5, 5, 5) == False

    # test de la méthode get_voisins()
    assert len(maGrille.get_voisins(0, 0)) == 3
    assert len(maGrille.get_voisins(0, 1)) == 5
    assert len(maGrille.get_voisins(1, 0)) == 5
    assert len(maGrille.get_voisins(1, 1)) == 8

    # tests des méthodes remplir_alea() et d'affichage
    for k in [0, 50, 100]:
        maGrille.remplir_alea(k)
        print(maGrille)
