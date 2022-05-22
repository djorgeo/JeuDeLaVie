    
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

def pulsar(self):
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

