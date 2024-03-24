from jeu import jeu
from menu import menu
from Sound import Sound
#from musique import musique

lancerAvecMenu = True #a modif si besoin
musique = True
if musique :
    Sound()
if lancerAvecMenu:
    menu()
jeu()