
import socket
import time
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 8888))
finfin = False
c = 0
print("ok")
while not finfin:
        socket.listen(5)
        print("Serveur lancé")
        client, address = socket.accept()

        fin = False
        c = 0
        while not fin:
            print("Serveur connecté")
            response = client.recv(255)
            if response != "b''":
                print(response)
                c += 1
                if c > 6:
                    fin = True
                    finfin = True

time.sleep(10)
print("Close")
client.close()
stock.close()
