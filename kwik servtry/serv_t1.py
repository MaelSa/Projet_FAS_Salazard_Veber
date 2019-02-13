import socket

hote = ''
port2 = 5000
port1 = 12800

conn1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn1.bind((hote, port1))
conn1.listen(5)

conn2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn2.bind((hote, port2))
conn2.listen(5)

client1, adress1 = conn1.accept()
client2, adress2 = conn2.accept()
print("wewconnect")
end = False

br1 = False
br2 = False


while not end:
    print("that'sok")
    received1 = client1.recv(255).decode()
    print(received1)
    received2 = client2.recv(255).decode()
    print(received2)
    if received1 == "True":
        client2.send("True".encode())
    else:
        client2.send("False".encode())
    if received2 == "True":
        client1.send("True".encode())
    else:
        client1.send("False".encode())
