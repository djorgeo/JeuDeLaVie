from grille import Grille
import time

def efface_ecran():
    """ permet d'effacer l'écran dans un terminal ANSI """
    print("\u001B[H\u001B[J")
    
def main():
    vie = Grille(10,15)
    vie.remplir_alea(50)
    vie.affecte_voisins()
    while True:
        efface_ecran()
        print(vie)
        print("\n")
        time.sleep(0.2)
        vie.jeu()
        vie.actualise()

main()