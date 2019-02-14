from serv_2j_1 import *
import threading

def serveur_2joueurs():
    t1 = threading.Thread( target = serv_j1 , args = (5000, ))
    t1.start()
    print("go,")

    t2 = threading.Thread( target = serv_j2 , args = (12800, ))
    t2.start()
    print("g2")
serveur_2joueurs()
