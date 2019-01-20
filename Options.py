#Classe permettant de gérer les options (dans les menus)
class Option:
    def __init__(self, name, color, sound):
        self.name = name   #(String) le nom de l'option
        self.color = color #(tuple) Couleur des backlight de l'écran lorsque l'option est en sélection
        self.sound = sound #(string) Chemin vers le son à jouer lors de l'option (peut être None)