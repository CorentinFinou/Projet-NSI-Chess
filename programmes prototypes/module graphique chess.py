import pygame

pygame.init()

fenetrePrincipale = pygame.display.set_mode((960,540), pygame.RESIZABLE)
def centrer(object):
    return fenetrePrincipale.get_size()[0]/2-object.get_size()[0]/2,fenetrePrincipale.get_size()[1]/2-object.get_size()[1]/2


imageFondForet = pygame.image.load("img/fonds/Fond_foret.png").convert()
imageFondForet = pygame.transform.scale(imageFondForet,(fenetrePrincipale.get_size()[0], fenetrePrincipale.get_size()[1]))

imageShop = pygame.image.load("img/gui/interface_shop.png").convert()
imageShop = pygame.transform.scale(imageShop, (fenetrePrincipale.get_size()[0]/4, fenetrePrincipale.get_size()[1]*0.90))



imagePlateau = pygame.image.load("img/gui/plateau.png").convert()
imagePlateau = pygame.transform.scale(imagePlateau, (fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]-100 if fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]<fenetrePrincipale.get_size()[1] else fenetrePrincipale.get_size()[1]-100,fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]-100 if fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]<fenetrePrincipale.get_size()[1] else fenetrePrincipale.get_size()[1]-100))


garderOuvert = True
while garderOuvert == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('Fermeture de la fenetre')
                garderOuvert = False
        if event.type == pygame.WINDOWRESIZED:
            imageFondForet = pygame.transform.scale(imageFondForet,(fenetrePrincipale.get_size()[0], fenetrePrincipale.get_size()[1]))
            imageShop = pygame.transform.scale(imageShop, (fenetrePrincipale.get_size()[0]/4, fenetrePrincipale.get_size()[1]*0.90))
            imagePlateau = pygame.transform.scale(imagePlateau, (fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]-100 if fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]<fenetrePrincipale.get_size()[1] else fenetrePrincipale.get_size()[1]-100,fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]-100 if fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]<fenetrePrincipale.get_size()[1] else fenetrePrincipale.get_size()[1]-100))
            print(f"Largeur : {fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]*2}, hauteur : {fenetrePrincipale.get_size()[1] }")

    fenetrePrincipale.blit(imageFondForet, centrer(imageFondForet))
    fenetrePrincipale.blit(imageShop, (fenetrePrincipale.get_size()[0]-imageShop.get_size()[0]-20,centrer(imageShop)[1]))
    fenetrePrincipale.blit(imagePlateau, centrer(imagePlateau))
    objetFutur = pygame.draw.rect(imageFondForet, "black",(0+imageShop.get_size()[0]+20-fenetrePrincipale.get_size()[0]/4,centrer(imageShop)[1],fenetrePrincipale.get_size()[0]/4, fenetrePrincipale.get_size()[1]*0.90))
    pygame.display.flip()
    
    

pygame.quit()
