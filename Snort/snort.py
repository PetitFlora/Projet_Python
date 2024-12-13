# ########################################################################## #
#                                   Snort                                    #
# ########################################################################## #


# ########################### Les règles du jeu ############################ #
#                                                                            #
# Ce jeu a été créé en 1970 par Simon Norton.                                #
#                                                                            #
# Deux joueurs s’affrontent sur un plateau bi-dimensionnel carré de n cases  #
# sur n cases initialement vide.                                             #
#                                                                            #
# Le premier joueur possède des pions blancs et le second des pions noirs.   #
#                                                                            #
# À tour de rôle, chaque joueur place un pion sur une case vide non          #
# adjacente orthogonalement à une case contenant un pion de l'adversaire.    #
#                                                                            #
# Le gagnant est le dernier joueur à pouvoir placer l'un de ses pions.       #
# Ou de façon équivalente, un joueur perd la partie dès qu'il ne peut plus   #
# placer l'un de ses pions sur le plateau.                                   #
#                                                                            #
# ########################################################################## #




def new_board(n):
    """
    Retourne une liste à deux dimensions de n cases sur n cases.

    Args:
        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

    Returns:
        list: liste bidimensionnelle représentant le plateau
    """
    return [[0] * n for i in range(n)]


def display_board(board, n):
    """
    Réalise l'affichage du plateau sur la console.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"
    """
    affiche = ['.', 'x', 'o']
    for i in range(n):
        print(i+1, '|', end=' ')
        for elt in board[i]:
            print(affiche[elt], end=' ')
        print()

    print('    ', 2*n*'_')

    print('      ', end='')
    for i in range(n):
        print(i+1, end=' ')
    print()


def possible_square(board, n, other_player, i, j):
    """
    Retourne si le joueur peut poser son pion sur la case.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

        other_player (int): entier représentant le joueur dont ce n'est le
        tour (par exemple 1 pour le premier joueur et 2 pour le second)

        i (int): numéro de la ligne

        j (int): numéro de la colonne

    Returns:
        bool: True si la case est jouable, False sinon
    """
    if board[i][j] != 0:
        return False

    if ((i > 0 and board[i-1][j] == other_player) or
            (i < n-1 and board[i+1][j] == other_player) or
            (j > 0 and board[i][j-1] == other_player) or
            (j < n-1 and board[i][j+1] == other_player)):
        return False

    return True


def select_square(board, n, other_player):
    """
    Demande au joueur les coordonnées d'une case où il peut poser un pion.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

        current_player (int): entier représentant le joueur dont c'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

        other_player (int): entier représentant le joueur dont ce n'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

    Returns:
        tuple: les coordonnées entées par le joueur
    """
    i = int(input('Choisir un numéro de ligne : ')) - 1
    j = int(input('Choisir un numéro de colonne : ')) - 1

    while (not (0 <= i < n and 0 <= j < n) or
            not possible_square(board, n, other_player, i, j)):
        i = int(input('Choisir un numéro de ligne : ')) - 1
        j = int(input('Choisir un numéro de colonne : ')) - 1

    return i, j


def update_board(board, current_player, i, j):
    """
    Réalise la pose du pion.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        current_player (int): entier représentant le joueur dont c'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

        i (int): numéro de la ligne

        j (int): numéro de la colonne
    """
    board[i][j] = current_player


def again(board, n, other_player):
    """
    Retourne si le joueur player peut encore poser un pion sur le plateau.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

        other_player (int): entier représentant le joueur dont ce n'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

    Returns:
        bool: True si il est encore possible de jouer, False sinon
    """
    for i in range(n):
        for j in range(n):
            if possible_square(board, n, other_player, i, j):
                return True

    return False


def snort():
    """Boucle principal du jeu de snort."""
    game_on = True
    n = int(input('Quelle taille pour le plateau ? '))
    while n < 3:
        n = int(input('Quelle taille pour le plateau ? '))

    board = new_board(n)
    current_player, other_player = 1, 2

    while game_on:
        display_board(board, n)
        print(f'Au joueur {current_player} de jouer')
        i, j = select_square(board, n, other_player)
        update_board(board, current_player, i, j)

        current_player, other_player = other_player, current_player

        if not again(board, n, other_player):
            display_board(board, n)
            current_player, other_player = other_player, current_player

            print(f'Le joueur {current_player} a gagné(e)')
            game_on = False


snort()
