
import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 8888))
finfin = False
c = 0
while not finfin:
        socket.listen(1)
        client, address = socket.accept()
        fin = False
        while not fin:
            response = client.recv(255)
            if response != "b''":
                print(response)
                c += 1
                if c > 3:
                    fin = True
                    finfin = True


print("Close")
client.close()
stock.close()
