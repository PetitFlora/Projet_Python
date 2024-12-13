# Snort
## Les règles du jeu
Ce jeu a été créé en 1970 par Simon Norton.

Deux joueurs s’affrontent sur un plateau bi-dimensionnel carré de n cases sur n cases initialement vide.

Le premier joueur possède des pions blancs et le second des pions noirs.

À tour de rôle, chaque joueur place un pion sur une case vide non adjacente orthogonalement à une case contenant un pion de l'adversaire.

Le gagnant est le dernier joueur à pouvoir placer l'un de ses pions. Ou de façon équivalente, un joueur perd la partie dès qu'il ne peut plus placer l'un de ses pions sur le plateau.



## Implémentation de ce jeu en Python
Il vous est fortement recommandé de lire l’intégralité de cette partie avant de commencer à coder.

Remarques importantes :

- On pourra éventuellement implémenter des sous-programmes en plus de ceux demandés.
- Le plateau sera naturellement une liste à deux dimensions d’entiers égaux à 0, 1 ou 2. Une case vide sera représentée par 0, un pion du premier joueur par 1 et un pion du second par 2.
- Plutôt que de recalculer régulièrement la dimension de cette liste on préfèrera la passer en paramètre de nos sous-programmes.
- L’exemple de rendu visuel du programme n’est qu’indicatif, vous pouvez l’améliorer.


Notations des paramètres des sous-programmes que l’on va implémenter :

- `board` : liste à deux dimensions d’entiers égaux à 0, 1 ou 2 représentant le plateau de jeu.
- `n` : entier strictement positif égal au nombre de lignes et de colonnes de `board`. 
- `player` : entier représentant le joueur dont c’est le tour (par exemple 1 pour le premier joueur et 2 pour le second).
- `i`, `j` : entiers quelconques.


Implémenter les sous-programmes suivants :

- Une fonction `newBoard(n)` qui retourne une liste à deux dimensions représentant l’état initial d’un plateau de jeu de n cases sur n cases.
- Une procédure `displayBoard(board, n)` qui réalise l’affichage du plateau sur la console. On représentera une case vide par un ‘.’, un pion blanc par un ‘x’ et un pion noir par un ‘o’. On numérotera les lignes et les colonnes (à partir de 1) pour que les joueurs puissent repérer facilement les coordonnées d'une case.  On aura donc un affichage ressemblant à celui-ci (après quelques tours de jeu) :
- Une fonction `possibleSquare(board, n, player, i, j)` qui retourne True si i et j sont les coordonnées d’une case où le joueur player peut poser un pion, et False sinon.
- Une fonction `selectSquare(board, n, player)` qui fait saisir au joueur player les coordonnées d’une case où il peut poser un pion. On supposera qu’il existe une telle case, on ne testera pas ce fait ici. Tant que ces coordonnées ne seront pas valides en regard des règles du jeu (et des dimensions du plateau), on lui demandera de nouveau de les saisir. Finalement, la fonction retournera ces coordonnées.
- Une procédure `updateBoard(board, player, i, j)` où l’on suppose ici que i et j sont les coordonnées d’une case où le joueur player peut poser un pion. Cette procédure réalise cette pose.
- Une fonction `again(board, n, player)` qui retourne True si le joueur player peut encore poser un pion sur le plateau et False sinon.
- Un programme principal `snort(n)` qui utilisera les sous-programmes précédents (et d’autres si besoin est) afin de permettre à deux joueurs de disputer une partie complète sur un plateau de jeu de n cases sur n cases.
