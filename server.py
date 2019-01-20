
import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 8888))

while True:
        socket.listen(5)
        while true:

                client, address = socket.accept()
                print("{} connected".format( address ))

                response = client.recv(255)
                if response != "":
                        print(response)

print("Close")
client.close()
stock.close()
