

#Classe permettant de gérer les options (dans les menus)
class Option:
    def __init__(self, name, color, sound):
        self.name = name #(String) le nom de l'option
        self.color = color #(tuple) Couleur des backlight de l'écran lorsque l'option est en sélection
        self.sound = sound #(string) Chemin vers le son à jouer lors de l'option (peut être None)


class QuestionQCM:
    """Classe pour programmer des questions avec une réponse de type QCM"""
    def __init__(self, options, answer):
        self.options = options #(Liste) Les différentes options du QCM (ces objets sont donc des instances de la classe option)
        self.answer = answer #(Entier) entier correspondant à l'indice de la réponse dans la liste des options


class QuestionsINT:
    """Classe pour programmer des questions qui attendent comme réponse un entier"""
    def __init__(self, name, answer, range):
        self.name = name #La chaîne de caractères correspondant à la question
        self.answer = answer #L'entier attendu en réponse
        self.range = range #Corresponf à l'intervalle d'entier possibles pour la réponse, afin de "subdiviser" la course du potentiomètre

    #def answer_choice(self):
        #fonction qui lit en continu les 