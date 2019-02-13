from new_serv import *
import threading
import action_potentiometre

print("on commence")
t1 = threading.Thread( target = serv, args = (12800, 1, ) )
t1.start()
print("premier thread")
t2 = threading.Thread( target  =serv, args = (5000, 2, ) )
t2.start
print("second thread")
