#Classe permettant de créer un quiz, suite de questions:

class Quiz:
    def __init__(self, questions, start_text, end_text, code):
        """questions est une liste de questions qui se déroulerons dans l'ordre"""
        self.questions = questions
        self.score = 0
        self.start_text = start_text
        self.end_text = end_text
        self.code = code
    def executer_quiz(self):
        for i in self.questions:
            if i.answer:
                score += 1
