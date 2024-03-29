import pygame

def menu():
    #import images avec noms correspondant aux noms donnés par paul aux variables du programme
    from consts import imageFondForet as fond_menu, bouton_jouer_img,bouton_quitter_img 

    # Initialisation de Pygame
    pygame.init()

    # Paramètres de la fenêtre
    fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Menu")

    # Redimensionnement des images
    fond_menu = pygame.transform.scale(fond_menu, fenetre.get_size())
    bouton_jouer_img = pygame.transform.scale(bouton_jouer_img, (fenetre.get_width()/4, fenetre.get_width()/4/2))
    bouton_quitter_img = pygame.transform.scale(bouton_quitter_img, (fenetre.get_width()/4, fenetre.get_width()/4/2))



    # Classe pour les boutons
    class Bouton:
        def __init__(self, x, y, image, action):
            self.rect = image.get_rect()
            self.rect.topleft = (x, y)
            self.image = image
            self.action = action
            self.state = False

        def dessiner(self):
            fenetre.blit(self.image, self.rect)

        def verifier_clic(self, pos):
            if self.rect.collidepoint(pos):
                self.action(self)

    # Fonctions pour les actions des boutons
    def action_jouer(self):
        self.state = True

    def action_quitter(self):
        pygame.quit()
        quit()

    # Création des boutons
    bouton_jouer = Bouton(fenetre.get_width()/2-bouton_jouer_img.get_width()/2, fenetre.get_height()/2-bouton_jouer_img.get_height(), bouton_jouer_img, action_jouer)
    bouton_quitter = Bouton(fenetre.get_width()/2-bouton_quitter_img.get_width()/2, fenetre.get_height()/2, bouton_quitter_img, action_quitter)
    boutons = [bouton_jouer, bouton_quitter]

    # Boucle principale
    def lancer():
        en_cours = True
        while en_cours:
            en_cours = True if bouton_jouer.state == False else False
            fenetre.blit(fond_menu, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            en_cours = False   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        for bouton in boutons:
                            bouton.verifier_clic(pos)


            for bouton in boutons:
                bouton.dessiner()

            pygame.display.flip()
    lancer()