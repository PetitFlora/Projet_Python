from tkinter import *


class Joueur:
    """Classe représantant un joueur."""

    def __init__(self, joueur, x, y, nb_pions, n):
        """Constructeur de la classe Joueur.

        Args:
            joueur (int): 1 ou 2, numéro du joueur
            x (int): coordonnée x de la reine
            nb_pions (int): nombre de pions
            y (int): coordonnée y de la reine
            n (int): taille du plateau
        """
        self._joueur = joueur
        self._reine = joueur + 2  # 3 ou 4 pour le numéro de la reine
        self._x = x
        self._y = y
        self._nb_pions = nb_pions
        self._n = n
        # Crée la liste des coordonnées des tours
        self._liste_pions = self.creer_liste()

    def set_x(self, x):
        """Setter de _x.

        Args:
            x (int): coordonné x de la reine
        """
        self._x = x

    def set_y(self, y):
        """Setter de _y.

        Args:
            y (int): coordonné y de la reine
        """
        self._y = y

    def set_nb_pions(self, nb_pions):
        """Setter de _nb_pions.

        Args:
            nb_pions (int): nombre de pion(s) du joueur
        """
        self._nb_pions = nb_pions

    def set_n(self, n):
        """Setter de _n.

        Args:
            n (int): taille du plateau
        """
        self._n = n

    def get_joueur(self):
        """Getter de _joueur.

        Returns:
            int: 1 ou 2, numéros du joueur
        """
        return self._joueur

    def get_reine(self):
        """Getter de _reine.

        Returns:
            int: 3 ou 4, numéros de la reine
        """
        return self._reine

    def get_x(self):
        """Getter de _x.

        Returns:
            int: coordonné x de la reine
        """
        return self._x

    def get_y(self):
        """Getter de _y.

        Returns:
            int: coordonné y de la reine
        """
        return self._y

    def get_nb_pions(self):
        """Getter de _nb_pions.

        Returns:
            int: nombre de pion(s) du joueur
        """
        return self._nb_pions

    def get_n(self):
        """Getter de _n.

        Returns:
            _type_: _description_
        """
        return self._n

    def get_liste_pions(self):
        """Getter de _liste_pions.

        Returns:
            list: liste des coordonnées des pions du joueur
        """
        return self._liste_pions

    def creer_liste(self):
        """Crée une liste avec les coordonnées des tours.

        Returns:
            list: liste des coordonnées
        """
        liste = []
        if self.get_joueur() == 1:  # Pour le joueur 1
            for i in range(self.get_n()//2, self.get_n()):
                for j in range(0, self.get_n()//2):
                    liste.append((i, j))

        else:  # Pour le joueur 2
            for i in range(0, self.get_n()//2):
                for j in range(self.get_n()//2, self.get_n()):
                    liste.append((i, j))

        return liste


class Jeu:
    """Classe représantant le Jeu."""

    __couleurs = ['grey15', 'SteelBlue1', 'PaleVioletRed1', 'navy', 'VioletRed4']

    def __init__(self, n=12):
        """Constructeur de la classe Jeu.

        Args:
            n (int): taille du plateau
        """
        self.__n = n
        self.__nb_pions = ((self.__n**2) // 4)  # Nombre de pions de chaque joueurs
        self.__joueur_actuel = Joueur(1, self.get_n()-1, 0, self.get_nb_pions(), self.get_n())  # Joueur actuelle (joueur 1 au debut de la partie)
        self.__autre_joueur = Joueur(2, 0, self.get_n()-1, self.get_nb_pions(), self.get_n())  # Autre joueur (joueur 2 au debut de la partie)
        self.__taille = 100 + self.get_n() * 50  # 100 = marge de 50 px de chaque cotées
        self.__plateau = self.creer_plateau()  # Créer un plateau avec la méthode correspondante

        self.f = Tk()
        self.f.geometry('400x500')  # Taille par default de la fenêtre
        self.f.title('Jeu sans nom')

        self.__termine = False  # Si la partie est fini ou pas
        self.__pions = [[None for _ in range(self.__n)] for _ in range(self.__n)]  # Liste de l'affichage des pions
        self.__pion_selectionne = False  # Si un pion est séléctionné
        self.__i1, self.__j1 = 0, 0  # Coordonnées du pion séléctionné

        self.afficher_menu()
        self.f.mainloop()

    def set_n(self, n):
        """Setter de __n.

        Args:
            n (int): taille du plateau
        """
        self.__n = n

    def set_nb_pions(self, nb_pion):
        """Setter de __nb_pions.

        Args:
            nb_pion (int): nombre de pion(s) de chaque joueurs
        """
        self.__nb_pions = nb_pion

    def set_joueur_actuel(self, joueur_actuel):
        """Setter de __joueur_actuel.

        Args:
            joueur_actuel (class): Instance de la classe Joueur
        """
        self.__joueur_actuel = joueur_actuel

    def set_autre_joueur(self, autre_joueur):
        """Setter de __autre_joueur.

        Args:
            joueur_actuel (class): Instance de la classe Joueur
        """
        self.__autre_joueur = autre_joueur

    def set_taille(self, taille):
        """Setter de __taille.

        Args:
            taille (int): taille de la fenêtre Tkinter
        """
        self.__taille = taille

    def set_plateau(self, i, j, valeur):
        """Setter de __plateau.

        Args:
            i (int): coordonné i dans le plateau
            j (int): coordonné j dans le plateau
            valeur (int): valeur à affecter
        """
        self.__plateau[i][j] = valeur

    def set_terminer(self, termine):
        """Setter de __termine.

        Args:
            terminer (bool): True si la partie est terminé
        """
        self.__termine = termine

    def set_pions(self, i, j, valeur):
        """Setter de __pions.

        Args:
            i (int): coordonné i dans la liste
            j (int): coordonné j dans la liste
            valeur (objet): create_oval de Tkinter
        """
        self.__pions[i][j] = valeur

    def set_pion_selectionne(self, selectionne):
        """Setter de __pion_selectionne.

        Args:
            selectionne (bool): True si un pion est séléctionné
        """
        self.__pion_selectionne = selectionne

    def set_i1(self, i1):
        """Setter de __i1.

        Args:
            i1 (int): coordonné i du pion séléctionné
        """
        self.__i1 = i1

    def set_j1(self, j1):
        """Setter de __j1.

        Args:
            j1 (int): coordonné j du pion séléctionné
        """
        self.__j1 = j1

    def get_n(self):
        """Getter de __n.

        Returns:
            int: taille du plateau
        """
        return self.__n

    def get_nb_pions(self):
        """Getter de __nb_pions.

        Returns:
            int: nombre de pions de chaque joueurs
        """
        return self.__nb_pions

    def get_joueur_actuel(self):
        """Getter de __joueur_actuel.

        Returns:
            class: instance de la classe Joueur
        """
        return self.__joueur_actuel

    def get_autre_joueur(self):
        """Getter de __autre_joueur.

        Returns:
            class: instance de la classe Joueur
        """
        return self.__autre_joueur

    def get_taille(self):
        """Getter de __taille.

        Returns:
            int: taille de la fenêtre Tkinter
        """
        return self.__taille

    def get_plateau(self):
        """Getter de __plateau.

        Returns:
            list: plateau du jeu
        """
        return self.__plateau

    def get_termine(self):
        """Getter de __termine.

        Returns:
            bool: True si la partie est terminé
        """
        return self.__termine

    def get_pions(self):
        """Gettre de __pions.

        Returns:
            list: listes des pions afficher dans la fenêtre Tkinter
        """
        return self.__pions

    def get_pion_selectionne(self):
        """Gettre de __pion_selectionne.

        Returns:
            bool: True si un pion est séléctionné
        """
        return self.__pion_selectionne

    def get_i1(self):
        """Gettre de __i1.

        Returns:
            int: coordonné i du pion séléctionné
        """
        return self.__i1

    def get_j1(self):
        """Gettre de __j1.

        Returns:
            int: coordonné j du pion séléctionné
        """
        return self.__j1

    def creer_plateau(self):
        """Crée le plateau de jeu.

        Returns:
            list: liste bidimensionnel représentant le plateau
        """
        liste = [[0] * self.get_n() for i in range(self.get_n())]

        for i in range(self.get_joueur_actuel().get_nb_pions()):  # Boucle autant de fois que les joueurs ont de pions
            x1 = self.get_joueur_actuel().get_liste_pions()[i][0]
            y1 = self.get_joueur_actuel().get_liste_pions()[i][1]

            x2 = self.get_autre_joueur().get_liste_pions()[i][0]
            y2 = self.get_autre_joueur().get_liste_pions()[i][1]

            liste[x1][y1] = 1  # Écrit le nb du joueur actuel
            liste[x2][y2] = 2  # Écrit le nb de l'autre joueur

        liste[self.get_n()-1][0] = 3  # Écrit le nb de la reine du joueur actuel
        liste[0][self.get_n()-1] = 4  # Écrit le nb de la reine de l'autre joueur

        return liste

    def pion_possible(self, i, j):
        """Vérifie si le pion est jouable.

        Args:
            i (int): coordonnée i du pion
            j (int): coordonnée j du pion

        Returns:
            bool: True si le pion est jouable, False sinon
        """
        deplacement = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
        if self.get_plateau()[i][j] in [self.get_joueur_actuel().get_joueur(),
                                        self.get_joueur_actuel().get_reine()]:
            for element in deplacement:
                x, y = element[0], element[1]
                if (0 <= x < self.get_n()) and (0 <= y < self.get_n()) and self.get_plateau()[x][y] == 0:  # 0 = case vide
                    return True
        return False

    def deplacement_possible(self, i1, j1, i2, j2):
        """Vérifie si le déplacement est possible.

        Args:
            i1 (int): coordonnée i de départ
            j1 (int): coordonnée j de départ
            i2 (int): coordonnée i d'arrivée
            j2 (int): coordonnée j d'arrivée

        Returns:
            bool: True si le déplacement est possible, False sinonSS
        """
        if ((i1 != i2) and (j1 != j2) and (self.get_plateau()[i1][j1] in [1, 2])  # Si une tour essaie de se déplacer pas en ligne
                or (i1, j1) == (i2, j2)):  # Si un pion essaie de se déplacer sur la case ou il se trouve déjà
            return False

        if i1 == i2:  # Si c'est la même ligne
            if j2 >= j1:  # A droite
                for j in range(j1+1, j2+1):
                    if self.get_plateau()[i1][j] != 0:
                        return False

            else:  # A gauche
                for j in range(j2, j1):
                    if self.get_plateau()[i1][j] != 0:
                        return False

        elif j2 == j1:  # Si c'est la même colonne
            if i2 >= i1:  # En bas
                for i in range(i1+1, i2+1):
                    if self.get_plateau()[i][j1] != 0:
                        return False

            else:  # En haut
                for i in range(i2, i1):
                    if self.get_plateau()[i][j1] != 0:
                        return False

        elif (abs(i1 - i2) != abs(j1 - j2)) and (self.get_plateau()[i1][j1] in [3, 4]):
            # Est-ce qu'un reine essaie de se déplacer pas en diagonnal
            return False

        elif (abs(i1 - i2) == abs(j1 - j2)) and (self.get_plateau()[i1][j1] in [3, 4]):
            # Est-ce qu'un reine essaie de se déplacer en diagonnal
            for nb in range(1, abs(i1 - i2) + 1):
                if i1 < i2:
                    i = i1 + nb
                else:
                    i = i1 - nb
                if j1 < j2:
                    j = j1 + nb
                else:
                    j = j1 - nb

                if self.get_plateau()[i1-nb][j1+nb] != 0:
                    return False

        return True

    def deplacer(self, i1, j1, i2, j2):
        """Déplace le pion.

        Args:
            i1 (int): coordonnée i de départ
            j1 (int): coordonnée j de départ
            i2 (int): coordonnée i d'arrivée
            j2 (int): coordonnée j d'arrivée
        """
        pion = self.get_plateau()[i1][j1]
        self.set_plateau(i1, j1, 0)  # On supprime le pion de sa case de départ
        self.set_plateau(i2, j2, pion)  # On ajoute le pion dans sa case d'arrivée
        if pion in [3, 4]:  # Si c'est une reine on modifie ses coordonnées
            self.get_joueur_actuel().set_x(i2)
            self.get_joueur_actuel().set_y(j2)

    def manger(self, i, j):
        """Mange les pions.

        Args:
            i (int): coordonnée i du pion qui vient d'être joué
            j (int): coordonnée j du pion qui vient d'être joué
        """
        x = self.get_joueur_actuel().get_x()
        y = self.get_joueur_actuel().get_y()
        autre_joueur = self.get_autre_joueur()

        if i >= x:  # Si la reine au dessus de la tour
            i_debut, i_fin = x, i+1
        else:  # si i < x # Si la reine en dessous de la tour
            i_debut, i_fin = i, x+1
        if j >= y:  # Si la reine à gauche de la tour
            j_debut, j_fin = y, j+1
        else:  # si j < y # Si la reine à droite de la tour
            j_debut, j_fin = j, y+1

        for ligne in range(i_debut, i_fin):
            for colonne in range(j_debut, j_fin):
                if self.get_plateau()[ligne][colonne] == autre_joueur.get_joueur():
                    self.set_plateau(ligne, colonne, 0)
                    autre_joueur.set_nb_pions(autre_joueur.get_nb_pions()-1)

    def afficher_menu(self):
        """Affiche les menu dans la fenêtre Tkinter.
        """
        self.menu = Menu(self.f)
        self.f.config(menu=self.menu)
        self.menufichier = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Fichier", menu=self.menufichier)
        self.menufichier.add_command(label = 'Nouveau', command=self.nouveau)  # On ne met pas les parenthèses pour que ça ne se déclanche pas tout de suite

    def nouveau(self):
        """Fenêtre pour démarrer une nouvelle partie.
        """
        self.__nouvelle_partie = Toplevel(self.f)
        self.__nouvelle_partie.geometry("300x150")
        self.__nouvelle_partie.title("Nouvelle partie")
        self.__combien_ligne = Label(self.__nouvelle_partie, text="Combient de ligne pour le plateau")
        self.__combien_ligne.place(x=0, y=0, anchor='nw')

        nb = IntVar()
        #On met lambda pour que la fonction s'exéctute seulement quand l'utilisateur click
        r6 = Radiobutton(self.__nouvelle_partie, text="6", variable=nb, value=6, command=lambda: self.afficher(nb.get()))
        r6.place(x=0, y=20, anchor='nw')
        r8 = Radiobutton(self.__nouvelle_partie, text="8", variable=nb, value=8, command=lambda: self.afficher(nb.get()))
        r8.place(x=40, y=20, anchor='nw')
        r10 = Radiobutton(self.__nouvelle_partie, text="10", variable=nb, value=10, command=lambda: self.afficher(nb.get()))
        r10.place(x=80, y=20, anchor='nw')
        r12 = Radiobutton(self.__nouvelle_partie, text="12", variable=nb, value=12, command=lambda: self.afficher(nb.get()))
        r12.place(x=120, y=20, anchor='nw')

    def afficher(self, n):
        """Affiche les élément du jeu dans la fenêtre Tkinter.

        Args:
            n (int): taille du plateau
        """
        self.set_n(n)
        self.set_nb_pions(((self.get_n()**2)//4))
        self.set_joueur_actuel(Joueur(1, self.get_n()-1, 0, self.get_nb_pions(), self.get_n()))
        self.set_autre_joueur(Joueur(2, 0, self.get_n()-1, self.get_nb_pions(), self.get_n()))
        self.set_taille(100 + self.get_n() * 50)
        self.__plateau = self.creer_plateau()
        self.set_terminer(False)

        self.f.geometry(f'{self.get_taille()}x{100 + self.get_taille()}')  # On adapte la taille
        self.__nouvelle_partie.destroy()  # Ferme la fenêtre pop up

        self.zone_texte = Frame(self.f, bg='grey15')
        self.zone_texte.place(x=0, y=self.get_taille(), anchor="nw", height=100, width=self.get_taille())
        self.player = Label(self.zone_texte, bg='grey15', fg='white', font=("Arial", 25), text=f'Joueur {self.get_joueur_actuel().get_joueur()}')
        self.player.pack(side = 'top')

        self.board = Canvas(self.f, bg='grey15', width=self.get_taille(), height=self.get_taille(), highlightthickness=0, bd=0)
        self.board.place(x=0, y=0, anchor="nw")

        for i in range(self.get_n()):
            for j in range(self.get_n()):
                color = self.__couleurs[self.get_plateau()[i][j]]
                x1, y1 = 50 + j * 50, 50 + i * 50
                x2, y2 = x1 + 50, y1 + 50
                self.board.create_rectangle(x1, y1, x2, y2, outline="white")
                pion = self.board.create_oval(x1+5, y1+5, x2-5, y2-5, fill=color, outline='grey15', width=5)
                self.set_pions(i, j, pion)  # liste constructeur jeu

        self.board.bind("<Button-1>", self.jouer)

    def mise_a_jour(self):
        """Met à jour l'affichage du plateau.
        """
        for i in range(self.get_n()):
            for j in range(self.get_n()):
                color = self.__couleurs[self.get_plateau()[i][j]]
                self.board.itemconfig(self.get_pions()[i][j], fill=color)

    def fini(self):
        """Vérifie si la partie est fini.

        Returns:
            bool: True si la parti est fin, False sinon
        """
        return self.get_joueur_actuel().get_nb_pions() <= 2

    def jouer(self, event):
        """Boucle principal du jeu.
        """
        if self.get_termine():  # retourne rien -> casse 'la boucle'
            return

        x, y = event.x, event.y
        if (50 < x < 50 + self.get_n()*50) and (50 < y < 50 + self.get_n()*50):
            # On vérifie si le clique est dans le plateau (avec les extrémités de x et de y)
            i, j = (y - 50) // 50, (x - 50) // 50  # On récupère les index qui correspondent à ceux de la liste
            if not self.get_pion_selectionne():  # Vérifie si le joueur n'a pas deja sélectionné un pion
                if self.pion_possible(i, j):
                    self.set_pion_selectionne(True)
                    self.board.itemconfig(self.get_pions()[i][j], outline='green')
                    self.set_i1(i)
                    self.set_j1(j)

            else:
                if self.deplacement_possible(self.get_i1(), self.get_j1(), i, j):  # i, j est la case de déplacement
                    self.deplacer(self.get_i1(), self.get_j1(), i, j)
                    self.board.itemconfig(self.get_pions()[self.get_i1()][self.get_j1()], outline='grey15')
                    self.manger(i, j)
                    self.mise_a_jour()
                    self.set_pion_selectionne(False)
                    self.__joueur_actuel, self.__autre_joueur = self.__autre_joueur, self.__joueur_actuel
                    self.player.config(text=f'Joueur {self.get_joueur_actuel().get_joueur()}')

            if self.fini():
                self.player.config(text=f'Le Joueur {self.get_autre_joueur().get_joueur()} à gagné')  # Label tkinter
                self.rejouer = Button(self.zone_texte, text='Rejouer ?', command=self.nouveau)
                self.rejouer.pack()
                self.set_terminer(True)


test = Jeu()