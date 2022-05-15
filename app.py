#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from grilleFrame import GrilleFrame
import time


class App(tk.Tk):
    """Classe principale du projet qui se charge de créer les différents composants graphiques"""

    def __init__(self, minWidth, minHeight, title):
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
        self.gridFrame = GrilleFrame(master=self.rootFrame, nbLignes=25, nbColonnes=45)
        self.gridFrame.grid(column=0, row=0, sticky="NSEW")

        # Création d'un Frame de configuration
        self.configFrame = ttk.Frame(self.rootFrame, style="ConfigFrame.TFrame")
        self.configFrame.grid(column=0, row=1, sticky="NSEW")
        self.configFrame.grid_columnconfigure(0, weight=30)
        self.configFrame.grid_columnconfigure(1, weight=30)
        self.configFrame.grid_columnconfigure(2, weight=30)
        self.configFrame.grid_columnconfigure(3, weight=10)

        # Création des widgets pour lacgénération aléatoire
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
        options = ["Clignotant", "Ruche 1", "Ruche 2", "Balise", "Crapeau", "Escalier", "Pulsard", "Pentadecathlon",
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
        """méthode qui retourne la proportion initiale de cellules vivantes"""
        return int(self.aleaRate.get().replace("%", "").replace("Taux: ", ""))

    def alea_init_config(self):
        """méthode a déclancher après un clic sur le Initialiser pour initialiser
        la grille"""
        self.gridFrame.remplir_alea(self.get_alea_rate())
        self.currentIter.set("0")

    def reset_grid(self):
        """méthode a déclancher après un clic sur le boutton Réinitialiser pour
        remettre la grille à son etat initial"""
        self.gridFrame.remplir_alea(0)
        self.currentIter.set("0")
        self.aleaRate.set("Taux: 0%")

    def play_niter(self):
        """Méthode pour mettre à jour la grille du jeu pendant un nombre d'itérations donné"""
        if self.nIteration.get() != "":
            for i in range(int(self.nIteration.get())):
                self.currentIter.set(str(int(self.currentIter.get()) + 1))
                self.gridFrame.jeu()
                self.gridFrame.actualise()
                self.update_idletasks()
                self.update()
                time.sleep(0.05)

    @staticmethod
    def validate_numeric_entry(user_input):
        """méthode de validation d'un champ de texte numérique"""
        if user_input.isdigit() or user_input == "":
            return True
        return False

    def init_known_struct(self):
        """méthode pour initialiser le jeu avec une configuration connue (clignotant, ruche, etc.)"""
        match self.knownStructure.get():
            case "Clignotant":
                self.gridFrame.clignotant()
            case "Ruche 1":
                self.gridFrame.ruche1()
            case "Ruche 2":
                self.gridFrame.ruche2()
            case "Balise":
                self.gridFrame.balise()
            case "Crapeau":
                self.gridFrame.crapeau()
            case "Escalier":
                self.gridFrame.escalier()
            case "Pulsard":
                self.gridFrame.pulsard()
            case "Pentadecathlon":
                self.gridFrame.pentadecathlon()
            case "Vaisseau spatial":
                self.gridFrame.vaisseau_spatial()

    def update_grid_type(self, event):
        """méthode pour changer le type de grille et réaffceter les voisins en coséquence"""
        self.gridFrame.gridType = self.gridType.get()
        self.gridFrame.affecte_voisins()
        print(self.gridFrame.est_voisin(1, 0, 0, 44))


if __name__ == "__main__":
    app = App(minWidth=920, minHeight=676, title="Jeu de la vie")
    app.mainloop()
