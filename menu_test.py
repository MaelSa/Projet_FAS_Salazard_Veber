from LCD import *
from classes import *
import grovepi
from Fonctions import *
from test_lcd import *
color1 = [255,0,0]
color2 = [0,255,0]
color3 = [0,0,255]
print("ok1")
option1 = Option("Premier choix", color1, 0)
option2 = Option("Second choix", color2,0)
option3 = Option("Troisieme choix", color3, 0)
print("ok2")
quit = False
Options = [option1,option2,option3]
num_current_option = grovepi.analogRead(0)//3
print("ok3")
while not quit:
	print("ok4")
	action_potentiometre, action_bouton1, action_bouton2 = afficherLCD(Options[num_current_option].name,Options[num_current_option].color)
	print("ok5")
	if action_potentiometre == 1 and num_current_option != len(Options) - 1:
		num_current_option += 1
	elif action_potentiometre == -1 and num_current_option != 0:
		num_current_option -= 1
	elif action_bouton1:
		quit = True


