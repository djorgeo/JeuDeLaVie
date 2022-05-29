# Jeu de la Vie
Ce projet a été réalisé en groupe dans le cadre de l’unité d’enseignement 
intitulée Projet mathématique-informatique de l’université d’Aix-Marseille.

## Auteurs
* Joffrey COTTIN 
* Clarine AZINMEDEM
* Christophe RAVIER

## Roadmap
Le planning qui que nous avons suivi au cours de la réalisation de ce projet
est contenu dans le répertoire [rapport/planning/Projet_DUCCIE_v2.gan](rapport/planning/Projet_DUCCIE_v2.gan)

## Code:
Le répertoire ```code/``` contient les fichiers python du projet
le fichier [```jeuVie_Terminal.py```](code/jeuVie_Terminal.py) permet de tester le fonctionnement de la grille en mode console.  
Il génère une grille aléatoire et calcule les évolutions successives (interrompre par ```Ctrl-C```).

Le fichier [```jeuVie_GUI.py```](code/jeuVie_GUI.py) est le fichier à démarrer pour exécuter le projet en mode graphique.

* Commande python pour lancer la version non graphique: ```python3 jeuVie_Terminal.py```
* Commande python pour lancer la version graphique: ```python3 jeuVie_GUI.py```

**Mode d'emploi rapide :**

* On peut à tout moment modifier directement l'état d'une cellule de la grille en cliquant dessus.
* La partie "initialisation aléatoire" permet de définir un pourcentage et d'initialiser une grille aléatoire contenant en moyenne ce pourcentage de cellules vivantes. Un clic sur "réinitialiser" vide la grille et remet le taux à 0%
* La partie "structures connues" permet de choisir parmi une liste d'exemple et d'initialiser la grille avec une configuration exemplaire du jeu de la vie.
* La partie "nombre d'itérations" permet de définir combien de générations vont être calculées et afficher par un clic sur le bouton "GO", mais aussi de modifier le type de la grille (entre plane et torique)

## Documentation
Le rapport en format pdf de ce projet est accessible à l'adresse [rapport/rapport_projet_jeu_de_la_vie.pdf](rapport/rapport_projet_jeu_de_la_vie.pdf).

Tandis que La documentation technique en format `html` est accessible à l'adresse [rapport/doc_technique/html/index.html](rapport/doc_technique/html/index.html).


## Arborescence
```
.
├── code
│   ├── bibli_exemples.py
│   ├── celluleFrame.py
│   ├── cellule.py
│   ├── grilleFrame.py
│   ├── grille.py
│   ├── jeuVie_GUI.py
│   ├── jeuVie_Terminal.py
├── rapport
│   ├── biblio.bib
│   ├── doc_technique
│   │   └── sphinx
│   │   └── html
│   │       ├── jeuVie_GUI.html
│   │       ├── bibli_exemples.html
│   │       ├── celluleFrame.html
│   │       ├── cellule.html
│   │       ├── genindex.html
│   │       ├── grilleFrame.html
│   │       ├── grille.html
│   │       ├── index.html
│   │       ├── jeuVie_Terminal.html
│   │       ├── _modules
│   │       │   ├── jeuVie_GUI.html
│   │       │   ├── bibli_exemples.html
│   │       │   ├── celluleFrame.html
│   │       │   ├── cellule.html
│   │       │   ├── grilleFrame.html
│   │       │   ├── grille.html
│   │       │   ├── index.html
│   │       │   └── jeuVie_Terminal.html
│   │       ├── modules.html
│   │       ├── objects.inv
│   │       ├── py-modindex.html
│   │       ├── search.html
│   │       ├── searchindex.js
│   │       ├── _sources
│   │       │   ├── jeuVie_GUI.rst.txt
│   │       │   ├── bibli_exemples.rst.txt
│   │       │   ├── celluleFrame.rst.txt
│   │       │   ├── cellule.rst.txt
│   │       │   ├── grilleFrame.rst.txt
│   │       │   ├── grille.rst.txt
│   │       │   ├── index.rst.txt
│   │       │   ├── jeuVie_Terminal.rst.txt
│   │       │   └── modules.rst.txt
│   │       └── _static
│   │           ├── base-stemmer.js
│   │           ├── basic.css
│   │           ├── css
│   │           │   ├── badge_only.css
│   │           │   ├── fonts
│   │           │   │   ├── fontawesome-webfont.eot
│   │           │   │   ├── fontawesome-webfont.svg
│   │           │   │   ├── fontawesome-webfont.ttf
│   │           │   │   ├── fontawesome-webfont.woff
│   │           │   │   ├── fontawesome-webfont.woff2
│   │           │   │   ├── lato-bold-italic.woff
│   │           │   │   ├── lato-bold-italic.woff2
│   │           │   │   ├── lato-bold.woff
│   │           │   │   ├── lato-bold.woff2
│   │           │   │   ├── lato-normal-italic.woff
│   │           │   │   ├── lato-normal-italic.woff2
│   │           │   │   ├── lato-normal.woff
│   │           │   │   ├── lato-normal.woff2
│   │           │   │   ├── Roboto-Slab-Bold.woff
│   │           │   │   ├── Roboto-Slab-Bold.woff2
│   │           │   │   ├── Roboto-Slab-Regular.woff
│   │           │   │   └── Roboto-Slab-Regular.woff2
│   │           │   └── theme.css
│   │           ├── doctools.js
│   │           ├── documentation_options.js
│   │           ├── file.png
│   │           ├── french-stemmer.js
│   │           ├── jquery-3.5.1.js
│   │           ├── jquery.js
│   │           ├── js
│   │           │   ├── badge_only.js
│   │           │   ├── html5shiv.min.js
│   │           │   ├── html5shiv-printshiv.min.js
│   │           │   └── theme.js
│   │           ├── language_data.js
│   │           ├── minus.png
│   │           ├── plus.png
│   │           ├── pygments.css
│   │           ├── searchtools.js
│   │           ├── translations.js
│   │           ├── underscore-1.13.1.js
│   │           └── underscore.js
│   ├── images
│   │   ├── evolution.tex
│   │   ├── jdv_exemple.png
│   │   ├── roadmap.png
│   │   └── voisinage_Moore.tex
│   ├── planning
│   │   ├── Projet_DUCCIE.gan
│   │   ├── Projet_DUCCIE_v2.gan
│   ├── rapport_projet_jeu_de_la_vie.pdf
│   └── rapport_projet_jeu_de_la_vie.tex
└── README.md

14 directories, 90 files
```
