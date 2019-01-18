import time
from grovepi import *
import sys
from EcranLCD import *

class QuestionQCM:
    """Classe pour programmer des questions avec une réponse de type QCM"""
    def __init__(self, options, answer):
        """options : array of options, answuer : option"""
        self.options = options #(Liste) Les différentes options du QCM (ces objets sont donc des instances de la classe option)
        self.answer = answer #(Entier) entier correspondant à l'indice de la réponse dans la liste des options

    def executer_question(self):
        """laisse tourner le menu tant qu'une option n'a pas été selectionnée"""
        #On utilise simplemen l'option menu, qui nous renvoie l'option selectionnée en passant la liste des opions en paramètre
        #return un bool si la réponse est juste ou fausse
        answer = menu_options(self.options)
        return answer == self.answer

class QuestionsINT:
    """Classe pour programmer des questions qui attendent comme réponse un entier"""
    def __init__(self, name, answer, range_start, range_end):
        """name : string, answer : int, range : int"""
        self.name = name #La chaîne de caractères correspondant à la question
        self.answer = answer #L'entier attendu en réponse
        self.range_start = range_start
        self.range_end = range_end
        self.range = range_end - range_start

    def executer_question(self):
        #"""lit en continu les réponses"""
        num_print = analogRead(0)//self.range
        quit = False
        if num_print > self.range_end:
            num_print = self.range_end
        while not quit:
            action_potentiometre, action_bouton1, action_bouton2 = afficherLCD(str(num_print),[0,255,0],self.range)
            print(action_potentiometre)
            if action_potentiometre == 1 and num_print != self.range - 1:
                num_print += 1
            elif action_potentiometre == -1 and num_print != 0:
                num_print -= 1
            elif action_bouton1:
                quit = True
        return num_print == self.answer


class QuestionAssist:
    """Classe assistée par quelqu'un (nous ou un bénévole), il faut écrire un code pour que la réponse soit juste, il y a aussi un code pour indiquer que la réponse est fausse"""
    def __init__(self, name, color, code_right, code_false):
        """name : string, color : tuple 3 elements, code_right : int, code_false : int"""
        self.code_right = code_right
        self.code_false = code_false
        self.color = color

    def answer_choice(self):
        """affiche des nombres à l'écran, qu'on change en tournant le potentiomètre, on appuie pour valider la réponse, retourne le nombre affiché à l'écran au moment de l'appui du bouton"""
        num_print = analogRead(0)//10
        if num_print > 10:
            num_print = 10
        while not quit:
            action_potentiometre, action_bouton1, action_bouton2 = afficherLCD(str(num_print),num_print.color,10)
            print(action_potentiometre)
            if action_potentiometre == 1 and num_print != self.range - 1:
                num_print += 1
            elif action_potentiometre == -1 and num_print != 0:
                num_print -= 1
            elif action_bouton1:
                quit = True
                return num_print

    def executer_question(self):
        """vérifie si la réponse donnée est juste ou fausse"""
        answer_given = False
        while answer_given != self.code_false and answer_given != self.code_right: #On boucle tant que le code donné ne correspond pas à la réponse juste ou la réponse fausse (on fait cela pour éviter les erreurs possibles sur les entrées)
            answer_given = self.answer_choice()
        if answer_given == self.code_false:
            return False
        else:
            return True
