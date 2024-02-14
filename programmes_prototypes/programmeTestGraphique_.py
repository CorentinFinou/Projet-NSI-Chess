import pygame,consts

pygame.init()
fenetrePrincipale = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
imageFondForet = pygame.transform.scale(consts.imageFondForet,(fenetrePrincipale.get_size()[0], fenetrePrincipale.get_size()[1]))
imageShop = pygame.transform.scale(consts.imageShop, (fenetrePrincipale.get_size()[0]/4, fenetrePrincipale.get_size()[1]*0.90))
imagePlateau = pygame.transform.scale(consts.imagePlateau, (fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]*2-80,fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]*2-80))

imgsPiecesB = [consts.imagePionB,consts.imageTourB,consts.imageFouB,consts.imageCavalierB,consts.imageReineB,consts.imageRoiB]
imgsPiecesN = [consts.imagePionN,consts.imageTourN,consts.imageFouN,consts.imageCavalierN,consts.imageReineN,consts.imageRoiN]

class case:
    def __init__(self,x,y,contenu = None):
        self.x = x
        self.y = y
        self.contenu = contenu
        self.size = imagePlateau.get_size()[0]/10
        self.visual = pygame.Rect((self.x)*self.size,(self.y)*self.size,self.size,self.size)

    def estVide(self):
        if self.contenu == None:
            return True
        else:
            return False
    
    def getParamCase(self):
        return self.contenu,self.y,self.x
    
    def modifContenu(self,new):
        self.contenu = new

    def couleurContenuDifferentVerif(self,couleur):
        try:
            if self.contenu.couleur == couleur:
                return False
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
    
    def affichage(self):
        pièces = [pion,tour,fou,cavalier,reine,roi]
        if self.couleur == "blanc":
            self.image = pygame.transform.scale(imgsPiecesB[pièces.index(self.avoirType())], (int(imagePlateau.get_size()[0] / 10), int(imagePlateau.get_size()[0] / 10)))
        else:
            self.image = pygame.transform.scale(imgsPiecesN[pièces.index(self.avoirType())], (int(imagePlateau.get_size()[0] / 10), int(imagePlateau.get_size()[0] / 10)))
        position = centrer_piece(self.x,self.y,self.image)
        fenetrePrincipale.blit(self.image, position)

def centrer_piece(x,y,imagePiece):
        decalage_x = (fenetrePrincipale.get_size()[0] - (imagePlateau.get_width()/10*8)) / 2
        decalage_y = (fenetrePrincipale.get_size()[1] - imagePlateau.get_height()/10*8) / 2
        return decalage_x + imagePiece.get_width()*x,decalage_y+imagePiece.get_height()*(y)
        
class pion(pièce): #ajouter mouvement diagonale lors de couleur différente
    def __init__(self, x, y,couleur,aBougé = False):
        pièce.__init__(self,x,y,couleur)
        self.aBoujé = aBougé
    
    def avoirType(self):
        return pion

    def mouvement(self, xOr, yOr): ###Ajouter vérification case vide
        possibilités = []
        if self.avoirCouleur() ==  'blanc' and yOr > 0:
            if plateau1.plateau[yOr-1][xOr].estVide() == True:
                possibilités.append((yOr-1,xOr))
                if plateau1.plateau[yOr-2][xOr].estVide() == True and self.aBoujé == False and yOr > 1:
                    possibilités.append((yOr-2,xOr))
            for i in [1,-1]:
                if plateau1.plateau[yOr-1][xOr+i].estVide() == False and plateau1.plateau[yOr-1][xOr+i].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr-1,xOr+i))
        if self.avoirCouleur() == 'noir' and yOr < 7:
            if plateau1.plateau[yOr+1][xOr].estVide() == True:
                possibilités.append((yOr+1,xOr))
                if plateau1.plateau[yOr+2][xOr].estVide() == True and self.aBoujé == False and yOr > 6:
                    possibilités.append((yOr+2,xOr))
            for i in [1,-1]:
                if plateau1.plateau[yOr+1][xOr+i].estVide() == False and plateau1.plateau[yOr+1][xOr+i].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr+1,xOr+i))
        return possibilités
        

class tour(pièce): #pièce marchant, ne plus toucher sauf pour ajout
    def __init__(self, x, y,couleur):
        pièce.__init__(self,x,y,couleur)
    
    def symbole(self):
        if self.couleur == 'blanc':
            return '♜'
        else:
            return '♖'
    
    def avoirType(self):
        return tour

    def mouvement(self, xOr, yOr):
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
        return possibilités

class fou(pièce): #pièce marchant, ne plus toucher sauf pour ajout
    def __init__(self, x, y,couleur):
        pièce.__init__(self,x,y,couleur)
    
    def symbole(self):
        if self.couleur == 'blanc':
            return '♝'
        else:
            return '♗'
    
    def avoirType(self):
        return fou

    def mouvement(self, xOr, yOr):
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
        for i in range(xOr if xOr<=yOr else yOr): #vérification NO
            if plateau1.plateau[yOr-i-1][xOr-i-1].estVide() == True:
                possibilités.append((yOr-i-1,xOr-i-1))
            elif plateau1.plateau[yOr-i-1][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((yOr-i-1,xOr-i-1))
                break
            else:
                break
        for i in range(xOr if xOr<=7-yOr else 7-yOr): #vérification SO
            if plateau1.plateau[yOr+i+1][xOr-i-1].estVide() == True:
                possibilités.append((yOr+i+1,xOr-i-1))
            elif plateau1.plateau[yOr+i+1][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((yOr+i+1,xOr-i-1))
                break
            else:
                break
        return possibilités

class cavalier(pièce): #pièce marchant, ne plus toucher sauf pour ajout
    def __init__(self, x, y,couleur):
        pièce.__init__(self,x,y,couleur)
    
    def symbole(self):
        if self.couleur == 'blanc':
            return '♞'
        else:
            return '♘'
    
    def avoirType(self):
        return cavalier
        
    def mouvement(self, xOr, yOr):
        possibilités = []
        mouvements = [(-1,-2),(-1,2),(-2,1),(2,1),(1,2),(1,-2),(2,-1),(-2,-1)]
        for i in mouvements: #vérification SE
            if 7>= yOr+i[0] >= 0 and 7>= xOr+i[1] >= 0:
                if plateau1.plateau[yOr+i[0]][xOr+i[1]].estVide() == True or plateau1.plateau[yOr+i[0]][xOr+i[1]].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr+i[0],xOr+i[1]))
        return possibilités

class reine(pièce): #pièce marchant, ne plus toucher sauf pour ajout
    def __init__(self, x, y,couleur):
        pièce.__init__(self,x,y,couleur)

    def symbole(self):
        if self.couleur == 'blanc':
            return '♛'
        else:
            return '♕'
    
    def avoirType(self):
        return reine
        
    def mouvement(self, xOr, yOr): #possible d'optimiser largement
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
        for i in range(xOr if xOr<=yOr else yOr): #vérification NO
            if plateau1.plateau[yOr-i-1][xOr-i-1].estVide() == True:
                possibilités.append((yOr-i-1,xOr-i-1))
            elif plateau1.plateau[yOr-i-1][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((yOr-i-1,xOr-i-1))
                break
            else:
                break
        for i in range(xOr if xOr<=7-yOr else 7-yOr): #vérification SO
            if plateau1.plateau[yOr+i+1][xOr-i-1].estVide() == True:
                possibilités.append((yOr+i+1,xOr-i-1))
            elif plateau1.plateau[yOr+i+1][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
                possibilités.append((yOr+i+1,xOr-i-1))
                break
            else:
                break
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
        return possibilités

class roi(pièce): #pièce marchant, ne plus toucher sauf pour ajout
    def __init__(self, x, y,couleur):
        pièce.__init__(self,x,y,couleur)

    def symbole(self):
        if self.couleur == 'blanc':
            return '♚'
        else:
            return '♔'
    
    def avoirType(self):
        return roi
    
    def mouvement(self, xOr, yOr): ###Ajouter vérification case vide
        possibilités = []
        mouvements = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        for i in mouvements: #vérification SE
            if 7>= yOr+i[0] >= 0 and 7>= xOr+i[1] >= 0:
                if plateau1.plateau[yOr+i[0]][xOr+i[1]].estVide() == True or plateau1.plateau[yOr+i[0]][xOr+i[1]].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr+i[0],xOr+i[1]))
        return possibilités

class plateau:
    def __init__(self):
        self.grille = []
        for y in range(1,9):
            ligne = []
            for x in range(1,9):
                nouvelle_case = case(x,y)
                ligne.append(nouvelle_case)
            self.grille.append(ligne)
        
    def placement_debut(self):
        for i in range(8):
            self.grille[0][i].modifContenu([tour(i,0,'noir'),cavalier(i,0,'noir'),fou(i,0,'noir'),reine(i,0,'noir'),roi(i,0,'noir'),fou(i,0,'noir'),cavalier(i,0,'noir'),tour(i,0,'noir')][i])
            self.grille[7][i].modifContenu([tour(i,7,'blanc'),cavalier(i,7,'blanc'),fou(i,7,'blanc'),reine(i,7,'blanc'),roi(i,7,'blanc'),fou(i,7,'blanc'),cavalier(i,7,'blanc'),tour(i,7,'blanc')][i])
            self.grille[1][i].modifContenu(pion(i,1,'noir'))
            self.grille[6][i].modifContenu(pion(i,6,'blanc'))

    def get_case(self,mouseX,mouseY):
        decalage_x = (fenetrePrincipale.get_size()[0] - (imagePlateau.get_width()/10*8)) / 2
        decalage_y = (fenetrePrincipale.get_size()[1] - (imagePlateau.get_height()/10*8)) / 2
        posXforCase = mouseX-decalage_x
        posYforCase = mouseY-decalage_y
        print(posXforCase//(imagePlateau.get_width()/10),posYforCase//(imagePlateau.get_height()/10))

 
def effectuerMouvement(xOr,yOr,xDest,yDest,echec = False, joueur = 'blanc', coupPrécédentEffectué = True):
    '''Transfome le format d'échec normal (case en bas à droite = a1) en format prog (case en bas à droite = (y=7, x=0))
       Puis envoie requète de mouvement à l'objet correspondant
    '''
    print(' ')
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
            assert plateau1.plateau[yOr][xOr].couleurContenuDifferentVerif(joueur) == False, "Vous ne pouvez pas jouer une pièce qui ne vous appartient pas"
            pièceParam = plateau1.getParam(yOr,xOr)
            possibilités = pièceParam[0].mouvement(xOr,yOr)
            try:
                print(yDest,xDest, possibilités)
                assert (yDest,xDest) in possibilités, 'Mouvement impossible'
                plateau1.plateau[yOr][xOr].modifContenu(None)
                if pièceParam[0].avoirType() != pion:
                    plateau1.plateau[yDest][xDest].modifContenu(pièceParam[0].avoirType()(xDest,yDest,pièceParam[0].avoirCouleur()))
                else : 
                    plateau1.plateau[yDest][xDest].modifContenu(pièceParam[0].avoirType()(xDest,yDest,pièceParam[0].avoirCouleur(),True))
                #test pour echecs :
                echecParam = plateau1.getParam(yDest,xDest)
                possibilités = echecParam[0].mouvement(xDest,yDest)
                for piece in possibilités:
                    pieceParam = plateau1.getParam(piece[0],piece[1])
                    if pieceParam[0] != None:
                        if pieceParam[0].avoirType() == roi:
                            if pieceParam[0].avoirCouleur() != plateau1.getParam(yDest,xDest)[0].avoirCouleur():
                                print("echec")
                                echec = True
                                mouvementsRoi = pieceParam[0].mouvement(pieceParam[3],pieceParam[2])
                                print(mouvementsRoi) #a finir (mat)
            except AssertionError as error:
                print(error)
                coupPrécédentEffectué = False
        except AssertionError as error:
            print(error)    
            coupPrécédentEffectué = False     
    except AssertionError as error:
        print(error)
        coupPrécédentEffectué = False
    finally:
        plateau1.afficherPlateau()
        print(f'Coup précédent éffectué : {coupPrécédentEffectué}')
        if coupPrécédentEffectué == True:
            joueur = "blanc" if joueur == "noir" else "noir"
        print(f"C'est le tour des {joueur}s")
        effectuerMouvement(input("Lettre correspondant à la coordonée x de la pièce : "),int(input("Chiffre correspondant à la coordonée y de la pièce : ")),input("Lettre correspondant à la coordonée x de la destination : "),int(input("Chiffre correspondant à la coordonée y de la destination : ")), echec, joueur)

def centrer(object):
    return fenetrePrincipale.get_size()[0]/2-object.get_size()[0]/2,fenetrePrincipale.get_size()[1]/2-object.get_size()[1]/2

def lancer_jeu():
    garderOuvert = True
    while garderOuvert == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('Fermeture de la fenetre')
                    garderOuvert = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                plateau1.get_case(x,y)

        #Placement des images de fond
        fenetrePrincipale.blit(imageFondForet, centrer(imageFondForet))
        fenetrePrincipale.blit(imageShop, (fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]-20,centrer(imageShop)[1]))
        fenetrePrincipale.blit(imagePlateau, centrer(imagePlateau))
        objetFutur = pygame.draw.rect(imageFondForet, "black",(0+imageShop.get_size()[0]+20-fenetrePrincipale.get_size()[0]/4,centrer(imageShop)[1],fenetrePrincipale.get_size()[0]/4, fenetrePrincipale.get_size()[1]*0.90))
        
        #Placement des images des pièces
        for ligne in plateau1.grille:
            for piece in ligne:
                if piece.contenu!=None:
                    piece.contenu.affichage()
        
        pygame.display.flip()

plateau1 = plateau()
plateau1.placement_debut()
lancer_jeu()

print('''C'est le tour des blancs''')