#Mode deux joueurs avec structure client-serveur en wifi
from EcranLCD import *
from Options import *
from Instances_classes import *
import time
import socket


def executer_mode_2(num_client):
    global 2j
    if not 2j:
        2j = True
        #Comme le joueur 1, seule change la fonction d'éxecution des quizz
        print('On lance le bon mode dexecution jesp')
        changer_mode = False
        ip = "192.168.1.53"
        ports = [5000,12800]
        port = ports[num_client]
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
                score = quiz1.executer_quiz_mode_2_joueurs()
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
                for i in range(2):
                    digitalWrite(led_rouge, 1)
                    digitalWrite(led_bleue, 1)
                    time.sleep(0.5)
                    digitalWrite(led_rouge, 0)
                    digitalWrite(led_bleue, 0)
                    time.sleep(0.5)
                score = quiz2.executer_quiz_mode_2_joueurs()
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

            elif quiz_choisi == 3:
                for i in range(2):
                    digitalWrite(led_rouge, 1)
                    digitalWrite(led_bleue, 1)
                    time.sleep(0.5)
                    digitalWrite(led_rouge, 0)
                    digitalWrite(led_bleue, 0)
                    time.sleep(0.5)
                score = quiz3.executer_quiz_mode_2_joueurs()
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

            elif quiz_choisi == 0:
                changer_mode = True
