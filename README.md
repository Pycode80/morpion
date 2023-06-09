# Le jeu du Morpion
## Brève présentation 
Ce morpion est codé en Python. Il intègre une fonctionalité de pseudo "intelligence artificelle". 
En effet, vous pouvez jouer en solo (contre la fameuse IA) ou en duo.
L'IA va d'abord voir si elle peut gagner, puis essayer de vous contrer, ensuite essayer de jouer
de manière intelligente puis si cela n'est pas possible, elle va faire un coup au hasard.

## Fonctionalités intéressentes

1. Présence d'une IA
2. J'utilise le module Rich afin de mettre le jeu en graphique mais dans la console

## Fonctionnalités à venir 

- [ ] Une implémentation pour Linux/MacOS car j'efface la console avec la commande cls. <br>
- [ ] Des répliques sympa quand l'IA ou le joueur Gagne.<br>
- [ ] Éventuellement une petite musique de fond.<br>
- [ ] Améliorer l'algorithme de l'IA pour la rendre plus difficile à battre<br>
- [ ] Créer une animation encore plus sympa quand l'IA "réfléchit"<br>

## Installation

1. Avec git :<br>
```
git clone https://github.com/Pycode80/morpion.git
cd morpion
pip install -r requirements.txt
python tic_tac_toe.py
```

2. A la dure:
    - Téléchargez le repo https://github.com/Pycode80/morpion/archive/refs/heads/master.zip et décompresser le.
    - Rendez vous dans le dossier décompréssé
    - Exécutez ces commandes :
        ```
        pip install -r requirements.txt
        python tic_tac_toe.py
        ```

*Ma version de Python est 3.11.3*

## Compilation

Commande pour compiler le projet avec `pyinstaller==5.11.0`

`pyinstaller --onefile --hidden-import=random --hidden-import=os --hidden-import=rich.console --hidden-import=rich.table --hidden-import=rich.prompt tic_tac_toe.py`

*Il est également possible d'effectuer la commande suivante : `pyinstaller tic_tac_toe.spec`*

## Release

Rendez-vous dans la section release : https://github.com/Pycode80/morpion/releases

## Images de production 

![Image1](images/image1.png)
![Image2](images/image2.png)






