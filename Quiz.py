#Classe permettant de créer un quiz, suite de questions:
from EcranLCD import *
import time
class Quiz:
    def __init__(self, questions, start_text, end_text, code):
        """questions est une liste de questions qui se déroulerons dans l'ordre"""
        self.questions = questions
        self.score = 0
        self.start_text = start_text
        self.end_text = end_text
        self.code = code
    def executer_quiz(self):
        afficherLCD("Bienvenue dans le quiz")
        time.sleep(2)
        score = 0
        i = 0
        retour_selection_quiz = False
        while i < len(self.questions) and not retour_selection_quiz:
            print("ON EXECTUTE LE QUIZZ")
            answer = self.questions[i].executer_question()
            print("réponse donnée", answer)

            if answer == -1:
                score = -1
                retour_selection_quiz = True
            elif answer:
                score += 1
                #On allume led verte brièvement, else on allume led rouge brièvement (si la réponse est fausse
            i += 1
        return score
