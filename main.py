#Main projet FASO rallye musée
from EcranLCD import *
from Options import *

Mode_1_joueur = Option("Mode 1 joueur", [0,0,0], "")
Mode_2_joueurs = Option("Mode 2 joueurs", [0,0,0], "")

Option_choisie = menu_options([Mode_1_joueur, Mode_2_joueurs])


if Option_choisie == 1:#On lance le mode 1 joueur
        choix_quiz1 = Option("Quiz1",[0,0,0], "")
        choix_quiz2 = Option("Quiz2",[0,0,0], "")
        choix_quiz3 = Option("Quiz3",[0,0,0], "")
        menu_options([choix_quiz1,choix_quiz2,choix_quiz3])
else:#On lance le mode 2 joueurs
