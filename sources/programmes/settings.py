import pygame
from Sound import Sound
from consts import imageShop,bouton_retour_img,bouton_musique_img
# Création des boutons
def settings(fenetre,Bouton,boutons,settingsOpenFctn,musique):
    global bouton_retour_img,bouton_musique_img
    
    def musiqueOnOff(self,musique):
        musique = False if musique == True else True
        print('musique mise sur ',musique)
        return musique

    fenetre_settings_img = pygame.transform.scale(imageShop,(fenetre.get_width()*0.8,fenetre.get_height()*0.8))

    bouton_retour_img = pygame.transform.scale(bouton_retour_img, (fenetre_settings_img.get_width()*0.3,fenetre_settings_img.get_width()*0.15))
    bouton_retour = Bouton(fenetre.get_width()/2-bouton_retour_img.get_width()/2, fenetre.get_height()/2-bouton_retour_img.get_height(), bouton_retour_img,settingsOpenFctn)
    boutons.append(bouton_retour)

    bouton_musique_img = pygame.transform.scale(bouton_musique_img,(fenetre_settings_img.get_width()*0.3,fenetre_settings_img.get_width()*0.15))
    bouton_musique = Bouton(fenetre.get_width()/2-bouton_musique_img.get_width()/2, fenetre.get_height()/2, bouton_musique_img, musiqueOnOff, musique)

    boutons.append(bouton_musique)
    

    fenetre.blit(fenetre_settings_img,(fenetre.get_width()/2-fenetre_settings_img.get_width()/2,fenetre.get_height()/2-fenetre_settings_img.get_height()/2))