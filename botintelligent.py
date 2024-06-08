import copy
import random

def jouables(grille: list) -> list:
    """
    Renvoie une liste des colonnes jouables dans la grille.

    Arguments:
        grille (list): La grille de jeu représentée sous forme de liste.

    Retourne:
        list: Une liste des colonnes jouables dans la grille.
    """
    colonnes = []

    for i in range(7):
        if grille[5][i] == 0:
            colonnes.append(i)

    return colonnes

def jouer(grille: list, colonne: int, joueur: int) -> list:
    """
    Effectue un coup dans la grille de jeu.

    Arguments:
        grille (list): La grille de jeu.
        colonne (int): La colonne dans laquelle effectuer le coup.
        joueur (int): Le joueur effectuant le coup.

    Retourne:
        list: La grille mise à jour après le coup.
    """
    for i in range(6):
        if grille[i][colonne] == 0:
            grille[i][colonne] = joueur
            return grille

    return grille

def gagne(grille:dict, joueur:int)-> bool:
    """
    Vérifie si le joueur a gagné dans la grille donnée.

    Arguments:
        grille (dict): La grille de jeu représentée sous forme de dictionnaire.
        joueur (int): Le joueur dont on vérifie s'il a gagné (1 ou 2).

    Retourne:
        bool: True si le joueur a gagné, False sinon.
    """
    # Vérification des lignes :
    for i in range(6):
        for j in range(4):
            if grille[i][j] == grille[i][j + 1] == grille[i][j + 2] == grille[i][j + 3] == joueur:
                return True

    # Vérification des colonnes :
    for i in range(7):
        for j in range(3):
            if grille[j][i] == grille[j + 1][i] == grille[j + 2][i] == grille[j + 3][i] == joueur:
                return True

    # Vérification des diagonales en 2 parties :
    for i in range(3):
        for j in range(4):
            if grille[i][j] == grille[i + 1][j + 1] == grille[i + 2][j + 2] == grille[i + 3][j + 3] == joueur:
                return True

    for i in range(3):
        for j in range(3, 7):
            if grille[i][j] == grille[i + 1][j - 1] == grille[i + 2][j - 2] == grille[i + 3][j - 3] == joueur:
                return True

    return False

def troispionsplaces(grille, joueur):
    """
    Vérifie si le joueur a placé trois pions consécutifs dans la grille.

    Arguments:
        grille (list): La grille de jeu représentée par une liste de listes.
        joueur (int): Le joueur dont on vérifie les pions (1 ou 2).

    Retourne:
        bool: True si le joueur a placé trois pions consécutifs, False sinon.
    """
    # Vérification des lignes
    for i in range(6):
        for j in range(4):
            if grille[i][j] == grille[i][j + 1] == grille[i][j + 2] == joueur and grille[i][j + 3] == 0:
                return True

    # Vérification des colonnes
    for i in range(7):
        for j in range(3):
            if grille[j][i] == grille[j + 1][i] == grille[j + 2][i] == joueur and grille[j + 3][i] == 0:
                return True
            
    # Vérification des diagonales
    for i in range(3):
        for j in range(4):
            if grille[i][j] == grille[i + 1][j + 1] == grille[i + 2][j + 2] == joueur and grille[i + 3][j + 3] == 0:
                return True
            
    for i in range(3):
        for j in range(3, 7):
            if grille[i][j] == grille[i + 1][j - 1] == grille[i + 2][j - 2] == joueur and grille[i + 3][j - 3] == 0:
                return True

    return False

def simuler(grille:dict, joueur:int)-> dict:
    """
    Effectue une simulation de jeu en utilisant une copie de la grille donnée et le joueur donné.
    Sélectionne le meilleur coup parmi les coups potentiels en évaluant différentes conditions.
    
    Arguments:
        grille (dict): La grille de jeu représentée par un dictionnaire.
        joueur (int): Le joueur actuel (1 ou 2).
        
    Retourne:
        dict: Le meilleur coup à jouer.
    """
    grille_copie = copy.deepcopy(grille)

    coups_potentiels = jouables(grille)
    meilleur_coup = random.choice(coups_potentiels)

    for coup in coups_potentiels:
        grille_copie = jouer(grille_copie, coup, joueur)

        jouer(grille_copie, coup, joueur)

        if gagne(grille_copie, joueur):
            meilleur_coup = coup
        elif gagne(grille_copie, joueur%2+1):
            meilleur_coup = coup
        elif troispionsplaces(grille_copie, joueur):
            meilleur_coup = coup
        elif troispionsplaces(grille_copie, joueur%2+1):
            meilleur_coup = coup

    return meilleur_coup

def choix(partie: dict)-> int:
    grille = partie["grille"]
    tourDe = partie["tourDe"]
    dernierCoup = partie["dernierCoup"]

    if dernierCoup is None:
        return 3
    
    return simuler(grille, tourDe)