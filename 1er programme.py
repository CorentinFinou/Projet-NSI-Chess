class case:
    '''classe des cases
    -si vide
    -contenu
    '''
    def __init__(self,x,y,contenu,couleur):
        self.contenu = contenu
        self.x = x
        self.y = y
        self.couleur = couleur

    def estVide(self):
        if self.contenu == None:
            return True
        else:
            return False
    
    def getParamCase(self):
        return self.contenu,self.y,self.x,self.couleur
    
    def modifContenu(self,new):
        self.contenu = new
        
    def couleurContenuDifferentVerif(self,couleur):
        try:
            if self.contenu.couleur == couleur:
                return False,self.contenu.couleur,self.contenu,self.y,self.x
            else:
                return True
        except AttributeError:
            print(self.contenu,self.y,self.x)
            return False

class pièce:
    '''class des pions, sera parent des classes pion, fou, cavalier, tour, reine, roi
    -position
    '''
    def __init__(self,x,y,couleur):
        try:
            assert x>=0 and y>=0, 'Les coordonnées de pièces doivent être des chiffres positifs'
            assert couleur == 'blanc' or couleur == 'noir'
            self.x = x
            self.y = y
            self.couleur = couleur
        except AssertionError as error:
            raise error
        except TypeError:
            raise TypeError('Les coordonnées doivent être des int')
    
    def avoirPosition(self):
        return self.x,self.y

    def avoirCouleur(self):
        return self.couleur

class pion(pièce):
    def __init__(self, x, y,couleur,aBougé = False):
        pièce.__init__(self,x,y,couleur)
        self.aBoujé = aBougé
    
    def symbole(self):
        if self.couleur == 'blanc':
            return '♟'
        else:
            return '♙'

    def mouvement(self, xOr, yOr, xDest, yDest): ###Ajouter vérification case vide
        if self.couleur == 'blanc':
            if self.aBoujé == False:
                possibilités = [(self.x,self.y-1),(self.x,self.y-2)]
            else:
                possibilités = [(self.x,self.y-1)]
        else:
            if self.aBoujé == False:
                possibilités = [(self.x,self.y+1),(self.x,self.y+2)]
            else:
                possibilités = [(self.x,self.y+1)]
        print(possibilités)
        try:
            assert (xDest,yDest) in possibilités, 'Mouvement impossible'
        except AssertionError as error:
            raise
        plateau1.plateau[yOr][xOr].modifContenu(None)
        plateau1.plateau[yDest][xDest].modifContenu(pion(yDest,xDest,self.couleur,True))

class tour(pièce): #pièce marchant, ne plus toucher sauf pour ajout
    def __init__(self, x, y,couleur):
        pièce.__init__(self,x,y,couleur)
    
    def symbole(self):
        if self.couleur == 'blanc':
            return '♜'
        else:
            return '♖'

    def mouvement(self, xOr, yOr, xDest, yDest):
        possibilités = []
        for i in range(7-yOr): #vérification vers le bas
            if plateau1.plateau[yOr+i+1][xOr].estVide() == True:
                possibilités.append((i+yOr+1,xOr))
            elif plateau1.plateau[yOr+i+1][xOr].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((i+yOr+1,xOr))
                break
            else:
                break
        for i in range(7-xOr): #vérification vers la droite
            if plateau1.plateau[yOr][xOr+i+1].estVide() == True:
                possibilités.append((yOr,i+xOr+1))
            elif plateau1.plateau[yOr][xOr+i+1].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((yOr,xOr+i+1))
            else:
                break
        for i in range(yOr): #vérification vers la gauche
            if plateau1.plateau[yOr-i-1][xOr].estVide() == True:
                possibilités.append((yOr-i-1,xOr))
            elif plateau1.plateau[yOr-i-1][xOr].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((i-yOr-1,xOr))
                break
            else:
                break
        for i in range(xOr): #vérification vers le haut
            if plateau1.plateau[yOr][xOr-i-1].estVide() == True:
                possibilités.append((yOr,xOr-i-1))
            elif plateau1.plateau[yOr][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((yOr,xOr-i-1))
                break
            else:
                break
        try:
            assert (yDest,xDest) in possibilités, 'Mouvement impossible'
            plateau1.plateau[yOr][xOr].modifContenu(None)
            plateau1.plateau[yDest][xDest].modifContenu(tour(yDest,xDest,self.couleur))
            print(possibilités)
        except AssertionError as error:
            print('Mouvement Impossible')

class fou(pièce):
    def __init__(self, x, y,couleur):
        pièce.__init__(self,x,y,couleur)
    
    def symbole(self):
        if self.couleur == 'blanc':
            return '♝'
        else:
            return '♗'

    def mouvement(self, xOr, yOr, xDest, yDest):
        possibilités = []
        for i in range(7-yOr if 7-yOr<7-xOr else 7-xOr): #vérification SE
            if plateau1.plateau[yOr+i+1][xOr+i+1].estVide() == True:
                possibilités.append((yOr+i+1,xOr+i+1))
            elif plateau1.plateau[yOr+i+1][xOr+i+1].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((i+yOr+1,xOr+i+1))
                break
            else:
                break
        for i in range(yOr if yOr<7-xOr else 7-xOr): #vérification NE
            if plateau1.plateau[yOr-i-1][xOr+i+1].estVide() == True:
                possibilités.append((yOr-i-1,xOr+i+1))
            elif plateau1.plateau[yOr-i-1][xOr+i+1].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((yOr-1-i,xOr+i+1))
                break
            else:
                break
        for i in range(xOr if xOr<=yOr else yOr):
            if plateau1.plateau[yOr-i-1][xOr-i-1].estVide() == True:
                possibilités.append((yOr-i-1,xOr-i-1))
            elif plateau1.plateau[yOr-i-1][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((yOr-i-1,xOr-i-1))
                break
            else:
                break
        for i in range(xOr if xOr<=7-yOr else 7-yOr):
            if plateau1.plateau[yOr+i+1][xOr-i-1].estVide() == True:
                possibilités.append((yOr+i+1,xOr-i-1))
            elif plateau1.plateau[yOr+i+1][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((yOr+i+1,xOr-i-1))
                break
            else:
                break
        print(possibilités)
        print(yDest,xDest)
        try:
            assert (yDest,xDest) in possibilités, 'Mouvement impossible'
            plateau1.plateau[yOr][xOr].modifContenu(None)
            plateau1.plateau[yDest][xDest].modifContenu(fou(self.x,self.y,self.couleur))
        except AssertionError as error:
            print('Mouvement Impossible')

class cavalier(pièce):
    def __init__(self, x, y,couleur):
        pièce.__init__(self,x,y,couleur)
    
    def symbole(self):
        if self.couleur == 'blanc':
            return '♞'
        else:
            return '♘'
        
    def mouvement(self, xOr, yOr, xDest, yDest):
        possibilités = []
        mouvements = [(-1,-2),(-1,2),(-2,1),(2,1),(1,2),(1,-2),(2,-1),(-2,-1)]
        for i in mouvements: #vérification SE
            if 7>= yOr+i[0] >= 0 and 7>= xOr+i[1] >= 0:
                if plateau1.plateau[yOr+i[0]][xOr+i[1]].estVide() == True or plateau1.plateau[yOr+i[0]][xOr+i[1]].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr+i[0],xOr+i[1]))
        print(possibilités)
        print(yDest,xDest)
        try:
            assert (yDest,xDest) in possibilités, 'Mouvement impossible'
            plateau1.plateau[yOr][xOr].modifContenu(None)
            plateau1.plateau[yDest][xDest].modifContenu(cavalier(self.x,self.y,self.couleur))
        except AssertionError as error:
            print((yDest,xDest),possibilités)
            print((yDest,xDest) in possibilités)
            print('Mouvement Impossible')

class reine(pièce):
    def __init__(self, x, y,couleur):
        pièce.__init__(self,x,y,couleur)

    def symbole(self):
        if self.couleur == 'blanc':
            return '♛'
        else:
            return '♕'

class roi(pièce):
    def __init__(self, x, y,couleur):
        pièce.__init__(self,x,y,couleur)

    def symbole(self):
        if self.couleur == 'blanc':
            return '♚'
        else:
            return '♔'

class plateau:
    def __init__(self):
        self.plateau=[]
        dec = False
        for i in range(8):
            ligne = []
            for j in range(8):
                if dec == False:
                    ligne.append(case(j,i,None,'noir'))
                    dec = True
                else:
                    ligne.append(case(j,i,None,'blanc'))
                    dec = False
            if dec == False : dec = True
            else : dec = False
            self.plateau.append(ligne)
            """
        for i in range(8):
            self.plateau[0][i].modifContenu([tour(i,1,'noir'),cavalier(i,1,'noir'),fou(i,1,'noir'),reine(i,1,'noir'),roi(i,1,'noir'),fou(i,1,'noir'),cavalier(i,1,'noir'),tour(i,1,'noir')][i])
            self.plateau[7][i].modifContenu([tour(i,1,'blanc'),cavalier(i,1,'blanc'),fou(i,1,'blanc'),reine(i,1,'blanc'),roi(i,1,'blanc'),fou(i,1,'blanc'),cavalier(i,1,'blanc'),tour(i,1,'blanc')][i])
            self.plateau[1][i].modifContenu(pion(i,1,'noir'))
            self.plateau[6][i].modifContenu(pion(i,6,'blanc'))"""

    def afficherPlateau(self):
        self.affichage = []
        for i in range (8):
            ligne = []
            for j in range(8):
                case = self.plateau[i][j]
                if case.estVide()==True:
                    if case.couleur == 'noir': ligne.append('■')
                    else: ligne.append('□')
                else:
                    ligne.append(case.contenu.symbole())
            self.affichage.append(ligne)
        for i in range(8):
            print(self.affichage[i])

    def getParam(self,y,x):
            assert self.plateau!=None
            return(self.plateau[y][x].getParamCase())
            
    def changeContenu(self,y,x,type,couleur):
        self.plateau[y][x].modifContenu(type(y,x,couleur))


def demandeDeMouvement(xOr,yOr,xDest,yDest):
    '''Transfome le format d'échec normal (case en bas à droite = a1) en format prog (case en bas à droite = (y=7, x=0))
       Puis envoie requète de mouvement à l'objet correspondant
    '''
    xPlateau = ['a','b','c','d','e','f','g','h']
    yPlateau = [i for i in range(1,9)]
    try:
        assert xOr in xPlateau and xDest in xPlateau, 'Coordonnées x invalides'
        assert yOr in yPlateau and yDest in yPlateau, 'Coordonnées y invalides'
        xOr = xPlateau.index(xOr)
        xDest = xPlateau.index(xDest)
        yOr = 8-yOr
        yDest = 8-yDest
        try:
            assert plateau1.plateau[yOr][xOr].estVide() == False, "Il n'y a pas de pièce sur cette case"
            plateau1.getParam(yOr,xOr)[0].mouvement(xOr,yOr,xDest,yDest)
            plateau1.afficherPlateau()
            print(' ')
            demandeDeMouvement(input("Lettre correspondant à la coordonée x de la pièce : "),int(input("Chiffre correspondant à la coordonée y de la pièce : ")),input("Lettre correspondant à la coordonée x de la destination : "),int(input("Chiffre correspondant à la coordonée y de la destination : ")))
        except AssertionError as error:
            raise error           

    except AssertionError as error:
        raise error






plateau1 = plateau()
plateau1.changeContenu(4,3,fou,'blanc')
plateau1.changeContenu(4,1,pion,'noir')
plateau1.afficherPlateau()
print(' ')
demandeDeMouvement(input("Lettre correspondant à la coordonée x de la pièce : "),int(input("Chiffre correspondant à la coordonée y de la pièce : ")),input("Lettre correspondant à la coordonée x de la destination : "),int(input("Chiffre correspondant à la coordonée y de la destination : ")))
