#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
jeuVie_GUI est le module principal de la version graphique du projet.
C'est dans ce module que la fenêtre principale du jeu est créée à l'aide de librairie tkinter.
Il s'agit en effet du point de départ du projet.
"""

import tkinter as tk
from tkinter import ttk
from grilleFrame import GrilleFrame
import time
from bibli_exemples import *


class App(tk.Tk):
    """
    Classe principale du projet qui se charge de créer les différents composants graphiques.
    C'est également la fenêtre principale du jeu.
    minWidth: largeur minimum en pixels de la fenêtre.
    minHeight: hauteur minimum en pixels de la fenêtre.
    """

    NBLIGNES = 30
    """attribut de classe qui indique le nombre de lignes de la grille."""
    NBCOLONNES = 50
    """attribut de classe qui indique le nombre de colonnes de la grille."""

    def __init__(self, minWidth: int, minHeight: int, title: str) -> None:
        """Constructeur de la classe App"""
        tk.Tk.__init__(self)
        self.minsize(width=minWidth, height=minHeight)
        self.title(title)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Styles
        self.style = ttk.Style()
        self.style.configure("RootFrame.TFrame", background="white")
        self.style.configure("ConfigFrame.TFrame", background="white")
        self.style.configure("Config.TLabelframe", background="white", padding=(5, 5, 5, 5))
        self.style.configure("config.TSpinbox", background="white")
        self.style.configure("config.TButton", background="white", font=("MV Boli", 11))
        self.style.configure("config.TEntry", background="white")
        self.style.configure("config.TLabel", background="white", font=("Corbel", 12))
        self.style.configure("config.TMenubutton", background="white", font=("Corbel", 12))
        self.style.configure("frameTitle.TLabel", background="white", font=("Corbel", 11, "bold", "italic"))
        self.style.configure("counter.TLabel", background="white", anchor="center", font=("Bahnschrift Light", 25),
                             foreground="#F32424", width="8")
        self.style.configure("counter.TFrame", background="white")

        # Creation du Frame principal
        self.rootFrame = ttk.Frame(self, style="RootFrame.TFrame", padding=(10, 2, 10, 2))
        self.rootFrame.grid(column=0, row=0, sticky="NSEW")
        self.rootFrame.grid_rowconfigure(0, weight=99)
        self.rootFrame.grid_rowconfigure(1, weight=1)
        self.rootFrame.grid_columnconfigure(0, weight=1)

        # Creation de la grille du jeu
        self.gridFrame = GrilleFrame(master=self.rootFrame, nbLignes=self.NBLIGNES, nbColonnes=self.NBCOLONNES,
                                     typeg='plane')
        self.gridFrame.grid(column=0, row=0, sticky="NSEW")

        # Création d'un Frame de configuration
        self.configFrame = ttk.Frame(self.rootFrame, style="ConfigFrame.TFrame")
        self.configFrame.grid(column=0, row=1, sticky="NSEW")
        self.configFrame.grid_columnconfigure(0, weight=30)
        self.configFrame.grid_columnconfigure(1, weight=30)
        self.configFrame.grid_columnconfigure(2, weight=30)
        self.configFrame.grid_columnconfigure(3, weight=10)

        # Création des widgets pour la génération aléatoire
        # d'une configuration de départ
        self.aleaFrameTitle = ttk.Label(self.configFrame, text="Initialisation aléatoire",
                                        style="frameTitle.TLabel")
        self.aleaFrame = ttk.LabelFrame(self.configFrame, labelwidget=self.aleaFrameTitle,
                                        style="Config.TLabelframe", labelanchor="nw")
        self.aleaFrame.grid(row=0, column=0, sticky="NSEW", padx=10, pady=20)
        self.aleaRate = tk.StringVar()
        self.aleaRate.set("Taux: 0%")
        self.aleaRateSpinbox = ttk.Spinbox(self.aleaFrame, values=["Taux: " + str(i) + "%" for i in range(101)],
                                           textvariable=self.aleaRate, state="readonly", width=9,
                                           style="config.TSpinbox", font=("Bahnschrift Light", 12))
        self.aleaRateSpinbox.grid(column=0, row=0, sticky="NSEW", padx=2, pady=2)
        self.aleaButton = ttk.Button(self.aleaFrame, text="Initialiser", command=self.alea_init_config,
                                     style="config.TButton")
        self.aleaButton.grid(column=1, row=0, sticky="NSEW", padx=2, pady=2)
        self.resetButton = ttk.Button(self.aleaFrame, text="Réinitialiser", command=self.reset_grid,
                                      style="config.TButton")
        self.resetButton.grid(column=1, row=1, sticky="NSEW", padx=2, pady=2)

        # Creation des widgets pour répliquer des structures connues
        self.knownStructsFrameTitle = ttk.Label(self.configFrame, text="Structures connues", style="frameTitle.TLabel")
        self.knownStructsFrame = ttk.LabelFrame(self.configFrame, labelwidget=self.knownStructsFrameTitle,
                                                style="Config.TLabelframe", labelanchor="nw")
        self.knownStructsFrame.grid(row=0, column=1, sticky="NSEW", padx=10, pady=20)
        options = ["Clignotant", "Ruche 1", "Ruche 2", "Balise", "Crapeau", "Escalier", "Pulsar", "Pentadecathlon",
                   "Vaisseau spatial"]
        self.knownStructure = tk.StringVar()
        self.knownStructure.set(options[0])
        self.knownStructsMenu = ttk.OptionMenu(self.knownStructsFrame, self.knownStructure, options[0],
                                               *options, direction="above", style="config.TMenubutton")
        self.knownStructsMenu.grid(row=0, column=0)
        self.knownStructsButton = ttk.Button(self.knownStructsFrame, text="Initialiser", command=self.init_known_struct,
                                             style="config.TButton")
        self.knownStructsButton.grid(column=0, row=1, sticky="NSEW", padx=2, pady=2)

        # Création des widgets pour l'exécution du jeu
        self.runFrameTitle = ttk.Label(self.configFrame, text="Exécution du jeu", style="frameTitle.TLabel")
        self.runFrame = ttk.LabelFrame(self.configFrame, labelwidget=self.runFrameTitle,
                                       style="Config.TLabelframe", labelanchor="nw")
        self.runFrame.grid(row=0, column=2, sticky="NSEW", padx=10, pady=20)
        self.nIterationLabel = ttk.Label(self.runFrame, text="Nombre d'itérations: ", style="config.TLabel")
        self.nIterationLabel.grid(column=0, row=0, sticky="NSEW", padx=2, pady=2)
        self.nIteration = tk.StringVar()
        self.nIteration.set("1")
        digit_validation = self.register(self.validate_numeric_entry)
        self.nIterationEntry = ttk.Entry(self.runFrame,
                                         textvariable=self.nIteration, width=7,
                                         style="config.TEntry", font=("Bahnschrift Light", 12),
                                         validate="key",
                                         validatecommand=(digit_validation, '%P'))
        self.nIterationEntry.grid(column=1, row=0, sticky="NSEW", padx=2, pady=2)
        gridTypes = ["Grille plane", "Grille torique"]
        self.gridType = tk.StringVar()
        self.gridType.set(gridTypes[0])
        self.gridTypeMenu = ttk.OptionMenu(self.runFrame, self.gridType, gridTypes[0],
                                           *gridTypes, direction="above", style="config.TMenubutton",
                                           command=self.update_grid_type)
        self.gridTypeMenu.grid(row=1, column=1)
        self.runIterButton = ttk.Button(self.runFrame, text="Go", command=self.play_niter,
                                        style="config.TButton")
        self.runIterButton.grid(column=1, row=2, sticky="NSEW", padx=2, pady=2)

        # Creation des widgets pour le suivi du nombre d'itérations
        self.iterFrame = ttk.Frame(self.configFrame, style="counter.TFrame")
        self.iterFrame.grid(row=0, column=3, sticky="NSEW", padx=10, pady=20)
        self.iterFrame.grid_rowconfigure(0, weight=1)
        self.iterFrame.grid_columnconfigure(0, weight=1)
        self.currentIter = tk.StringVar()
        self.currentIter.set("0")
        self.counterLabel = ttk.Label(self.iterFrame, textvariable=self.currentIter, style="counter.TLabel")
        self.counterLabel.grid(row=0, column=0, sticky="NSEW")

    def get_alea_rate(self):
        """Méthode qui permet de récupérer la proportion initiale de cellules vivantes entrée par l'utilisateur."""
        return int(self.aleaRate.get().replace("%", "").replace("Taux: ", ""))

    def alea_init_config(self):
        """Méthode qui permet d'initialiser de façon aléatoire la grille avec un taux de cellules vivantes fourni par
        l'utilisateur. Cette méthode est appelée après un click de l'utilisateur sur le bouton Initialiser."""
        self.gridFrame.remplir_alea(self.get_alea_rate())
        self.currentIter.set("0")

    def reset_grid(self):
        """Méthode qui permet de réinitialiser la grille, c'est-à-dire la remettre à son état initial avec toutes les
        cellules mortes. Cette méthode est appelée après un click de l'utilisateur sur le bouton Réinitialiser."""
        self.gridFrame.remplir_alea(0)
        self.currentIter.set("0")
        self.aleaRate.set("Taux: 0%")

    @staticmethod
    def validate_numeric_entry(user_input):
        """Méthode de classe qui permet d'effectuer la validation d'un champ de texte numérique,
        c'est-à-dire faire en sorte que ce champ de texte n'accepte que des valeurs numériques"""
        if user_input.isdigit() or user_input == "":
            return True
        return False

    def init_known_struct(self):
        """Méthode qui permet d'initialiser la grille avec la configuration initiale d'une structure connue
        (Clignotant, Ruche 1, Ruche 2, Balise, Crapeau, Escalier, Pulsar, Pentadecathlon ou Vaisseau spatial)"""
        test = self.knownStructure.get()
        if test == "Clignotant":
            clignotant(self.gridFrame)
        elif test == "Ruche 1":
            ruche1(self.gridFrame)
        elif test == "Ruche 2":
            ruche2(self.gridFrame)
        elif test == "Balise":
            balise(self.gridFrame)
        elif test == "Crapeau":
            crapeau(self.gridFrame)
        elif test == "Escalier":
            escalier(self.gridFrame)
        elif test == "Pulsar":
            pulsar(self.gridFrame)
        elif test == "Pentadecathlon":
            pentadecathlon(self.gridFrame)
        elif test == "Vaisseau spatial":
            vaisseau_spatial(self.gridFrame)

    def play_niter(self):
        """Méthode qui utilise les règles du jeu de la vie pour mettre la grille à jour de façon itérative
        pendant un nombre d'itérations fourni par l'utilisateur"""
        if self.nIteration.get() != "":
            for i in range(int(self.nIteration.get())):
                self.currentIter.set(str(int(self.currentIter.get()) + 1))
                self.gridFrame.jeu()
                self.gridFrame.actualise()
                self.update_idletasks()
                self.update()
                time.sleep(0.05)

    def update_grid_type(self, event):
        """Méthode qui permet de changer le type de grille (plane ou torique) à utiliser
        et de recalculer les voisins de chaque cellule en conséquence"""
        self.gridFrame.set_type_grille(self.gridType.get()[7:])  # le slicing supprime le mot "Grille"
        # Changer le type de grille change les voisinages des cases du bord.
        # En appelant la méthode affecte_voisins(), on va modifier la liste des voisins des cellules.
        self.gridFrame.affecte_voisins()


if __name__ == "__main__":
    app = App(minWidth=920, minHeight=676, title="Jeu de la vie")
    app.mainloop()

# Tests utilisateurs des différentes interactions effectuées.
# En particulier il a bien été vérifié que le passage
# d'une grille torique à plane fonctionnait correctement dans les deux sens.
