import pygame
from consts import imageShop,bouton_settings_img

# Création des boutons
def settings(fenetre,boutons,Bouton,action):
    global bouton_settings_img
    fenetre_settings_img = pygame.transform.scale(imageShop,(fenetre.get_width()*0.8,fenetre.get_height()*0.8))
    bouton_settings_img = pygame.transform.scale(bouton_settings_img, (fenetre_settings_img.get_width()*0.3,fenetre_settings_img.get_width()*0.15))
    bouton_settings = Bouton(fenetre.get_width()/2-bouton_settings_img.get_width()/2, fenetre.get_height()/2-bouton_settings_img.get_height()/2, bouton_settings_img, action)
    boutons.append(bouton_settings)
    fenetre.blit(fenetre_settings_img,(fenetre.get_width()/2-fenetre_settings_img.get_width()/2,fenetre.get_height()/2-fenetre_settings_img.get_height()/2))