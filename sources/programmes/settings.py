import pygame
from consts import imageShop

def settings(fenetre,settingsVar):
    fenetre_settings_img = pygame.transform.scale(imageShop,(fenetre.get_width()*0.8,fenetre.get_height()*0.8))
    fenetre.blit(fenetre_settings_img,(fenetre.get_width()/2-fenetre_settings_img.get_width()/2,fenetre.get_height()/2-fenetre_settings_img.get_height()/2))
