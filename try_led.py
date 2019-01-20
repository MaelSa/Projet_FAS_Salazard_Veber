from grovepi import *
import time
led_rouge = 4
led_bleue = 7

pinMode(led_bleue, "OUTPUT")
pinMode(led_rouge, "OUTPUT")

time.sleep(1)

digitalWrite(led_rouge, 1)
digitalWrite(led_bleue, 1)