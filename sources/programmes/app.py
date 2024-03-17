from jeu import jeu
from menu import menu
from Sound import Sound
#from musique import musique

lancerAvecMenu = True #a modif si besoin
musique = False

if lancerAvecMenu:
    if musique :
        Sound()    
    menu()
jeu()