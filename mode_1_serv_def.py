#Mode deux joueurs avec structure client-serveur en wifi
from EcranLCD import *
from Options import *
from Instances_classes import *
from Mode_2_joueurs import *
import time
import socket


def executer_mode_1j_serv(ip, num_client):
    print("what we do is one mod serv")
    ports = [5000,12800]
    port = ports[num_client]
    #Comme le joueur 1, seule change la fonction d'éxecution des quizz
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
        choix_quiz4 = Option("Quiz4", [50,100,0], "")
        time.sleep(1)
        quiz_choisi = menu_options([choix_quiz1, choix_quiz2, choix_quiz3, choix_quiz4])
        print("le quizz choisi est ", quiz_choisi)

        if quiz_choisi == 1:
            for i in range(2):
                digitalWrite(led_rouge, 1)
                digitalWrite(led_bleue, 1)
                time.sleep(0.5)
                digitalWrite(led_rouge, 0)
                digitalWrite(led_bleue, 0)
                time.sleep(0.5)
            score = quiz1.executer_mode_1_serv(ip, port)
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
            score = quiz2.executer_mode_1_serv(ip, port)
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
            score = quiz3.executer_mode_1_serv(ip, port)
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
        elif quiz_choisi == 4:
            for i in range(2):
                digitalWrite(led_rouge, 1)
                digitalWrite(led_bleue, 1)
                time.sleep(0.5)
                digitalWrite(led_rouge, 0)
                digitalWrite(led_bleue, 0)
                time.sleep(0.5)
            score = quiz4.executer_mode_1_serv(ip, port)
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
