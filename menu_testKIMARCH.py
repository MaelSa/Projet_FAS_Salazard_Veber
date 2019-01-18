from test_lcd import *
from EcranLCD import *
from Options import *
from Fonctions import *
#from LCD import *
color1 = [255,0,0]
color2 = [0,255,0]
color3 = [0,0,255]
option1 = Option("J aime", color1, 0)
option2 = Option("Les", color2,0)
option3 = Option("musees", color3, 0)
quit = False
Options = [option1,option2,option3]
num_current_option = analogRead(0)//3
if num_current_option > 2:
	num_current_option = 2
while not quit:
	action_potentiometre, action_bouton1, action_bouton2 = afficherLCD(Options[num_current_option].name,Options[num_current_option].color,3)
	print(action_potentiometre)
	if action_potentiometre == 1 and num_current_option != len(Options) - 1:
		num_current_option += 1
	elif action_potentiometre == -1 and num_current_option != 0:
		num_current_option -= 1
	elif action_bouton1:
		quit = True


afficherLCD("Au revoir poto")
