import time
import grovepi
import sys

#Classe permettant de gérer les options (dans les menus)
class Option:
    def __init__(self, name, color, sound):
        """name : string, color : tuple 3 elements, sound : string"""
        self.name = name #(String) le nom de l'option
        self.color = color #(tuple) Couleur des backlight de l'écran lorsque l'option est en sélection
        self.sound = sound #(string) Chemin vers le son à jouer lors de l'option (peut être None)


class QuestionQCM:
    """Classe pour programmer des questions avec une réponse de type QCM"""
    def __init__(self, options, answer):
        """options : array of options, answer : option"""
        self.options = options #(Liste) Les différentes options du QCM (ces objets sont donc des instances de la classe option)
        self.answer = answer #(Entier) entier correspondant à l'indice de la réponse dans la liste des options


class QuestionsINT:
    """Classe pour programmer des questions qui attendent comme réponse un entier"""
    def __init__(self, name, answer, range_start, range_end):
        """name : string, answer : int, range : int"""
        self.name = name #La chaîne de caractères correspondant à la question
        self.answer = answer #L'entier attendu en réponse
        self.range_start = range_start
        self.range_end = range_end
    def answer_choice(self):
        """lit en continu les réponses"""
        answer_given = False
        pos_start = grovepi.analogRead(0)
        range = self.range_end - self.range_start
        increment = range/255
        int_shown = self.range_start + (pos_start * range)
        while not answer_given: #On continue tant qu'une réponse n'a pas été donnée
            posCourante=grovepi.analogRead(0))
            answer_given = bool(grovepi.digital.read(3))
            #faut calculer le décalage, incrementer ... modifier la pos, mais la laisser en pos courante si on modifie pas (à réfléchir still)


class QuestionAssist:
    """Classe assistée par quelqu'un (nous ou un bénévole), il faut écrire un code pour que la réponse soit juste, il y a aussi un code pour indiquer que la réponse est fausse"""
    def __init__(self, name, color, code_right, code_false):
        """name : string, color : tuple 3 elements, code_right : int, code_false : int"""
        self.code_right = code_right
        self.code_false = code_false
        self.color = color

    def answer_choice(self):
        answer_given = False
        while not answer_given:
            number_shown = grovepi.analogRead(0)
            answer_given = bool(grovepi.digital.read(3))
        return number_shown
