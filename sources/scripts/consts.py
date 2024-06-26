import pygame

pygame.init()
fenetrePrincipale = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#Fonds
imageFondForet = pygame.image.load("../img/fonds/Fond_foret.png").convert()
imageShop = pygame.image.load("../img/gui/interface_shop.png").convert_alpha()
imagePlateau = pygame.image.load("../img/gui/plateau.png").convert()

#items/pieces
imagePionB = pygame.image.load("../img/items/pieces/pion_B.png").convert_alpha()
imagePionN = pygame.image.load("../img/items/pieces/pion_N.png").convert_alpha()
imageFouB = pygame.image.load("../img/items/pieces/fou_B.png").convert_alpha()
imageFouN = pygame.image.load("../img/items/pieces/fou_N.png").convert_alpha()
imageCavalierB = pygame.image.load("../img/items/pieces/cavalier_B.png").convert_alpha()
imageCavalierN = pygame.image.load("../img/items/pieces/cavalier_N.png").convert_alpha()
imageTourB = pygame.image.load("../img/items/pieces/tour_B.png").convert_alpha()
imageTourN = pygame.image.load("../img/items/pieces/tour_N.png").convert_alpha()
imageReineB = pygame.image.load("../img/items/pieces/reine_B.png").convert_alpha()
imageReineN = pygame.image.load("../img/items/pieces/reine_N.png").convert_alpha()
imageRoiB = pygame.image.load("../img/items/pieces/roi_B.png").convert_alpha()
imageRoiN = pygame.image.load("../img/items/pieces/roi_N.png").convert_alpha()

#items/cards
imageCarteGel = pygame.image.load("../img/items/cards/gel_carte.png").convert_alpha()
imageCarteInvocation = pygame.image.load("../img/items/cards/invocation_carte.png").convert_alpha()
imagePileCartes = pygame.image.load("../img/items/cards/carte_pile.png").convert_alpha()
#items/buttons
bouton_jouer_img = pygame.image.load('../img/items/buttons/bouton_jouer.png').convert_alpha()
bouton_quitter_img = pygame.image.load('../img/items/buttons/bouton_quitter.png').convert_alpha()

#effects
effetGelImg = pygame.image.load('../img/effects/gel.png').convert_alpha()

#police de caractères
police = pygame.font.Font('../img/fonts/font.ttf', 16)