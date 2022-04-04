#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:47:52 2021

@author: jcottin
"""

import tkinter as tk
from grille import Grille



class Application(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.create_widgets()
        
    def create_widgets(self):
        
        # zone graphque
        self.canvas = tk.Canvas(self, 
                                width = 800, 
                                height = 600, 
                                background = "white")
        self.canvas.pack(padx = 5, 
                         pady = 5)
        for i in range(1, 30):
            self.canvas.create_line(0, 20*i, 800, 20*i, width=2)
        for j in range(0, 40):
            self.canvas.create_line(20*j, 0, 20*j, 600, width=2)
        
        # bouton 'Lancer'
        self.button = tk.Button(self, 
                                text = "Lancer",
                                command = self.excecute)
        self.button.pack(padx = 5, 
                         pady = 5)
        
    def excecute(self):
        vie = Grille(30, 40)
        vie.remplir_alea(10)
        vie.affecte_voisins()
        for ligne in range(len(vie.matrix)) :
            for colonne in range(len(vie.matrix[0])):
                cell = vie.matrix[ligne][colonne]
                if cell.actuel == True:
                    self.canvas.create_rectangle(20*ligne, 20*colonne,
                                                 20*ligne+20, 20*colonne+20,fill="red")
        
        
    
    def action_clic_souris(self, event):
        self.canvas.focus_set()
        x = event.x
        y = event.y
        self.canvas.create_rectangle(x,y,x+10,y+10,fill="red")
        print("Clic à x =",x,", y =",y)
        return
    
        
    

if __name__ == "__main__":
    app = Application()
    app.title("Test")        
    #app.geometry("445x160")
    #app.bind('<Escape>', app.remiseaZero)
    #app.bind("<Button-1>", app.action_clic_souris)
    app.mainloop()