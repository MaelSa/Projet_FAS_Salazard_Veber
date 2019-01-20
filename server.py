
import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 8888))
finfin = False
c = 0
print("ok")
while not finfin:
        socket.listen(1)
        print("ok")
        client, address = socket.accept()
        print("ok")
        fin = False
        while not fin:
            print("ok2")
            response = client.recv(255)
            if response != "b''":
                print(response)
                #c += 1
                #print(c)
                #if c > 3:
                #    fin = True
                #    finfin = True


print("Close")
client.close()
stock.close()
