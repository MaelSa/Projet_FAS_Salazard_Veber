from grovepi import *
import time


##### ACTION : Surveille les entrées #####

def action(temps,nbrOption=0,ignorer=[False,False]):
    '''
Données :
    temps (int>0) détermine combien de temps les boutons/potentiomètre sont surveillés

        Options :
    nbrOption (int>=0) pour le menu déroulant, si 0 alors pas de menu déroulant donc potentiomètre inactif
    ignorer (Liste de bool) pour rendre les boutons inactifs

Résultat :
    Lorsque l'utilisateur agit sur un bouton/potentiomètre actif, alors la fonction prend fin et renvoie des informations sur l'action
    '''

    ### Initialisation
    # Potentiomètre    
    posStart = analogRead(0)
    mvtPosition=0
    # Boutons
    bouton1=False
    bouton2=False
    # Temps
    tStart=time.time()
    tCourant=time.time()

    ### Test jusqu'à temps écoulé ou action détectée    
    while (tCourant < tStart+temps) and (mvtPosition == 0) and not bouton1 and not bouton2:
        # Potentiomètre
        if nbrOption:
            posCourante=analogRead(0)
            if posCourante-posStart > 256//nbrOption:
                mvtPostion=1
            elif posStart-posCourante > 256//nbrOption:
                mvtPosition=-1
        # Bouton 1
        if not ignorer[0] and (digitalRead(3)==1):
            bouton1=True
        # Bouton 2
        if not ignorer[1] and (digitalRead(2)==1):
            bouton2=True
        # Temps
        tCourant=time.time()

    ### Renvoie ce qui a été détecté
    return mvtPosition,bouton1,bouton2


  
##### AFFICHER : Print sur écran #####

def afficherLCD(text,rgb=[0,255,0],nbrOption=0,ignorer=[False,False]):
"""
Données :
    text (Chaine de caractères) que l'on souhaite afficher sur lécran lcd

        Options :
    rgb (Liste de int E {0;255}) pour définir la couleur de fond d'écran
        Spécifique à action :
    nbrOption (int>=0) pour le menu déroulant, si 0 alors pas de menu déroulant donc potentiomètre inactif
    ignorer (Liste de bool) pour rendre les boutons inactifs

Résultat :
    Affiche le texte sur l'écran LCD
    Lorsque l'utilisateur agit sur un bouton/potentiomètre actif, alors la fonction prend fin et renvoie des informations sur l'action
"""

    ### Initialise la couleur de fond
    setRGB(rgb[0],rgb[1],rgb[2])

    ### Analyse du texte
    reste=len(text)%16
    nbrLigne=len(text)//16+1

    i=1 # Itérateur de ligne
    while i<nbrLigne:

        ## Si un mot est coupé en 2
        if (text[i*16-1] != " ") and (text[i*16-1] != ",") and (text[i*16-1] != "!") and (text[i*16-1] != "?") and (text[i*16-1] != ":") and (text[i*16] != " "):
            decalage=1 # Invariant
            caractere=text[i*16-1-decalage]

            # Comptons le nombre de caractère à décaler à la ligne
            while (caractere != " ") and (decalage < 15):
                decalage+=1
                caractere=text[i*16-1-decalage]

            # Cas Particulier : Le mot est plus long que 16 caractères
            if (decalage == 15) and ((caractere != " ") or (text[i*16+1] != " ")):
                text=text[:i*16-1]+"-"+text[i*16-1:]
                nbrLigne=nbrLigne+(reste+1)//16
                reste=(reste+1)%16

            # Cas Usuel : On décale le mot à la ligne
            else :
                text=text[:i*16-decalage]+"\n"+text[i*16-decalage:]
                nbrLigne=nbrLigne+(reste+decalage)//16
                reste=(reste+decalage)%16
        i+=1
                

    ### Affiche le texte et fait défiler si nécessaire jusqu'à ce que l'utilisateur agisse
    pot,bouton1,bouton2=0,False,False
    # On évalue action mais pas la première fois -> Do...While
    while not pot and not bouton1 and not bouton2:
        i=0 # Itérateur de ligne
        while i<nbrLigne and not pot and not bouton1 and not bouton2:
            lignes=text[i*16:(i+2)*16] # Caractères 0 à 31 etc             
            setText(lignes)
            i+=1
            pot,bouton1,bouton2=action(2,nbrOption,ignorer)

    return pot,bouton1,bouton2


########## TESTS ##########

#afficherLCD("16 char par lign")
#afficherLCD("Bonjour, je suis etudiant en IG,je fais mon projet FASO, dont le but est d ecrire des lignes pour ecrires des lignes")
#afficherLCD("anticonstitutionnellement")
