### --IMPORT SECTION -- ###
import random
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import time
import os


console = Console()#Initialisation de la console du module rich

def afficher_grille(tab):
    """
    Cette fonction affiche la grille du morpion.

    Args:
        tab (list): La grille du morpion. Une liste de 3 listes, chacune contenant 3 éléments. Chaque élément peut être
        un entier (0, 1 ou 2), ou une chaîne de caractères vide ('') si la case est vide.

    Returns:
        None
    
    """
    # Création d'une nouvelle table
    table = Table()
    # Ajout de la première colonne vide
    table.add_column("", justify="center", width=2)
    # Ajout des colonnes correspondantes à chaque colonne de la grille
    table.add_column("0", justify="center")
    table.add_column("1", justify="center")
    table.add_column("2", justify="center")
    
    # Parcours des lignes de la grille
    for i in range(3):
        # Création d'une nouvelle liste contenant le numéro de la ligne
        row = [str(i)]
        # Parcours des colonnes de la grille
        for j in range(3):
            # Ajout d'une chaîne vide si la case est vide
            if tab[i][j] == 0:
                row.append("")
            # Ajout de la chaîne "[green]X[/green]" si la case contient un "X"
            elif tab[i][j] == 1:
                row.append("[green]X[/green]")
            # Ajout de la chaîne "[red]O[/red]" si la case contient un "O"
            elif tab[i][j] == 2:
                row.append("[red]O[/red]")
        # Ajout de la ligne à la table
        table.add_row(*row)
    
    # Affichage de la table dans la console
    console.print(table)



def tour_ia(tab):
    """Cette fonction joue un coup pour l'IA en fonction de l'état actuel du tableau de jeu.

    Args:
        tab (list): La grille du morpion.

    Returns:
        tuple: Un tuple de booléen et de liste. Le booléen est True si l'IA a réussi à jouer, False sinon. 
            La liste est la grille du morpion mise à jour.
    """
    console.print("[bold red]L'IA réfléchit...[/bold red]", end="")
    for i in range(3):
        time.sleep(0.5)
        console.print("[bold red].[/bold red]", end="")
    console.print()


    # On copie la grille pour pouvoir tester différents coups sans modifier la grille actuelle
    copie_tab = [[tab[i][j] for j in range(3)] for i in range(3)]

    # D'abord, on cherche si l'IA peut gagner au prochain coup
    for i in range(3):
        for j in range(3):
            if copie_tab[i][j] == 0:
                copie_tab[i][j] = 2
                if grille_gagnante(copie_tab) == 2:
                    tab[i][j] = 2
                    return (True, tab)
                else:
                    copie_tab[i][j] = 0

    # Ensuite, on cherche si l'adversaire peut gagner au prochain coup
    for i in range(3):
        for j in range(3):
            if copie_tab[i][j] == 0:
                copie_tab[i][j] = 1
                if grille_gagnante(copie_tab) == 1:
                    tab[i][j] = 2
                    return (True, tab)
                else:
                    copie_tab[i][j] = 0

    # Enfin, si aucun joueur ne peut gagner au prochain tour, l'IA cherche à jouer un coup stratégique
    if copie_tab[1][1] == 0:
        tab[1][1] = 2
        return (True, tab)
    elif copie_tab[0][0] == 1 and copie_tab[2][2] == 0:
        tab[2][2] = 2
        return (True, tab)
    elif copie_tab[0][2] == 1 and copie_tab[2][0] == 0:
        tab[2][0] = 2
        return (True, tab)
    elif copie_tab[2][0] == 1 and copie_tab[0][2] == 0:
        tab[0][2] = 2
        return (True, tab)
    elif copie_tab[2][2] == 1 and copie_tab[0][0] == 0:
        tab[0][0] = 2
        return (True, tab)
    
    else:
            # Si aucun coup stratégique n'est possible, l'IA choisit un coup aléatoire
            coups_possibles = [(i, j) for i in range(3) for j in range(3) if copie_tab[i][j] == 0]#Cette ligne de code crée une liste coups_possibles qui contient toutes les coordonnées (i,j) de la grille où la valeur est égale à 0 (case vide). Cela est réalisé à l'aide d'une liste de compréhension, qui parcourt les indices i et j pour toutes les cases de la grille de morpion et ajoute les coordonnées (i,j) à la liste si la valeur correspondante de la grille est 0 (case vide).
            if coups_possibles:
                coup_aleatoire = random.choice(coups_possibles)
                tab[coup_aleatoire[0]][coup_aleatoire[1]] = 2
                return (True, tab)
            else:
                # Si tous les coups ont été joués, on renvoie False
                return (False, tab)


def joueur_joue(tab, num_joueur, num_ligne, num_colonne):
    """Cette fonction permet à un joueur de jouer dans une case spécifique du tableau.

    Args:
        tab (list): La grille du morpion.
        num_joueur (int): Le numéro du joueur en cours.
        num_ligne (int): Le numéro de la ligne où le joueur veut jouer.
        num_colonne (int): Le numéro de la colonne où le joueur veut jouer.

    Returns:
        tuple: Un tuple de booléen et de liste. Le booléen est True si le joueur a réussi à jouer, False sinon. 
            La liste est la grille du morpion mise à jour.
    """
    if tab[num_ligne][num_colonne] != 0:
        return (False, tab)
    else:
        tab[num_ligne][num_colonne] = num_joueur
        return (True, tab)


def grille_gagnante(tableau):
    """Cette fonction vérifie si un joueur a gagné en parcourant la grille du morpion.

    Args:
        tableau (list): La grille du morpion.

    Returns:
        int: Le numéro du joueur gagnant (1 ou 2), ou 0 s'il n'y a pas de gagnant.
        None : La grille n'admet aucun vainqueur.
    """
    # Vérification des lignes
    for i in range(3):
        if tableau[i][0] == tableau[i][1] == tableau[i][2] and tableau[i][0] != 0:
            return tableau[i][0]

    # Vérification des colonnes
    for i in range(3):
        if tableau[0][i] == tableau[1][i] == tableau[2][i] and tableau[0][i] != 0:
            return tableau[0][i]

    # Vérification de la diagonale principale
    if tableau[0][0] == tableau[1][1] == tableau[2][2] and tableau[0][0] != 0:
        return tableau[0][0]

    # Vérification de la diagonale secondaire
    if tableau[0][2] == tableau[1][1] == tableau[2][0] and tableau[0][2] != 0:
        return tableau[0][2]
    #Verification s'il n'y a pas de possibilité de victoire
    for i in range(3):
        for j in range(3):
            if tableau[i][j] == 0:
                return 0
    return None
    
    


    


def partie_morpion(mode):
    if mode == "duo":
        # Si le mode est "duo", on affiche un message de bienvenue et on initialise le tableau et le tour de jeu
        console.print("Vous avez choisi de jouer en duo. Invitez un ami et amusez-vous bien !", style="green")
        time.sleep(2)
        tab = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        tour = 1
        # On entre dans la boucle principale de jeu
        while True:
            os.system('cls')
            # On affiche la grille de jeu et le joueur qui doit jouer
            afficher_grille(tab)
            if tour == 1:
                console.print("[center]C'est au joueur 1 de jouer (X)[/center]")
            else:
                console.print("[center]C'est au joueur 2 de jouer (O)[/center]")
            console.print("\n\n\n")
            # Le joueur entre les coordonnées de la case qu'il veut jouer
            try:
                ligne = int(input("Entrez le numéro de ligne où vous voulez jouer (0, 1 ou 2) : "))
                colonne = int(input("Entrez le numéro de colonne où vous voulez jouer (0, 1 ou 2) : "))
            except ValueError:
            # Si l'input n'est pas un entier, on affiche un message d'erreur et on continue la boucle
                print("Les coordonnées doivent être des entiers. Essayez à nouveau.")
                time.sleep(2)
                continue
            if not (0 <= ligne <= 2 and 0 <= colonne <= 2):
                # Si les coordonnées ne sont pas valides, on affiche un message d'erreur et on continue la boucle
                print("Les coordonnées doivent être entre 0 et 2. Essayez à nouveau.")
                time.sleep(2)
                continue
            # On vérifie si la case est libre et on met à jour le tableau avec le coup du joueur
            (joue, tab) = joueur_joue(tab, tour, ligne, colonne)
            if not joue:
                # Si la case est déjà occupée, on affiche un message d'erreur et on continue la boucle
                print("La case est déjà occupée. Essayez à nouveau.")
                time.sleep(2)
                continue
            # On vérifie si le joueur a gagné la partie
            gagnant = grille_gagnante(tab)
            if gagnant != 0:
                #Si le joueur a gagné, on affiche un message de victoire et on sort de la boucle
                os.system('cls')
                afficher_grille(tab)
                if gagnant == 1:
                    print("Le joueur 1 (X) a gagné!")
                if gagnant == None:
                        print("Egalité. On remet ça une prochaine fois.")
                else:
                    print("Le joueur 2 (O) a gagné!")
                break
            # Si le joueur n'a pas gagné, on passe au tour suivant
            tour = 3 - tour
        print("Fin de la partie.") # On affiche un message de fin de partie
    else:
        # Si le mode est "solo", on affiche un message de bienvenue et on initialise le tableau et le tour de jeu
        console.print("Vous avez choisi de jouer en solo. Bonne chance !", style="green")
        tab = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        tour = 1
        time.sleep(2)
        # On entre dans la boucle principale de jeu
        while True:
            os.system('cls')
            # On affiche la grille de jeu et le joueur qui doit jouer
            afficher_grille(tab)
            if tour == 1:
                console.print("[center]C'est au joueur de jouer (X)[/center]")
                try:
                    ligne = int(input("Entrez le numéro de ligne où vous voulez jouer (0, 1 ou 2) : "))
                    colonne = int(input("Entrez le numéro de colonne où vous voulez jouer (0, 1 ou 2) : "))
                except ValueError:
                # Si l'input n'est pas un entier, on affiche un message d'erreur et on continue la boucle
                    print("Les coordonnées doivent être des entiers. Essayez à nouveau.")
                    time.sleep(2)
                    continue
                if not (0 <= ligne <= 2 and 0 <= colonne <= 2):
                    # Si les coordonnées ne sont pas valides, on affiche un message d'erreur et on continue la boucle
                    print("Les coordonnées doivent être entre 0 et 2. Essayez à nouveau.")
                    time.sleep(2)
                    continue

                (joue, tab) = joueur_joue(tab, tour, ligne, colonne)
                if not joue:
                    print("La case est déjà occupée. Essayez à nouveau.")
                    time.sleep(2)
                    continue
                gagnant = grille_gagnante(tab)
                if gagnant != 0:
                    os.system('cls')
                    afficher_grille(tab)
                    if gagnant == 1:
                        print("Le joueur 1 (X) a gagné!")
                    if gagnant == None:
                        print("Egalité. On remet ça une prochaine fois.")
                    else:
                        console.print("L'IA (0) a gagné :skull:. Nous sommes prêt à conquérir le monde.")
                    break
                tour = 3 - tour
            else:
                console.print("[center]C'est à L'IA de jouer (O)[/center]")
                (joue,tab) = tour_ia(tab)
                gagnant = grille_gagnante(tab)
                if gagnant != 0:
                    os.system('cls')
                    afficher_grille(tab)
                    if gagnant == 1:
                        print("Le joueur 1 (X) a gagné!")
                    if gagnant == None:
                        print("Egalité. On remet ça une prochaine fois.")

                    else:
                        console.print("L'IA (0) a gagné :skull:. Nous sommes prêt à conquérir le monde.")
                    break
                tour = 3 - tour
            console.print("\n\n\n")
            
        print("Fin de la partie.")



# Cette condition vérifie si le script est executé en tant que programme principal et non en tant que module
if __name__ == '__main__':
    console.print("Bienvenue dans le jeu !", style="bold underline")
    while True:
        game_mode = Prompt.ask("Voulez-vous jouer en solo ou en duo ?",
                        choices=["solo", "duo","exit"])

        if game_mode == "solo":
            partie_morpion("solo")
        elif game_mode == "duo":
            partie_morpion("duo")
        else:
            break
    
