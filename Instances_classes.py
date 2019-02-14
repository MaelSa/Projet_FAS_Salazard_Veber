from Question import *
from Quiz import *
from Options import *

#Alexandre consulte l'oracle d'Apollon
tableau1 = QuestionAssist("Trouver le serpent", (100, 20, 100), 2, 5, 'tableau1.wav')
#Réponse : en or, en dessous du pot qui fume

#Ariane dans l'île de Naxos
tableau3 = QuestionsINT("Combien de personnages ?", 15, 0, 40, 'tableau3.wav')

#Fermeté de Jubellius Taurea
option10a = Option("L aigle Romaine", [0, 255, 255], "option10a.wav")
option10b = Option("Le Faucon Romain", [255, 0, 255], "option10b.wav")
option10c = Option("La Chouette Grecque", [255, 255, 0], "option10c.wav")
tableau10a = QuestionQCM("Quel oiseau est au dessus de SPQR ?",[option10a, option10b, option10c], 1, "tableau10a.wav")

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
tableau14 = QuestionAssist("Trouver les deux etoiles de David", (100, 20, 100), 6, 3, "tableau14.wav")
#Réponse : dans l'arbre

#La Formation de l'Homme par Prométhée aidé du secours de Minerve
tableau15 = QuestionsINT("Combien d’animaux ?", 5, 0, 10, 'tableau15.wav')


### NEW QUESTIONS

#Le baptême du Christ
tableau18 = QuestionAssist("Trouver l'epee", (100, 20, 100), 6, 3, "")
#Réponse : Cachée sous le casque

#Le Retour de la chasse
tableau19 = QuestionsINT("Combien d’animaux ?", 8, 0, 10, 'tableau15.wav')

#Pygmalion amoureux de sa statue
tableau21 = QuestionAssist("Ou est Pygmalion ?", (100, 20, 100), 6, 3, "")
#Réponse : Homme habillé

#Saint Jean-Baptiste
option22a = Option("Jean-Baptiste apotre de Dieu", [0, 255, 255], "")
option22b = Option("Jean-Baptiste fils de Dieu", [255, 255, 0], "")
option22c = Option("Voici l'agneau de Dieu", [255, 255, 0], "")
tableau22 = QuestionQCM("Que veut dire Ecce Agnus Dei ?",[option22a, option22b, option22c], 3)

#Ulysse sauvé du naufrage par Minerve, aborde à l'ile de Calypso
tableau24 = QuestionAssist("Trouver Minerve ?", (100, 20, 100), 6, 3, "")
#Réponse : Femme en bleu

#Vénus demande à Vulcain des armes pour son fils Enée
option25a = Option("Des enfers et du feu", [0, 255, 255], "")
option25b = Option("Du fer et du feu", [255, 255, 0], "")
option25c = Option("Des volcans et du feu", [255, 255, 0], "")
tableau25a = QuestionQCM("Vulcain etait le Dieu de...",[option25a, option25b, option25c], 2)

option25d = Option("Hades", [0, 255, 255], "")
option25e = Option("Ares", [255, 255, 0], "")
option25f = Option("Hephaistos", [255, 255, 0], "")
tableau25b = QuestionQCM("Quel equivalent grec pour Vulcain ?",[option25d, option25e, option25f], 3)

#Vue de la ville d'Elburg, sur le Zuyderzee
option27a = Option("Blanc", [0, 255, 255], "")
option27b = Option("Jaune", [255, 255, 0], "")
option27c = Option("Marron", [255, 255, 0], "")
tableau27 = QuestionQCM("Couleur du moulin a vent :",[option27a, option27b, option27c], 1)

#Vue de la ville de Grave-sur-Meuse, dans les Pays-Bas
tableau28 = QuestionsINT("Combien de charrues ?", 6, 0, 10, '')


# QUIZ
quiz1 = Quiz([tableau1, tableau3, tableau10a, tableau11, tableau12], "Debut du quiz 1", "Fin du quiz 1 !", 2)
quiz2 = Quiz([tableau10b, tableau13, tableau14, tableau15, tableau18], "Debut du quiz 2", "Fin du quiz 2 !", 2)
quiz3 = Quiz([tableau19, tableau21, tableau22, tableau24, tableau25a], "Debut du quiz 3", "Fin du quiz 3 !", 2)
quiz4 = Quiz([tableau25b, tableau27, tableau28, tableau13, tableau12],"Debut du quiz", "Fin du quiz ", 2)
