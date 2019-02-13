from basic import *
import time
import threading
t1 = threading.Thread(target=flac, args=("waww",))
t1.start()
time.sleep(0.5)
t2 = threading.Thread(target=flac, args=("lezl",))
t2.start()
