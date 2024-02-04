import pygame

pygame.init()

fenetrePrincipale = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
def centrer(object):
    return fenetrePrincipale.get_size()[0]/2-object.get_size()[0]/2,fenetrePrincipale.get_size()[1]/2-object.get_size()[1]/2


imageFondForet = pygame.image.load("../img/fonds/Fond_foret.png").convert()
imageFondForet = pygame.transform.scale(imageFondForet,(fenetrePrincipale.get_size()[0], fenetrePrincipale.get_size()[1]))

imageShop = pygame.image.load("../img/gui/interface_shop.png").convert()
imageShop = pygame.transform.scale(imageShop, (fenetrePrincipale.get_size()[0]/4, fenetrePrincipale.get_size()[1]*0.90))

imagePlateau = pygame.image.load("../img/gui/plateau.png").convert()
imagePlateau = pygame.transform.scale(imagePlateau, (fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]*2-80,fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]*2-80))

class case:
    def __init__(self,x,y,contenu = None):
        self.x = x
        self.y = y
        self.contenu = contenu
        self.size = imagePlateau.get_size()[0]/10
    
    def draw_case(self,surface):
        self.visual = pygame.draw.rect(surface,"red",(self.x*self.size,self.y*self.size,self.size,self.size),1)

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
            
def drawGrid(surface,sizeX=1,sizeY=1):
    for y in range(1,sizeY):
        for x in range(1,sizeX):
            nouvelle_case = case(x,y)
            nouvelle_case.draw_case(surface)

garderOuvert = True
while garderOuvert == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('Fermeture de la fenetre')
                garderOuvert = False
    fenetrePrincipale.blit(imageFondForet, centrer(imageFondForet))
    fenetrePrincipale.blit(imageShop, (fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]-20,centrer(imageShop)[1]))
    fenetrePrincipale.blit(imagePlateau, centrer(imagePlateau))
    drawGrid(imagePlateau,9,9)
    objetFutur = pygame.draw.rect(imageFondForet, "black",(0+imageShop.get_size()[0]+20-fenetrePrincipale.get_size()[0]/4,centrer(imageShop)[1],fenetrePrincipale.get_size()[0]/4, fenetrePrincipale.get_size()[1]*0.90))
    pygame.display.flip()


    

pygame.quit()