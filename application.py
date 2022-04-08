#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 22:47:52 2021

@author: jcottin
"""

import tkinter as tk
from grille import Grille

class Application(tk.Tk):
    
    def __init__(self, width, height, cote=20):
        tk.Tk.__init__(self)
        self.width = width 
        self.height = height
        self.cote = cote
        self.create_widgets()
    
    def create_widgets(self):
        # zone graphque
        self.canvas = tk.Canvas(self, 
                                width = self.width, 
                                height = self.height, 
                                background = "white")
        self.canvas.pack(padx = 5, 
                         pady = 5)
        for i in range(0, self.height//self.cote):
            self.canvas.create_line(0, self.cote*i, self.width, self.cote*i, width=1)
        for j in range(0, self.width//self.cote):
            self.canvas.create_line(self.cote*j, 0, self.cote*j, self.height, width=1)        
        # bouton 'Lancer'
        self.button = tk.Button(self, 
                                text = "Lancer",
                                command = self.excecute)
        self.button.pack(padx = 5, 
                         pady = 5)
        
    def excecute(self):
        vie = Grille(self.width//self.cote, self.height//self.cote)
        vie.remplir_alea(10)
        vie.affecte_voisins()
        
        for ligne in range(len(vie.matrix)) :
            for colonne in range(len(vie.matrix[0])):
                cell = vie.matrix[ligne][colonne]
                if cell.actuel == True:
                    self.canvas.create_rectangle(self.cote*ligne, self.cote*colonne,
                                                 self.cote*ligne+self.cote, self.cote*colonne+self.cote,fill="red")
        
        
    """
    def action_clic_souris(self, event):
        self.canvas.focus_set()
        x = event.x
        y = event.y
        self.canvas.create_rectangle(x,y,x+10,y+10,fill="red")
        print("Clic à x =",x,", y =",y)
        return
    """
        
    

if __name__ == "__main__":
    app = Application(800, 600,10)
    app.title("Test")        
    #app.geometry("445x160")
    #app.bind('<Escape>', app.remiseaZero)
    #app.bind("<Button-1>", app.action_clic_souris)
    app.mainloop()