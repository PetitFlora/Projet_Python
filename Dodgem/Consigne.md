# Dodgem
## Les règles du jeu
Ce jeu a été créé en 1972 par Colin Vout.

Deux joueurs s’affrontent sur un plateau bi-dimensionnel carré de n cases sur n cases.

Le premier joueur possède des pions blancs et le second des pions noirs.

Initialement le premier joueur dispose n−1 pions sur la dernière ligne en excluant la première case de celle-ci, et le second joueur dispose n−1 pions sur la première colonne en excluant la dernière case de celle-ci.

À tour de rôle, chaque joueur déplace l'un de ses pions vers une case vide orthogonalement adjacente.

Le premier joueur ne peut déplacer un pion que vers le haut, vers la gauche ou vers la droite.

Le second joueur ne peut déplacer un pion que vers la droite, vers le haut ou vers le bas.

Si le premier joueur possède un pion sur la ligne du haut et qu'il décide de le déplacer vers le haut, ce pion sort définitivement du plateau.

Si le second joueur possède un pion sur la colonne de droite et qu'il décide de le déplacer vers la droite, ce pion sort définitivement du plateau.

Un joueur gagne la partie s'il réussit à faire sortir tous ses pions du plateau ou si tous ses pions sont bloqués par ceux de son adversaire.




## Implémentation de ce jeu en Python

Remarques importantes :

- On pourra éventuellement implémenter des sous-programmes en plus de ceux demandés.
- La grille sera naturellement une liste à deux dimensions d’entiers égaux à 0, 1 ou 2. Une case vide sera représentée par 0, un pion du premier joueur par 1 et un pion du second par 2.
- Plutôt que de recalculer régulièrement la dimension de cette liste on préfèrera la passer en paramètre de nos sous-programmes.
- L’exemple de rendu visuel du programme n’est qu’indicatif, vous pouvez l’améliorer.


Notations des paramètres des sous-programmes que l’on va implémenter :

- `board` : liste à deux dimensions d’entiers égaux à 0, 1 ou 2 représentant le plateau de jeu.
- `n` : entier strictement positif égal au nombre de lignes et de colonnes de `board`.
- `player` : entier représentant le joueur dont c’est le tour (par exemple 1 pour le premier joueur et 2 pour le second).
- `i`, `j` : entiers quelconques.
- `directions` : un t-uple de 4 couples constituant les 4 directions orthogonales possibles directions = ((-1, 0), (0, 1), (1, 0), (0, -1)).
- `m` : entier compris entre 1 et 4 qui repère l'une des 4 directions.


Implémenter les sous-programmes suivants :

- Une fonction `newBoard(n)` qui retourne une liste à deux dimensions représentant l’état initial d’un plateau de jeu de n cases sur n cases.
- Une procédure `displayBoard(board, n)` qui réalise l’affichage du plateau sur la console. On représentera une case vide par un ‘.’, un pion blanc par un ‘x’ et un pion noir par un ‘o’. On numérotera les lignes et les colonnes (à partir de 1) pour que les joueurs puissent repérer facilement les coordonnées d'une case. La configuration initiale du plateau de 5 lignes et 5 colonnes sera donc affichée comme cela :
- Une fonction `possiblePawn(board, n, directions, player, i, j` qui retourne True si i et j sont les coordonnées d’un pion que le joueur player peut déplacer, et False sinon.
- Une fonction `selectPawn(board, n, directions, player)` qui fait saisir au joueur player les coordonnées d’un pion pouvant se déplacer. On supposera qu’il existe un tel pion, on ne testera pas ce fait ici. Tant que ces coordonnées ne seront pas valides en regard des règles du jeu et des dimensions du plateau, on lui demandera de nouveau de les saisir. Finalement, la fonction retournera ces coordonnées.
- Une fonction `possibleMove(board, n, directions, player, i, j, m)` où l’on suppose ici que i et j sont les coordonnées du pion que le joueur player souhaite déplacer. Cette fonction retourne True si le joueur player peut déplacer ce pion dans la direction m et False sinon.
- Une fonction `selectMove(board, n, directions, player, i, j)` où l’on suppose ici que i et j sont les coordonnées du pion que le joueur player souhaite déplacer. Cette fonction fait saisir au joueur player une direction dans laquelle il souhaite déplacer ce pion. Tant que cette direction ne sera pas valide en regard des règles du jeu et des dimensions du plateau, on lui demandera de nouveau de la saisir. Finalement, la fonction retournera cette direction.
- Une procédure `move(board, n, directions, player, i, j, m)` où l’on suppose ici que i et j sont les coordonnées du pion que le joueur player souhaite déplacer dans la direction m. Cette procédure réalise ce déplacement.
- Une fonction `win(board, n, directions, player)` qui retourne True si le joueur player a gagné la partie et False sinon.
- Un programme principal `dodgem(n)` qui utilisera les sous-programmes précédents (et d’autres si besoin est) afin de permettre à deux joueurs de disputer une partie complète sur un plateau de jeu de n cases sur n cases.
