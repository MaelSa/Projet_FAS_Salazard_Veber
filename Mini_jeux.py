#Mini jeux et fonctions nécessaires
from Fonctions import *

def menu(options):
    """options est une liste, renvoie l'option selectionnée"""
    select = False #Variable indiquant si un choix a été fait
    state_pot = lire_intensité() #Variable gérant l'état du potentiomètre
    current_option_select = 0 #Variable qui contient l'option sur laquelle se trouve le curseur

    longueur_cran = int(256/len(options)-1)
    while not select: #La boucle tourne tant qu'un choix n'a pas été fait
        afficher_string(option[current_option_select])
        current_state_pot = lire_intensité()





          
        mvt = current_state_pot - state_pot
        if abs(mvt)>longueur_cran:
            if mvt > 0:
                if current_option_select != len(options) - 1:
                    current_option_select += 1
                else:
                    current_option_select = 0
            else:
                if current_option_select != 0:
                    current_option_select -= 1
                else:
                    current_option_select = len(options) - 1

            state_pot = current_state_pot
        select = lire_bouton()

    return(options[current_option_select])
