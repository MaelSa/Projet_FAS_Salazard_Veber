from Fonctions_lcd import *
from EcranLCD import *
from Options import *
from Fonctions_lcd import *


def menu_options(Options):

	#color1 = [255,0,0]
	#color2 = [0,255,0]
	#color3 = [0,0,255]
	#option1 = Option("J aime", color1, 0)
	#option2 = Option("Les", color2,0)
	#option3 = Option("musees", color3, 0)
	#quit = False
	#Options = [option1,option2,option3]
	num_current_option = analogRead(0)//len(Options)
	if num_curret_option > len(Options) - 1:
		num_current_option = len(Options) - 1
	while not quit:
		action_potentiometre, action_bouton1, action_bouton2 = afficherLCD(Options[num_current_option].name,Options[num_current_option].color,3)
		print(num_current_option)
		if action_potentiometre == 1 and num_current_option != len(Options) - 1:
			num_current_option += 1
		elif action_potentiometre == -1 and num_current_option != 0:
			num_current_option -= 1
		elif action_bouton1:
			quit = True
	return num_current_option + 1
