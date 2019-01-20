from Question import *
from Quiz import *
from Options import *
# A insérer à la ligne 7 de Instances_classes.py

#Alexandre consulte l'oracle d'Apollon
tableau1 = QuestionAssist("Trouver le serpent", (100, 20, 100), 2, 5, 'tableau1')
#Réponse : en or, en dessous du pot qui fume

#Ariane dans l'île de Naxos
tableau3 = QuestionsINT("Combien de personnages ?", 15, 0, 40, 'tableau3')

#Fermeté de Jubellius Taurea
option10a = Option("L aigle Romaine", [0, 255, 255], "")
option10b = Option("Le Faucon Romain", [255, 0, 255], "")
option10c = Option("La Chouette Grecque", [255, 255, 0], "")
tableau10a = QuestionQCM("Quel oiseau est au dessus de SPQR ?",[option10a, option10b, option10c], 1)

option10d = Option("Sumus pridque romanus", [0, 255, 255], "")
option10e = Option("Senatus polus romanus", [255, 0, 255], "")
option10f = Option("Sancticus pune romanus", [255, 255, 0], "")
tableau10b = QuestionQCM("Que veut dire SPQR ?",[option10d, option10e, option10f], 2)

#Hector exposé sur les rives du Scamandre après avoir été tué par Achille et traîné à son char ; Vénus préserve son corps de la corruption
option11a = Option("Vrai", [0, 255, 255], "")
option11b = Option("Faux", [255, 255, 0], "")
tableau11 = QuestionQCM("Achille saigne des talons ?",[option11a, option11b], 2)

#Jésus-Christ guérissant des malades au bord du lac de Génézareth
# Nous devons toujours décider de la bonne réponse donc hors présentation
option12a = Option("Rose", [0, 255, 255], "")
option12b = Option("Bleue", [255, 0, 255], "")
option12c = Option("Violette", [255, 255, 0], "")
tableau12 = QuestionQCM("De quelle couleur est la toge de Jesus ?",[option12a, option12b, option12c], 1)

#La Chasse de Didon et Enée
option13a = Option("Demi-Dieu", [0, 255, 255], "")
option13b = Option("Demi-Deesse", [255, 255, 0], "")
tableau13 = QuestionQCM("Enee etait un demi-dieu ou une demi-deesse ?",[option13a, option13b], 1)

#La Danse
tableau14 = QuestionAssist("Trouver les deux etoiles de David", (100, 20, 100), 6, 3)
#Réponse : dans l'arbre

#La Formation de l'Homme par Prométhée aidé du secours de Minerve
tableau15 = QuestionsINT("Combien d’animaux ?", 5, 0, 10, 'tableau15')


# QUIZ
quiz1 = Quiz([tableau14, tableau10a, tableau15, tableau1, tableau3], "Debut du quiz 1", "Fin du quiz 1 !", 2)
quiz2 = Quiz([tableau12, tableau14, tableau11, tableau13, tableau10a], "Debut du quiz 2", "Fin du quiz 2 !", 2)
quiz3 = Quiz([tableau13, tableau15, tableau10b, tableau1, tableau12], "Debut du quiz 3", "Fin du quiz 3 !", 2)

# la suite une autre fois car flemme !
