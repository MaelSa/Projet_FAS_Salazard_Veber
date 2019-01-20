#Fichier regroupant les instances des classes options, questions et quizz#Fichier regroupant la liste des questions)
#La numérotation des questions correspond à la numérotation des oeuvres
from Question import *
from Options import *
from Quiz import *

option1 = Option("Premiere option", [0, 255, 255], "")
option2 = Option("Seconde option", [0, 100, 50], "")
option3 = Option("Troisieme option", [40,50,100], "")

Question_1 = QuestionAssist("Trouver le serpent", (100, 20, 100), 2, 5)
#Réponse : en or, en dessous du pot qui fume

Question_3 = QuestionsINT("Combien de personnages", 15, 0, 40)

Question_2 = QuestionQCM("Question qcm",[option1, option2, option3], 1)

Question_8 = QuestionAssist("Trouver la lance/marteau", (0, 0, 0), 0, 0)
#Réponse, vers la droite

#Question_10a = QuestionQCM() Il faut d'abord faire les options
#Question_10b = QuestionQCM() Il faut d'abotd faire les options

#Question_11 = QuestionQCM()

#Question_12 =  QuestionQCM()

#Question_13 = QuestionQCM()

#Fichier regroupant la liste des questions)
#La numérotation des questions correspond à la numérotation des oeuvres





quiz1 = Quiz([Question_2, Question_1, Question_3],"Debut du quiz 1","fin du quiz 1",2)
quiz2 = Quiz([Question_1, Question_3, Question_8],"Debut du quiz 1","fin du quiz 1",2)
quiz3 = Quiz([Question_1, Question_3, Question_8],"Debut du quiz 1","fin du quiz 1",2)
