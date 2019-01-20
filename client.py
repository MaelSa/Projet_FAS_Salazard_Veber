# coding: utf-8

import socket

hote = "192.168.1.53"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))
string = "hey you"
stringsend = string.encode()
socket.send(stringsend)

print("Close")
socket.close()
