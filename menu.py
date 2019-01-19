from Fonctions_lcd import *
from EcranLCD import *
from Options import *
from Fonctions_lcd import *


def menu_options(Options):


	num_current_option = analogRead(0)//len(Options)
	if num_current_option > len(Options) - 1:
		num_current_option = len(Options) - 1
	quit = False
	while not quit:
		action_potentiometre, action_bouton1, action_bouton2 = afficherLCD(Options[num_current_option].name,Options[num_current_option].color,3)
		print(num_current_option)
		if action_potentiometre == 1 and num_current_option != len(Options) - 1:
			num_current_option += 1
		elif action_potentiometre == -1 and num_current_option != 0:
			num_current_option -= 1
		elif action_bouton1:
			quit = True
	print("on return", num_current_option + 1)
	return num_current_option
