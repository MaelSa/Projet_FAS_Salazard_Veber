#Main projet FASO rallye musée
from EcranLCD import *
from Options import *
from Instances_classes import *
Mode_1_joueur = Option("Mode 1 joueur", [255,0,0], "")
Mode_2_joueurs = Option("Mode 2 joueurs", [0,255,0], "")
fin_de_programme = False
while not fin_de_programme:
    Option_choisie = menu_options([Mode_1_joueur, Mode_2_joueurs])
    if Option_choisie == 0: #On lance le mode 1 joueur
        changer_mode = False
        while not changer_mode:
            choix_quiz1 = Option("Quiz1", [255, 0, 0], "")
            choix_quiz2 = Option("Quiz2", [0, 255, 0], "")
            choix_quiz3 = Option("Quiz3", [0, 0, 255], "")
            quiz_choisi = menu_options([choix_quiz1, choix_quiz2, choix_quiz3])
            print("le quizz choisi est ", quiz_choisi)
            if quiz_choisi == 1:

                score = quiz1.executer_quiz()
                if score == -1:
                    changer_mode = True
                    afficherLCD("Retour au choix du mode de jeu")
                    time.sleep(2)
                else:
                    score_string = str(score)
                    affichage_score = "Votre score sur ce quizz est de " + score_string
                    afficherLCD(affichage_score)
                    bouton1 = False
                    while not bouton1:
                        bouton1 = digitalRead(3)
            #elif quiz_choisi == 2:

#else:#On lance le mode 2 joueurs
