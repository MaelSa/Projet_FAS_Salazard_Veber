from new_serv import *
import _thread
print("on commence")
_thread.start_new_thread( serv, (12800, 1, ) )
print("premier thread")
_thread.start_new_thread( serv, (5000, 2, ) )
print("second thread")
