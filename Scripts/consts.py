import pygame

pygame.init()
fenetrePrincipale = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#Fonds
imageFondForet = pygame.image.load("../img/fonds/Fond_foret.png").convert()
imageShop = pygame.image.load("../img/gui/interface_shop.png").convert()
imagePlateau = pygame.image.load("../img/gui/plateau.png").convert()

#Items
imagePionB = pygame.image.load("../img/items/pion_B.png").convert_alpha()
imagePionN = pygame.image.load("../img/items/pion_N.png").convert_alpha()
imageFouB = pygame.image.load("../img/items/fou_B.png").convert_alpha()
imageFouN = pygame.image.load("../img/items/fou_N.png").convert_alpha()
imageCavalierB = pygame.image.load("../img/items/cavalier_B.png").convert_alpha()
imageCavalierN = pygame.image.load("../img/items/cavalier_N.png").convert_alpha()
imageTourB = pygame.image.load("../img/items/tour_B.png").convert_alpha()
imageTourN = pygame.image.load("../img/items/tour_N.png").convert_alpha()
imageReineB = pygame.image.load("../img/items/reine_B.png").convert_alpha()
imageReineN = pygame.image.load("../img/items/reine_N.png").convert_alpha()
imageRoiB = pygame.image.load("../img/items/roi_B.png").convert_alpha()
imageRoiN = pygame.image.load("../img/items/roi_N.png").convert_alpha()