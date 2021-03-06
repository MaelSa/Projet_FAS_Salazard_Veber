#Classe permettant de créer un quiz, suite de questions:
from EcranLCD import *
import time
from grovepi import *

led_rouge = 4
led_bleue = 7
pinMode(led_bleue, "OUTPUT")
pinMode(led_rouge, "OUTPUT")


class Quiz:
    def __init__(self, questions, start_text, end_text, code):
        """questions est une liste de questions qui se déroulerons dans l'ordre"""
        self.questions = questions
        self.score = 0
        self.start_text = start_text
        self.end_text = end_text
        self.code = code
    def executer_quiz(self):
        print("Bienvenue dans le quizz")
        afficherLCD("Bienvenue dans le quiz")
        time.sleep(2)
        score = 0
        i = 0
        retour_selection_quiz = False
        while i < len(self.questions) and not retour_selection_quiz:
            answer = self.questions[i].executer_question()
            print("réponse donnée", answer)

            if answer == -1:
                #Appui du bouton 2, donc retour en arrièr edans les menus
                score = -1
                retour_selection_quiz = True
                afficherLCD("Retour au choix des quizz", [0, 100, 50])
                time.sleep(1)
            elif answer:
                #Bonne réponse
                score += 1
                #On allume led verte brièvement, else on allume led rouge brièvement (si la réponse est fausse
                digitalWrite(led_bleue, 1)
                afficherLCD("Reponse juste !", [0, 255, 0])
                time.sleep(1)
                digitalWrite(led_bleue, 0)

            else:
                digitalWrite(led_rouge, 1)
                afficherLCD("Reponse fausse !", [255, 0, 0])
                time.sleep(1)
                digitalWrite(led_rouge, 0)

            i += 1
        return score

    def executer_quiz_mode_2_joueurs(self):
        #Même chose que pour l'execution à 1 joueur, mais avec envoi des informations au serveur grâce au socket
        global bonne_rep
        global sent_rep

        bonne_rep = False
        sent_rep = False

        print("Bienvenue dans le quizz")
        afficherLCD("Bienvenue dans le quiz")
        print("je pense que c'est le bon mode")
        time.sleep(2)
        score = 0
        i = 0
        retour_selection_quiz = False
        while i < len(self.questions) and not retour_selection_quiz:
            answer = self.questions[i].executer_question()
            print("réponse donnée", answer)
            print(str(type(answer)))
            if answer == "True":
                print("gotit")
            if answer == -1:
                #Réponse signifiant un appui sur le bouton2,donc retour en arrière
                score = -1
                retour_selection_quiz = True
                afficherLCD("Retour au choix des quizz", [0, 100, 50])

                time.sleep(1)
            elif answer:
                print("LA REPONSE EST BONNE")
                bonne_rep = True
                sent_rep = False
                #La réponse correspond à la bonne réponse
                score += 1
                # On allume led verte brièvement, else on allume led rouge brièvement (si la réponse est fausse
                digitalWrite(led_bleue, 1)
                afficherLCD("Reponse juste !", [0, 255, 0])
                time.sleep(1)
                string = "Reponse juste"

                digitalWrite(led_bleue, 0)

            else:
                digitalWrite(led_rouge, 1)
                afficherLCD("Reponse fausse !", [255, 0, 0])

                time.sleep(1)
                digitalWrite(led_rouge, 0)
            i += 1

        return score

    def executer_mode_1_serv(self, ip, port):
        import socket
        hote = ip
        port = port
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.connect((hote, port))
        afficherLCD("Bienvenue dans le quiz")
        time.sleep(2)
        score = 0
        i = 0
        retour_selection_quiz = False
        while i < len(self.questions) and not retour_selection_quiz:
            answer = self.questions[i].executer_question()
            print("réponse donnée", answer)

            if answer == -1:
                #Réponse signifiant un appui sur le bouton2,donc retour en arrière
                score = -1
                retour_selection_quiz = True
                afficherLCD("Retour au choix des quizz", [0, 100, 50])
                string = "Retour au choix des quizz"
                stringsend = string.encode()
                socket.send(stringsend)
                time.sleep(1)
            elif answer:
                #La réponse correspond à la bonne réponse
                score += 1
                # On allume led verte brièvement, else on allume led rouge brièvement (si la réponse est fausse
                digitalWrite(led_bleue, 1)
                afficherLCD("Reponse juste !", [0, 255, 0])
                time.sleep(1)
                string = "Reponse juste"
                stringsend = string.encode()
                socket.send(stringsend)
                digitalWrite(led_bleue, 0)

            else:
                digitalWrite(led_rouge, 1)
                afficherLCD("Reponse fausse !", [255, 0, 0])
                string = "Reponse fausse"
                stringsend = string.encode()
                socket.send(stringsend)
                time.sleep(1)
                digitalWrite(led_rouge, 0)
            i += 1
        string = "Le score est de " + str(score)
        stringsend = str(score).encode()
        socket.send(stringsend)
        socket.close()
        return score
