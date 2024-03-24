import pygame

class Sound:
    def __init__(self):
        self.music = pygame.mixer_music.load("../mp3/musique_fond.mp3")
        self.music_play = pygame.mixer.music.play(loops=-1)
        