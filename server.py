
import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 8888))

while True:
        socket.listen(5)
        client, address = socket.accept()
        fin = False
        while not fin:
            response = client.recv(255)
            if response != "":
                print(response)
                if response == "fin":
                        fin = True

print("Close")
client.close()
stock.close()
