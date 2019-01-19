#Fichier regroupant les instances des classes options, questions et quizz#Fichier regroupant la liste des questions)
#La numérotation des questions correspond à la numérotation des oeuvres
from Question import *
from Options import *
from Quiz import *

option1 = Option()

Question_1 = QuestionAssist("Trouver le serpent", (100, 20, 100), 2, 5)
#Réponse : en or, en dessous du pot qui fume

Question_3 = QuestionsINT("Combien de personnages", 15, 0, 40)



Question_8 = QuestionAssist("Trouver la lance/marteau", (0, 0, 0), 0, 0)
#Réponse, vers la droite

#Question_10a = QuestionQCM() Il faut d'abord faire les options
#Question_10b = QuestionQCM() Il faut d'abotd faire les options

#Question_11 = QuestionQCM()

#Question_12 =  QuestionQCM()

#Question_13 = QuestionQCM()

#Fichier regroupant la liste des questions)
#La numérotation des questions correspond à la numérotation des oeuvres


Question_1 = QuestionAssist("Trouver le serpent",(0,0,0),15,15)
#Réponse : en or, en dessous du pot qui fume

Question_3 = QuestionsINT("Combien de personnages", 15, 0, 40)

Question_8 = QuestionAssist("Trouver la lance/marteau",(0,0,0),0,0)
#Réponse, vers la droite

#Question_10a = QuestionQCM() Il faut d'abord faire les options
#Question_10b = QuestionQCM() Il faut d'abotd faire les options

#Question_11 = QuestionQCM()

#Question_12 =  QuestionQCM()

#Question_13 = QuestionQCM()

quiz1 = Quiz([Question_1, Question_3, Question_8],"Debut du quiz 1","fin du quiz 1",2)
quiz2 = Quiz([Question_1, Question_3, Question_8],"Debut du quiz 1","fin du quiz 1",2)
quiz3 = Quiz([Question_1, Question_3, Question_8],"Debut du quiz 1","fin du quiz 1",2)
