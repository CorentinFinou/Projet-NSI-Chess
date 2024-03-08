import pygame,consts
def jeu():
    pygame.init()
    fenetrePrincipale = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    imageFondForet = pygame.transform.scale(consts.imageFondForet,(fenetrePrincipale.get_size()[0], fenetrePrincipale.get_size()[1]))
    imageShop = pygame.transform.scale(consts.imageShop, (fenetrePrincipale.get_size()[0]/4, fenetrePrincipale.get_size()[1]*0.60))
    imagePlateau = pygame.transform.scale(consts.imagePlateau, (fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]*2-80,fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]*2-80))
    carteTestSprite = pygame.sprite.Sprite()

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
                self.sprite = None
                self.moveable = True
                self.effets = []
                self.effetsSprites = {}

            except AssertionError as error:
                raise error
            except TypeError:
                raise TypeError('Les coordonnées doivent être des int')
        
        def avoirPosition(self):
            return self.x,self.y

        def avoirCouleur(self):
            return self.couleur

        def bougerImage(self,destX,destY,groupe):
            #print(self.position,groupe,self,self.sprite) #sprite dans aucun groupe la 2ème fois
            self.x = destX
            self.y = destY
            self.affichage(groupe)

        def affichage(self,groupe):
            if self.sprite != None:
                groupe.remove(self.sprite)
            self.sprite = pygame.sprite.Sprite()
            pièces = [pion,tour,fou,cavalier,reine,roi]
            if self.couleur == "blanc":
                self.sprite.image = pygame.transform.scale(imgsPiecesB[pièces.index(self.avoirType())], (int(imagePlateau.get_size()[0] / 10), int(imagePlateau.get_size()[0] / 10)))
            else:
                self.sprite.image = pygame.transform.scale(imgsPiecesN[pièces.index(self.avoirType())], (int(imagePlateau.get_size()[0] / 10), int(imagePlateau.get_size()[0] / 10)))
            self.sprite.rect = self.sprite.image.get_rect()
            self.position = centrer_piece(self.x,self.y,self.sprite.image)
            self.sprite.rect.topleft = (self.position[0],self.position[1])
            groupe.add(self.sprite)

        def affichageEffet(self,effet,effetImg,group):
            if effet in self.effets:
                self.effets.remove(effet)
                del self.effetsSprites[effet]
            else:
                self.effets.append(effet)
                self.effetsSprites[effet] = pygame.sprite.Sprite()
                self.effetsSprites[effet].image = pygame.transform.scale(effetImg,(self.sprite.image.get_width()/3,self.sprite.image.get_height()/3))
                self.effetsSprites[effet].rect = self.effetsSprites[effet].image.get_rect()
                self.effetsSprites[effet].rect.topright = self.sprite.rect.topright
                group.add(self.effetsSprites[effet])
                
                

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
            if 0<xOr<7:
                diagTest = [1,-1]
            elif 0<xOr:
                diagTest = [-1]
            else:
                diagTest = [1]
            if self.avoirCouleur() ==  'blanc' and yOr > 0:
                if plateau1.grille[yOr-1][xOr].estVide() == True:
                    possibilités.append((yOr-1,xOr))
                    if plateau1.grille[yOr-2][xOr].estVide() == True and self.aBoujé == False and yOr > 1:
                        possibilités.append((yOr-2,xOr))
                for i in diagTest:
                    if plateau1.grille[yOr-1][xOr+i].estVide() == False and plateau1.grille[yOr-1][xOr+i].couleurContenuDifferentVerif(self.couleur)==True:
                        possibilités.append((yOr-1,xOr+i))
            if self.avoirCouleur() == 'noir' and yOr < 7:
                if plateau1.grille[yOr+1][xOr].estVide() == True:
                    possibilités.append((yOr+1,xOr))
                    if plateau1.grille[yOr+2][xOr].estVide() == True and self.aBoujé == False and yOr < 6:
                        possibilités.append((yOr+2,xOr))
                for i in diagTest:
                    if plateau1.grille[yOr+1][xOr+i].estVide() == False and plateau1.grille[yOr+1][xOr+i].couleurContenuDifferentVerif(self.couleur)==True:
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
                if plateau1.grille[yOr+i+1][xOr].estVide() == True:
                    possibilités.append((i+yOr+1,xOr))
                elif plateau1.grille[yOr+i+1][xOr].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((i+yOr+1,xOr))
                    break
                else:
                    break
            for i in range(7-xOr): #vérification vers la droite
                if plateau1.grille[yOr][xOr+i+1].estVide() == True:
                    possibilités.append((yOr,i+xOr+1))
                elif plateau1.grille[yOr][xOr+i+1].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr,xOr+i+1))
                else:
                    break
            for i in range(yOr): #vérification vers le haut
                if plateau1.grille[yOr-i-1][xOr].estVide() == True:
                    possibilités.append((yOr-i-1,xOr))
                elif plateau1.grille[yOr-i-1][xOr].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr-i-1,xOr))
                    break
                else:
                    break
            for i in range(xOr): #vérification vers la gauche
                if plateau1.grille[yOr][xOr-i-1].estVide() == True:
                    possibilités.append((yOr,xOr-i-1))
                elif plateau1.grille[yOr][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
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
                if plateau1.grille[yOr+i+1][xOr+i+1].estVide() == True:
                    possibilités.append((yOr+i+1,xOr+i+1))
                elif plateau1.grille[yOr+i+1][xOr+i+1].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((i+yOr+1,xOr+i+1))
                    break
                else:
                    break
            for i in range(yOr if yOr<7-xOr else 7-xOr): #vérification NE
                if plateau1.grille[yOr-i-1][xOr+i+1].estVide() == True:
                    possibilités.append((yOr-i-1,xOr+i+1))
                elif plateau1.grille[yOr-i-1][xOr+i+1].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr-1-i,xOr+i+1))
                    break
                else:
                    break
            for i in range(xOr if xOr<=yOr else yOr): #vérification NO
                if plateau1.grille[yOr-i-1][xOr-i-1].estVide() == True:
                    possibilités.append((yOr-i-1,xOr-i-1))
                elif plateau1.grille[yOr-i-1][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr-i-1,xOr-i-1))
                    break
                else:
                    break
            for i in range(xOr if xOr<=7-yOr else 7-yOr): #vérification SO
                if plateau1.grille[yOr+i+1][xOr-i-1].estVide() == True:
                    possibilités.append((yOr+i+1,xOr-i-1))
                elif plateau1.grille[yOr+i+1][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
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
                    if plateau1.grille[yOr+i[0]][xOr+i[1]].estVide() == True or plateau1.grille[yOr+i[0]][xOr+i[1]].couleurContenuDifferentVerif(self.couleur)==True:
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
                if plateau1.grille[yOr+i+1][xOr+i+1].estVide() == True:
                    possibilités.append((yOr+i+1,xOr+i+1))
                elif plateau1.grille[yOr+i+1][xOr+i+1].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((i+yOr+1,xOr+i+1))
                    break
                else:
                    break
            for i in range(yOr if yOr<7-xOr else 7-xOr): #vérification NE
                if plateau1.grille[yOr-i-1][xOr+i+1].estVide() == True:
                    possibilités.append((yOr-i-1,xOr+i+1))
                elif plateau1.grille[yOr-i-1][xOr+i+1].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr-1-i,xOr+i+1))
                    break
                else:
                    break
            for i in range(xOr if xOr<=yOr else yOr): #vérification NO
                if plateau1.grille[yOr-i-1][xOr-i-1].estVide() == True:
                    possibilités.append((yOr-i-1,xOr-i-1))
                elif plateau1.grille[yOr-i-1][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr-i-1,xOr-i-1))
                    break
                else:
                    break
            for i in range(xOr if xOr<=7-yOr else 7-yOr): #vérification SO
                if plateau1.grille[yOr+i+1][xOr-i-1].estVide() == True:
                    possibilités.append((yOr+i+1,xOr-i-1))
                elif plateau1.grille[yOr+i+1][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr+i+1,xOr-i-1))
                    break
                else:
                    break
            for i in range(7-yOr): #vérification vers le bas
                if plateau1.grille[yOr+i+1][xOr].estVide() == True:
                    possibilités.append((i+yOr+1,xOr))
                elif plateau1.grille[yOr+i+1][xOr].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((i+yOr+1,xOr))
                    break
                else:
                    break
            for i in range(7-xOr): #vérification vers la droite
                if plateau1.grille[yOr][xOr+i+1].estVide() == True:
                    possibilités.append((yOr,i+xOr+1))
                elif plateau1.grille[yOr][xOr+i+1].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr,xOr+i+1))
                else:
                    break
            for i in range(yOr): #vérification vers le haut
                if plateau1.grille[yOr-i-1][xOr].estVide() == True:
                    possibilités.append((yOr-i-1,xOr))
                elif plateau1.grille[yOr-i-1][xOr].couleurContenuDifferentVerif(self.couleur)==True:
                    possibilités.append((yOr-i-1,xOr))
                    break
                else:
                    break
            for i in range(xOr): #vérification vers la gauche
                if plateau1.grille[yOr][xOr-i-1].estVide() == True:
                    possibilités.append((yOr,xOr-i-1))
                elif plateau1.grille[yOr][xOr-i-1].couleurContenuDifferentVerif(self.couleur)==True:
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
                    if plateau1.grille[yOr+i[0]][xOr+i[1]].estVide() == True or plateau1.grille[yOr+i[0]][xOr+i[1]].couleurContenuDifferentVerif(self.couleur)==True:
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

        def get_object(self,y,x):
            return self.grille[int(y)][int(x)].getParamCase()[0]

        def get_case(self,mouseX,mouseY):
            decalage_x = (fenetrePrincipale.get_size()[0] - (imagePlateau.get_width()/10*8)) / 2
            decalage_y = (fenetrePrincipale.get_size()[1] - (imagePlateau.get_height()/10*8)) / 2
            posXforCase = mouseX-decalage_x
            posYforCase = mouseY-decalage_y
            return posXforCase//(imagePlateau.get_width()/10),posYforCase//(imagePlateau.get_height()/10)

    class carte:
            def __init__(self, ordrePile, type, groupe):
                self.ordrePile = ordrePile
                self.sprite = pygame.sprite.Sprite()
                self.sprite.image = None
                self.type = type
                self.position = None
                self.groupe = groupe
                self.selectionnee = False
                self.jouee = False
  
            def avoirType(self):
                return self.type
            
            def definirSprite(self):
                listeCartes = {'gel': consts.imageCarteGel,
                               'intagibilité' : 'const.imageIntangibiltié',
                               'immolation' : 'consts.imageImmolation',#a faire en classe si besoin dans le futur
                               'invocation' : consts.imageCarteInvocation}
                if self.sprite.image == None:
                    self.sprite.image = pygame.transform.scale(listeCartes[self.type], (fenetrePrincipale.get_size()[0]/10,fenetrePrincipale.get_size()[1]/3))
                    self.sprite.imageInitiale = self.sprite.image                    
                    

            def affichage(self):
                self.definirSprite()
                if not self.position:
                    self.position = (fenetrePrincipale.get_width()-imageShop.get_width()/2 - self.sprite.image.get_width()/2 -20, fenetrePrincipale.get_height()-self.sprite.image.get_height()-20)
                self.origin = self.position
                self.sprite.rect = self.sprite.image.get_rect()
                self.sprite.rect.topleft = self.position
                self.groupe.add(self.sprite)
            
            def modifierPosition(self, newPos, valid = True):
                self.groupe.remove(self.sprite)
                if valid:
                    self.position = newPos[0]-self.sprite.image.get_width()/2,newPos[1]-self.sprite.image.get_height()/2
                else:
                    self.position = None
                self.affichage()

            def verifierAction(self,joueur,groupeEffet):
                case = plateau1.get_case(self.position[0]+self.sprite.image.get_width()/2,self.position[1]+self.sprite.image.get_height()/2)
                if case[0]<0 or case[0]>7 or case[1]<0 or case[1]>7:
                    self.modifierPosition(self.origin, False)
                else:
                    self.action(case,joueur,groupeEffet)

            def action(self,case,joueur,groupeEffet):
                if plateau1.grille[int(case[1])][int(case[0])].estVide() == False and plateau1.get_object(int(case[1]),int(case[0])).couleur != joueur:
                    target = plateau1.get_object(int(case[1]),int(case[0]))
                    if self.avoirType() == 'gel':
                        target.moveable = False
                        target.affichageEffet('gel',consts.effetGelImg,groupeEffet)
                        self.sprite.kill()
                        self.jouee = True
                else:
                    self.modifierPosition(self.origin, False)



    def effectuerMouvement(piece,xDest,yDest,groupe, joueur = 'blanc',mat = False, coupPrécédentEffectué = True):
        xOr,yOr = piece.avoirPosition()
        try:
            assert plateau1.grille[yOr][xOr].estVide() == False, "Il n'y a pas de pièce sur cette case"
            assert plateau1.grille[yOr][xOr].couleurContenuDifferentVerif(joueur) == False, "Vous ne pouvez pas jouer une pièce qui ne vous appartient pas"
            piece = plateau1.get_object(yOr,xOr)
            possibilités = piece.mouvement(xOr,yOr)
            try:
                assert (yDest,xDest) in possibilités, 'Mouvement impossible'
                pieceMangée = plateau1.grille[yDest][xDest].getParamCase()[0]
                if piece.avoirType() != pion:
                    plateau1.grille[yDest][xDest].modifContenu(plateau1.grille[yOr][xOr].contenu)
                else :
                    plateau1.grille[yDest][xDest].modifContenu(plateau1.grille[yOr][xOr].contenu)
                    plateau1.grille[yDest][xDest].contenu.aBoujé = True
                plateau1.grille[yOr][xOr].modifContenu(None)
                piece.bougerImage(xDest,yDest,groupe)
                #test pour mat :
                groupe.remove(pieceMangée.sprite)
                if pieceMangée.avoirType() == roi:
                    mat = True
                    print(f'Partie terminée ! Les {joueur}s ont gagné !')
                
            except AssertionError as error:
                print(error)
                print(possibilités)
                coupPrécédentEffectué = False
        except AssertionError as error:
            print(error) 
            coupPrécédentEffectué = False
        finally:
            #print(f'Coup précédent éffectué : {coupPrécédentEffectué}')
            if coupPrécédentEffectué == True :
                joueur = "blanc" if joueur == "noir" else "noir"
            return joueur,coupPrécédentEffectué,mat

    def centrer(object):
        return fenetrePrincipale.get_size()[0]/2-object.get_size()[0]/2,fenetrePrincipale.get_size()[1]/2-object.get_size()[1]/2

    def lancer_jeu(mat = False):
        garderOuvert = True
        spritesPiecesGroupe = pygame.sprite.Group()
        spritesCartesGroup = pygame.sprite.Group()
        spritesEffetsGroup = pygame.sprite.Group()
        cartes = []
        cartesJouées = []
        joueur = 'blanc'
        #print(f" \nC'est le tour des {joueur}s")
        for ligne in plateau1.grille:
            for piece in ligne:
                if piece.contenu!=None:
                    piece.contenu.affichage(spritesPiecesGroupe)
        while garderOuvert == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        garderOuvert = False  
                    if event.key == pygame.K_a and len(cartes)<=2:
                        carteTest = carte(1,'gel'if len(cartes)%2==1 else 'invocation', spritesCartesGroup)
                        cartes.append(carteTest)   
                        carteTest.definirSprite()
                        carteTest.affichage() 
                        for i in range(len(cartes)):
                            c = cartes[i]
                            spritesCartesGroup.remove(c.sprite)
                            if len(cartes) == 1:
                                pass
                            else:
                                c = cartes[i]
                                if c in cartes[:len(cartes)-1]:
                                    c.position = c.position[0]-(c.sprite.image.get_width()/2)*(len(cartes)-1),c.position[1]
                                else:
                                    c.position = c.position[0]+(c.sprite.image.get_width()/2),c.position[1]
                            c.sprite.image = pygame.transform.scale(c.sprite.imageInitiale,(c.sprite.imageInitiale.get_width()/(1.1**len(cartes)),c.sprite.imageInitiale.get_height()/(1.1**len(cartes))))
                                #c.sprite.rect = c.sprite.image.get_rect()
                            c.affichage()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0<=plateau1.get_case(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[0]<=7 and 0<=plateau1.get_case(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[1]<=7:
                        xOr,yOr = plateau1.get_case(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                        pieceABouger = plateau1.get_object(yOr,xOr)
                        if pieceABouger != None and pieceABouger.avoirCouleur() == joueur and pieceABouger.moveable == True:
                            deuxiemeClic = False
                            while deuxiemeClic == False:
                                if pygame.event.wait().type == pygame.MOUSEBUTTONDOWN:
                                    deuxiemeClic = True
                                    xDest,yDest = plateau1.get_case(int(pygame.mouse.get_pos()[0]),pygame.mouse.get_pos()[1])
                                    xDest,yDest = int(xDest),int(yDest)
                            joueur,coupEffectué,mat = effectuerMouvement(pieceABouger,xDest,yDest,spritesPiecesGroupe,joueur,mat)
                            if coupEffectué == True and mat == False:
                                pass
                                #print(f" \nC'est le tour des {joueur}s")
                    if event.button == 1 :
                        for e in cartes:
                            if e.sprite.rect.collidepoint(pygame.mouse.get_pos()):
                                carteTest.selectionnee = True
                elif event.type == pygame.MOUSEMOTION:
                    if cartes != [] and carteTest.selectionnee:
                        newPos = pygame.mouse.get_pos()
                        carteTest.modifierPosition(newPos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if cartes != [] and carteTest.selectionnee:
                        carteTest.selectionnee = False
                        carteTest.verifierAction(joueur,spritesEffetsGroup)
                        if carteTest.jouee == True:
                            cartes.remove(carteTest)
                            cartesJouées.append(carteTest)
                            del carteTest
            if mat == True:
                garderOuvert = False

            #Placement des images de fond
            fenetrePrincipale.blit(imageFondForet, centrer(imageFondForet))
            fenetrePrincipale.blit(imageShop, (fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]-20,centrer(imageShop)[1]-fenetrePrincipale.get_size()[1]/3))
            fenetrePrincipale.blit(imagePlateau, centrer(imagePlateau))
            objetFutur = pygame.draw.rect(imageFondForet, "black",(imageShop.get_size()[0]+20-fenetrePrincipale.get_size()[0]/4,(fenetrePrincipale.get_size()[1]*0.10)//2,fenetrePrincipale.get_size()[0]/4, fenetrePrincipale.get_size()[1]*0.90))
            
            

            #Placement des images des pièces
            spritesPiecesGroupe.draw(fenetrePrincipale)
            spritesPiecesGroupe.update()
            spritesCartesGroup.draw(fenetrePrincipale)
            spritesCartesGroup.update()
            spritesEffetsGroup.draw(fenetrePrincipale)
            spritesEffetsGroup.update()
            pygame.display.flip()

    plateau1 = plateau()
    plateau1.placement_debut()
    lancer_jeu()
