#Classe permettant de créer un quiz, suite de questions:
from EcranLCD import *
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
        score = 0
        for i in self.questions:

            print("ON EXECTUTE LE QUIZZ")
            answer = i.executer_question()
            print("réponse donnée", answer)
            if answer:
                score += 1
                #On allume led verte brièvement, else on allume led rouge brièvement (si la réponse est fausse
        return score
