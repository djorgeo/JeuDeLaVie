#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
grille est un module utilisé à la fois par la version graphique et non graphique du jeu.
Ce module contient l'implémentation de la classe Grille qui est l'une des plus des plus
importantes du projet.
"""

from __future__ import annotations
from cellule import Cellule
from typing import List
from random import random


class Grille():
    """
    Cette classe permet d'implémenter la grille sur laquelle se déroule le jeu de la vie 
    qui peut être plane ou torique.
    nbLignes: il s'agit du nombre de lignes de la grille.
    nbColonnes: représente le nombre de colonnes de la grille.
    typeg: c'est le type de grille (plane ou torique).
    """

    VOISINAGE = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    """Liste utilisée pour le calcul des voisins d'une cellule"""

    def __init__(self: Grille, nbLignes: int, nbColonnes: int, typeg: str) -> None:
        """ Constructeur de la classe Grille """
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes
        self.matrix = [[Cellule() for j in range(self.nbColonnes)] for i in range(self.nbLignes)]
        self.type_grille = typeg

    def dans_grille(self: Grille, i: int, j: int) -> bool:
        """ Méthode qui permet de vérifier si le point de coordonnées (i, j) fait partie la grille.
         Elle retourne True si le point (i, j) est dans la grille et False sinon. """
        return 0 <= i < self.nbLignes and 0 <= j < self.nbColonnes

    def setXY(self: Grille, i: int, j: int, cellule: Cellule) -> None:
        """ Méthode qui permet d'insérer une cellule dans la case (i, j) de la grille.
         le paramètre "cellule" représente la cellule à insérer dans la case (i, j) de la grille."""
        if self.dans_grille(i, j):
            self.matrix[i][j] = cellule
        else:
            raise IndexError(str(i, j))

    def getXY(self: Grille, i: int, j: int) -> Cellule:
        """ Méthode qui renvoie la cellule située dans la case (i, j) de la grille. """
        if self.dans_grille(i, j):
            return self.matrix[i][j]
        else:
            return None

    def get_nbColonnes(self: Grille) -> int:
        """ Méthode qui renvoie le nombre de colonnes de la grille. """
        return self.nbColonnes

    def get_nbLignes(self: Grille) -> int:
        """ Méthode qui renvoie le nombre de lignes de la grille. """
        return self.nbLignes

    def get_type_grille(self: Grille) -> str:
        """ Méthode qui renvoie le type de la grille (plane ou torique). """
        return self.type_grille

    def set_type_grille(self: Grille, typeg: str) -> None:
        """ Méthode qui permet de modifier le type de la grille.
        Le paramètre "typeg" est la chaine de caractère (plane ou torique)
        à utiliser pour mettre à jour le type de la grille. """
        self.type_grille = typeg

    def get_voisins(self: Grille, x: int, y: int) -> List[Cellule]:
        """ Méthode qui renvoie la liste des voisins d’une cellule. """
        voisins = []
        if self.get_type_grille() == 'plane':
            for (i, j) in self.VOISINAGE:
                if self.dans_grille(x + i, y + j):
                    voisins.append(self.getXY(x + i, y + j))
        else:  # cas où la grille est torique
            nbColonnes, nbLignes = self.get_nbColonnes(), self.get_nbLignes()
            for (i, j) in self.VOISINAGE:
                voisins.append(self.getXY((x + i) % nbLignes, (y + j) % nbColonnes))
        return voisins

    def affecte_voisins(self: Grille) -> None:
        """ Méthode qui permet d'affecter à chaque cellule de la grille la liste de ses voisins. """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.set_voisins(self.get_voisins(i, j))

    def __str__(self: Grille) -> str:
        """ Méthode spéciale pour afficher la grille sous forme d'une chaîne de caractères. """
        chaine = ""
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                chaine += str(self.getXY(i, j))
            chaine += "\n"
        return chaine

    def remplir_alea(self, taux: int):
        """ Méthode qui permet de remplir aléatoirement la Grille avec un certain taux de cellules vivantes.
         Le paramètre "taux" représente le pourcentage de cellules vivantes à créer sur la grille. """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                if random() <= (taux / 100):
                    cellule = self.getXY(i, j)
                    cellule.naitre()
                    cellule.basculer()

    def jeu(self: Grille) -> None:
        """ Méthode qui passe en revue toutes les cellules de la grille et calcule leur état futur. """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.calcule_etat_futur()

    def actualise(self: Grille) -> None:
        """ Méthode qui permet de basculer toutes les cellules de la grille dans leur état futur. """
        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                cellule = self.getXY(i, j)
                cellule.basculer()


if __name__ == "__main__":

    maGrille = Grille(15, 10, 'plane')

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

    # tests des méthodes remplir_alea() et d'affichage
    for k in [0, 50, 100]:
        maGrille.remplir_alea(k)
        print(maGrille)

    # test des méthodes affecte_voisins(), jeu() et actualise()
    maGrille = Grille(15, 10, 'plane')
    maGrille.remplir_alea(15)
    print(maGrille)
    maGrille.affecte_voisins()
    cell93 = maGrille.getXY(9, 3)
    cell02 = maGrille.getXY(0, 2)
    print(cell93, cell02)
    assert len(cell93.get_voisins()) == 8
    assert len(cell02.get_voisins()) == 5
    maGrille.jeu()
    maGrille.actualise()
    print(maGrille)

    # répétition des tests avec une grille torique
    maGrille2 = Grille(15, 10, 'torique')

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

    # tests des méthodes remplir_alea() et d'affichage
    for k in [0, 50, 100]:
        maGrille2.remplir_alea(k)
        print(maGrille2)

    # test des méthodes affecte_voisins(), jeu() et actualise()
    maGrille2 = Grille(15, 10, 'torique')
    maGrille2.remplir_alea(15)
    print(maGrille2)
    maGrille2.affecte_voisins()
    cell93 = maGrille2.getXY(9, 3)
    cell02 = maGrille2.getXY(0, 2)
    print(cell93, cell02)
    assert len(cell93.get_voisins()) == 8
    assert len(cell02.get_voisins()) == 8
    maGrille2.jeu()
    maGrille2.actualise()
    print(maGrille2)
