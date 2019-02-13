from Mode_2_joueurs_func import *
from client_2j import *

import threading
def main_2j(num_client):
    port = [12800, 5000]
    print("on commence")
    t1 = threading.Thread( target = client_2j, args = (port[num_client], "192.168.1.53", ) )
    t1.start()
    print("premier thread")
    t2 = threading.Thread( target  = executer_mode_2, args = ( ) )
    t2.start
    print("second thread")
