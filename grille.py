#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:47:52 2021

@author: jcottin
"""

from __future__ import annotations
from cellule import Cellule
from typing import List
from random import random


class Grille():
    """ classe Grille pour les cellules du le Jeu de la vie """
    def __init__(self: Grille, nbLignes: int, nbColonnes: int) -> None:
        """ Constructeur de la classe Grille """
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes        
        self.matrix = [[Cellule() for j in range(self.nbColonnes)] for i in range(self.nbLignes)]
        
    def dans_grille(self: Grille, i: int, j: int) -> bool:
        """ teste si le point de coordonnées (i,j) est dans la grille """
        return 0 <= i < self.nbLignes and 0 <= j < self.nbColonnes

    def setXY(self: Grille, i: int, j: int, cellule: Cellule) -> None:
        """ affecte une nouvelle cellule à la case (i, j) de la grille """
        if self.dans_grille(i, j):
            self.matrix[i][j] = cellule
        else:
            raise IndexError(str(i, j))

    def getXY(self: Grille, i: int, j: int) -> Cellule:
        """ renvoie la cellule située dans la case (i, j) de la grille """
        if self.dans_grille(i, j):
            return self.matrix[i][j]
        else:
            return None

    def get_nbColonnes(self: Grille) -> int:
        """ renvoie le nombre de colonnes de la grille """
        return self.nbColonnes

    def get_nbLignes(self: Grille) -> int:
        """ renvoie le nombre de lignes de la grille """
        return self.nbLignes

    @staticmethod
    def est_voisin(i: int, j: int, x: int, y: int) -> bool:
        """ teste si les cases (i, j) et (x, y) sont voisines dans la grille """
        return max(abs(x - i), abs(y - j)) == 1        

    def get_voisins(self: Grille, x: int, y: int) -> List[Cellule]:
        """ renvoie la liste des voisins d’une cellule """
        voisins = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.dans_grille(i, j) and Grille.est_voisin(x, y, i, j):
                    voisins.append(self.getXY(i, j))
        return voisins

    def affecte_voisins(self: Grille) -> None:
        """ affecte à chaque cellule de la grille la liste de ses voisins """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.set_voisins(self.get_voisins(i, j))

    def __str__(self: Grille) -> str:
        """ méthode spéciale pour afficher l'objet sous forme d'une chaîne de caractères """
        chaine = ""
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                chaine += str(self.getXY(i, j))
            chaine += "\n"
        return chaine

    def remplir_alea(self, taux: int):
        """ remplit aléatoirement la Grille avec un certain taux de Cellule vivantes """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                if random() <= (taux / 100):
                    cellule = self.getXY(i, j)
                    cellule.naitre()
                    cellule.basculer()
                    #print(cellule)

    def jeu(self: Grille) -> None:
        """ passe en revue toutes les Cellule de la Grille, calcule leur état futur """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.calcule_etat_futur()

    def actualise(self: Grille) -> None:
        """ bascule toutes les Cellule de la Grille dans leur état futur """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.basculer()

if __name__ == "__main__":

    maGrille = Grille(15, 10)
    
    # test d'accès au attributs
    assert maGrille.nbLignes == 15
    assert maGrille.nbColonnes == 10
    assert maGrille.get_nbLignes() == 15
    assert maGrille.get_nbColonnes() == 10    
    
    # test de la méthode dans_grille()
    assert maGrille.dans_grille(0,0) == True
    assert maGrille.dans_grille(15,10) == False
    assert maGrille.dans_grille(8,8) == True
    
    # test de la méthode est_voisin()
    assert maGrille.est_voisin(1,2,3,3) == False
    assert maGrille.est_voisin(8,8,8,7) == True
    assert maGrille.est_voisin(5,5,5,5) == False
    
    # test de la méthode get_voisins()
    assert len(maGrille.get_voisins(0,0)) == 3
    assert len(maGrille.get_voisins(0,1)) == 5
    assert len(maGrille.get_voisins(1,0)) == 5
    assert len(maGrille.get_voisins(1,1)) == 8
    
    # tests des méthodes remplir_alea() et d'affichage
    for k in [0,50,100]:
        maGrille.remplir_alea(k)
        print(maGrille)
        
