import pygame

pygame.init()

fenetrePrincipale = pygame.display.set_mode((960,540), pygame.RESIZABLE)
def centrer(object):
    return fenetrePrincipale.get_size()[0]/2-object.get_size()[0]/2,fenetrePrincipale.get_size()[1]/2-object.get_size()[1]/2

'''
imagePlateau = pygame.image.load("img/plateau.png").convert()
imagePlateauTaille = (fenetrePrincipale.get_size()[0]/1.2-(fenetrePrincipale.get_size()[0]/1.2/10),fenetrePrincipale.get_size()[0]/1.2-(fenetrePrincipale.get_size()[0]/1.2/10))
imagePlateau = pygame.transform.scale(imagePlateau, imagePlateauTaille)
'''

'''
imageShop = pygame.image.load("img/interface_shop.png").convert()
imageShopTaille = (0,0)
imageShop = pygame.transform.scale(imageShop, imageShopTaille)
'''

garderOuvert = True
while garderOuvert == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('Fermeture de la fenetre')
                garderOuvert = False
        if event.type == pygame.WINDOWRESIZED:
            imagePlateauTaille = (fenetrePrincipale.get_size()[0]/1.2-(fenetrePrincipale.get_size()[0]/1.2-fenetrePrincipale.get_size()[1]),fenetrePrincipale.get_size()[0]/1.2-(fenetrePrincipale.get_size()[0]/1.2-fenetrePrincipale.get_size()[1]))
            imagePlateau = pygame.transform.scale(imagePlateau, imagePlateauTaille)

            imageShopTaille = (fenetrePrincipale.get_size()[0]/4.44, fenetrePrincipale.get_size()[1]/1.2)
            imageShop = pygame.transform.scale(imageShop, imageShopTaille)


    fenetrePrincipale.blit(imagePlateau,centrer(imagePlateau))
    fenetrePrincipale.blit(imageShop,(centrer(imageShop)[0]+fenetrePrincipale.get_size()[0]/2.70,centrer(imageShop)[1]))
    pygame.display.flip()
    
    

pygame.quit()