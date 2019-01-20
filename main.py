#Main projet FASO rallye musée
from EcranLCD import *
from Options import *
from Instances_classes import *
from Mode_2_joueurs import *
import time
led_rouge = 4
led_bleue = 7
pinMode(led_bleue, "OUTPUT")
pinMode(led_rouge, "OUTPUT")

for i in range(3):
    digitalWrite(led_rouge, 1)
    digitalWrite(led_bleue, 1)
    time.sleep(0.5)
    digitalWrite(led_rouge, 0)
    digitalWrite(led_bleue, 0)

Mode_1_joueur = Option("Mode 1 joueur", [0,50,50], "")
Mode_2_joueurs = Option("Mode 2 joueurs", [0,255,0], "")
fin_de_programme = False
while not fin_de_programme:
    Option_choisie = menu_options([Mode_1_joueur, Mode_2_joueurs])
    print("L'option choisie est ", Option_choisie)
    if Option_choisie == 1: #On lance le mode 1 joueur
        changer_mode = False
        while not changer_mode:
            print("on entre dans le menu des quizz")
            for i in range(2):
                digitalWrite(led_rouge, 1)
                digitalWrite(led_bleue, 1)
                time.sleep(0.5)
                digitalWrite(led_rouge, 0)
                digitalWrite(led_bleue, 0)
                time.sleep(0.5)

            choix_quiz1 = Option("Quiz1", [0, 50, 100], "")
            choix_quiz2 = Option("Quiz2", [0, 255, 0], "")
            choix_quiz3 = Option("Quiz3", [0, 0, 255], "")
            time.sleep(1)
            quiz_choisi = menu_options([choix_quiz1, choix_quiz2, choix_quiz3])
            print("le quizz choisi est ", quiz_choisi)
            if quiz_choisi == 1:
                for i in range(2):
                    digitalWrite(led_rouge, 1)
                    digitalWrite(led_bleue, 1)
                    time.sleep(0.5)
                    digitalWrite(led_rouge, 0)
                    digitalWrite(led_bleue, 0)
                    time.sleep(0.5)
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

            elif quiz_choisi == 2:
                print("on exectute mode 2")
                executer_mode_2()

            elif quiz_choisi == 0:
                changer_mode = True


