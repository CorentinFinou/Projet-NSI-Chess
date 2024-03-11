import pygame
import os
from Sound import Sound

# Initialisation de Pygame
pygame.init()

Sound()
# Paramètres de la fenêtre
fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")

# Chargement des images
fond_menu = pygame.image.load('fond_menu.png').convert()
bouton_jouer_img = pygame.image.load('bouton_jouer.png').convert_alpha()
bouton_quitter_img = pygame.image.load('bouton_quitter.png').convert_alpha()

# Redimensionnement des images
fond_menu = pygame.transform.scale(fond_menu, fenetre.get_size())
bouton_jouer_img = pygame.transform.scale(bouton_jouer_img, (300, 150))
bouton_quitter_img = pygame.transform.scale(bouton_quitter_img, (300, 150))

# Police de caractères
police = pygame.font.Font(None, 40)

# Classe pour les boutons
class Bouton:
    def __init__(self, x, y, image, action):
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.image = image
        self.action = action

    def dessiner(self):
        fenetre.blit(self.image, self.rect)

    def verifier_clic(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

# Fonctions pour les actions des boutons
def action_jouer():
    os.system("python main.py")

def action_quitter():
    pygame.quit()
    quit()

# Création des boutons
bouton_jouer = Bouton(550, 300, bouton_jouer_img, action_jouer)
bouton_quitter = Bouton(550, 400, bouton_quitter_img, action_quitter)
boutons = [bouton_jouer, bouton_quitter]

# Boucle principale
en_cours = True
while en_cours:
    fenetre.blit(fond_menu, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                for bouton in boutons:
                    bouton.verifier_clic(pos)

    for bouton in boutons:
        bouton.dessiner()

    pygame.display.flip()

pygame.quit()
quit()
