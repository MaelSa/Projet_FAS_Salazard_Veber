########## ECRAN ##########

##### FONCTIONS IMPORTEES #####

import time,sys,grovepi

if sys.platform == 'uwp':
    import winrt_smbus as smbus
    bus = smbus.SMBus(1)
else:
    import smbus
    import RPi.GPIO as GPIO
    rev = GPIO.RPI_REVISION
    if rev == 2 or rev == 3:
        bus = smbus.SMBus(1)
    else:
        bus = smbus.SMBus(0)

# this device has two I2C addresses
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e

# set backlight to (R,G,B) (values from 0..255 for each)
def setRGB(r,g,b):
    bus.write_byte_data(DISPLAY_RGB_ADDR,0,0)
    bus.write_byte_data(DISPLAY_RGB_ADDR,1,0)
    bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
    bus.write_byte_data(DISPLAY_RGB_ADDR,4,r)
    bus.write_byte_data(DISPLAY_RGB_ADDR,3,g)
    bus.write_byte_data(DISPLAY_RGB_ADDR,2,b)

# send command to display (no need for external use)
def textCommand(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)

# set display text \n for second line(or auto wrap)
def setText(text):
    textCommand(0x01) # clear display
    time.sleep(.05)
    textCommand(0x08 | 0x04) # display on, no cursor
    textCommand(0x28) # 2 lines
    time.sleep(.05)
    count = 0
    row = 0
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xc0)
            if c == '\n':
                continue
        count += 1
        bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

#Update the display without erasing the display
def setText_norefresh(text):
    textCommand(0x02) # return home
    time.sleep(.05)
    textCommand(0x08 | 0x04) # display on, no cursor
    textCommand(0x28) # 2 lines
    time.sleep(.05)
    count = 0
    row = 0
    while len(text) < 32: #clears the rest of the screen
        text += ' '
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xc0)
            if c == '\n':
                continue
        count += 1
        bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

##### FONCTION NOUVELLE #####
def action(temps,nbrOption=1):
    # Potentiomètre
    posStart=grovepi.analogRead(0)
    mvtPosition=0
    # Boutons
    bouton1=False
    bouton2=False
    # Temps
    tStart=time.time()
    tCourant=time.time()

    while (tCourant < tStart+temps) and (mvtPosition == 0) and not bouton1 and not bouton2:
        # Potentiomètre
        posCourante=grovepi.analogRead(0)
        if posCourante-posStart > 256//nbrOption:
            mvtPostion=1
        elif posStart-posCourante > 256//nbrOption:
            mvtPosition=-1
        # Bouton 1
        if grovepi.digitalRead(3)==1:
            bouton1=True

	# Bouton 2
        if grovepi.digitalRead(2)==1:
            bouton2=True
        tCourant=time.time()
    return mvtPosition,bouton1,bouton2

def afficherLCD(text,rgb=[0,255,0]):
#"""
#Données :
#    text (Chaine de caractères) que lon souhaite afficher sur lécran lcd
#        Option :
#    rgb (Liste de int E {0;255}) pour définir la couleur de fond d'écran

#Résultat :
#    Affiche le texte sur l'écran LCD
#"""

    ### Initialise la couleur de fond
    setRGB(rgb[0],rgb[1],rgb[2])

    ### Analyse le texte pour ne pas couper de mot
    reste=len(text)%16
    nbrLigne=len(text)//16+1

    i=1
    while i<nbrLigne :
        if (text[i*16-1] != " ") and (text[i*16-1] != ",") and (text[i*16-1] != "!") and (text[i*16-1] != "?") and (text[i*16-1] != ":") and (text[i*16] != " "):
            while caractere != " "



    ### Affiche le texte et fait défiler si nécessaire jusqu'à ce que quelqu'un agisse
    a = False
    while not a:
                     # On évalue action mais pas la première fois -> Do...While
        i=0 # Itérateur de ligne
        a,b,c=action(2)
        while i<nbrLigne and not a:
            ligne1=text[i*16:(i+2)*16] # Caractères 0 à 31 etc
            if i==nbrLigne-1: # S'il n'y a pas de ligne i+2
                ligne1=text[i*16:(i+1)*16+reste]

            setText(ligne1)
            i+=1
            a,b,c = action(3)
            print("ok42")
    return a,b,c

########## TESTS ##########
#afficherLCD(a)
#afficherLCD("16 char par lign")
#afficherLCD("Bonjour, je suis étudiant en IG,je fais mon projet FASo, dont le but est d écrire des lignes pour écrires des lignes")
