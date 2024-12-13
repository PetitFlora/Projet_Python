# ########################################################################## #
#                                  Dodgem                                    #
# ########################################################################## #


# ########################### Les règles du jeu ############################ #
#                                                                            #
# Ce jeu a été créé en 1972 par Colin Vout.                                  #
#                                                                            #
# Deux joueurs s’affrontent sur un plateau bi-dimensionnel carré de n cases  #
# sur n cases initialement vide.                                             #
#                                                                            #
# Le premier joueur possède des pions blancs et le second des pions noirs.   #
#                                                                            #
# Initialement le premier joueur dispose n−1 pions sur la dernière ligne en  #
# excluant la première case de celle-ci, et le second joueur dispose n−1     #
# pions sur la première colonne en excluant la dernière case de celle-ci.    #
#                                                                            #
# À tour de rôle, chaque joueur déplace l'un de ses pions vers une case      #
# vide orthogonalement adjacente.                                            #
#                                                                            #
# Le premier joueur ne peut déplacer un pion que vers le haut, vers la       #
# gauche ou vers la droite.                                                  #
#                                                                            #
# Le second joueur ne peut déplacer un pion que vers la droite, vers le      #
# haut ou vers le bas.                                                       #
#                                                                            #
# Si le premier joueur possède un pion sur la ligne du haut et qu'il         #
# décide de le déplacer vers le haut, ce pion sort définitivement du         #
# plateau.                                                                   #
#                                                                            #
# Si le second joueur possède un pion sur la colonne de droite et qu'il      #
# décide de le déplacer vers la droite, ce pion sort définitivement du       #
# plateau.                                                                   #
#                                                                            #
# Un joueur gagne la partie s'il réussit à faire sortir tous ses pions du    #
# plateau ou si tous ses pions sont bloqués par ceux de son adversaire.      #
#                                                                            #
# ########################################################################## #




def new_board(n):
    """
    Retourne une liste à deux dimensions de n cases sur n cases.

    Args:
        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

    Returns:
        list: liste à deux dimensions d'entiers égaux à 0, 1 ou 2 représentant
        le plateau de jeu
    """
    board = [[0] * n for _ in range(n)]
    for i in range(1, n):
        board[n-1][i] = 1
        board[i-1][0] = 2
    return board


def display_board(board, n):
    """
    Réalise l'affichage du plateau dans la console.

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


def possible_pawn(board, n, directions, current_player, i, j):
    """
    Retourne si i et j sont des coordonnées possible d'un pion du joueur.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

        directions (tuple): un tuple de 4 couples constituant les 4 directions
        orthogonales

        current_player (int): entier représentant le joueur dont c'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

        i (int): numéro de la ligne

        j (int): numéro de la colonne

    Returns:
        bool: True si le pion peut-être déplacer, False sinon
    """
    if board[i][j] != current_player:
        return False

    for d in range(4):
        if possible_move(board, n, directions, current_player, i, j, d):
            return True
    return False


def select_pawn(board, n, directions, current_player):
    """
    Fait saisir au joueur les coordonnées d'un pion pouvant se déplacer.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

        directions (tuple): un tuple de 4 couples constituant les 4 directions
        orthogonales

        current_player (int): entier représentant le joueur dont c'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

    Returns:
        tuple: coordonnées d'un pion pouvant se déplacer
    """
    i = int(input("Choisir la ligne d'un pion : ")) - 1
    j = int(input("Choisir la colonne d'un pion : ")) - 1

    while (not (0 <= i < n and 0 <= j < n) or
           not possible_pawn(board, n, directions, current_player, i, j)):
        i = int(input("Choisir la ligne d'un pion : ")) - 1
        j = int(input("Choisir la colonne d'un pion : ")) - 1

    return i, j


def possible_move(board, n, directions, current_player, i, j, m):
    """
    Retourne si le joueur peut déplacer le pion dans la direction m.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

        directions (tuple): un tuple de 4 couples constituant les 4 directions
        orthogonales

        current_player (int): entier représentant le joueur dont c'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

        i (int): numéro de la ligne

        j (int): numéro de la colonne

        m (int): entier compris entre 0 et 3 qui repère l'une des 4 directions

    Returns:
        bool: True si le pion peut-être déplacer dans la direction m
    """
    if (current_player == 1 and m == 2) or (current_player == 2 and m == 3):
        return False

    x, y = i + directions[m][0], j + directions[m][1]

    if ((not (-1 <= x < n and 0 <= y < n) and current_player == 1) or
            (not (0 <= x < n and 0 <= y <= n) and current_player == 2) or
            ((0 <= x < n and 0 <= y < n) and board[x][y] != 0)):
        return False

    return True


def select_move(board, n, directions, current_player, i, j):
    """
    Demande au joueur une direction dans laquelle déplacer son pion.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

        directions (tuple): un tuple de 4 couples constituant les 4 directions
        orthogonales

        current_player (int): entier représentant le joueur dont c'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

        i (int): numéro de la ligne

        j (int): numéro de la colonne

    Returns:
        int: direction dans laquelle le pion va se déplacer
    """
    m = int(input("Choisir la direction du mouvement(1 pour Nord, "
                  "2 pour Est, 3 pour Sud et 4 pour Ouest) : ")) - 1

    while (m not in [0, 1, 2, 3] or
           not possible_move(board, n, directions, current_player, i, j, m)):
        m = int(input("Choisir la direction du mouvement(1 pour Nord,"
                      "2 pour Est, 3 pour Sud et 4 pour Ouest) : ")) - 1

    return m


def move(board, n, directions, current_player, i, j, m):
    """
    Réalise le déplacement du pion.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

        directions (tuple): un tuple de 4 couples constituant les 4 directions
        orthogonales

        current_player (int): entier représentant le joueur dont c'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

        i (int): numéro de la ligne

        j (int): numéro de la colonne

        m (int): entier compris entre 0 et 3 qui repère l'une des 4 directions
    """
    x, y = i + directions[m][0], j + directions[m][1]

    if ((current_player == 1 and x == -1) or
            (current_player == 2 and y == n)):
        board[i][j] = 0
        print(f"Le joueur {current_player} a sorti un pion.")

    else:
        board[i][j] = 0
        board[x][y] = current_player


def still_pawns(board, n, other_player):
    """
    Retourne si le joueur a toujours des pions sur le plateau.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

        other_player (int): entier représentant le joueur dont ce n'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

    Returns:
        bool: True si le joueur a toujours des pions, false sinon
    """
    for i in range(n):
        for j in range(n):
            if board[i][j] == other_player:
                return True

    return False


def win(board, n, directions, current_player):
    """
    Retourne si le joueur a gagné la partie.

    Args:
        board (list): liste à deux dimensions d'entiers égaux à 0, 1 ou 2
        représentant le plateau de jeu

        n (int): entier strictement positif égal au nombre de lignes et de
        colonnes de "board"

        directions (tuple): un tuple de 4 couples constituant les 4 directions
        orthogonales

        current_player (int): entier représentant le joueur dont c'est le tour
        (par exemple 1 pour le premier joueur et 2 pour le second)

    Returns:
        bool: True si le joueur a gagné, False sinon
    """
    for i in range(n):
        for j in range(n):
            if possible_pawn(board, n, directions, current_player, i, j):
                return False

    return True


def dodgem():
    """Boucle principal du jeu de dodgem."""
    game_on = True
    n = int(input("Quelle taille pour le plateau ? "))
    while n < 3:
        n = int(input('Quelle taille pour le plateau ? '))

    board = new_board(n)
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    current_player, other_player = 1, 2

    while game_on:
        display_board(board, n)
        print(f'Au joueur {current_player} de jouer')
        i, j = select_pawn(board, n, directions, current_player)
        m = select_move(board, n, directions, current_player, i, j)
        move(board, n, directions, current_player, i, j, m)

        current_player, other_player = other_player, current_player

        if (win(board, n, directions, current_player) or
                not still_pawns(board, n, other_player)):
            display_board(board, n)

            if win(board, n, directions, current_player):
                print(f'Le joueur {current_player} a gagné(e)')
            else:
                print(f'Le joueur {other_player} a gagné(e)')

            game_on = False


dodgem()
