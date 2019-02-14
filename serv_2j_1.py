import socket
import time

def serv_j1(port):
    print("ON LANCE LE SEEEERVEUUUUUR")
    port = port
    global received1
    global received2
    global takecount1
    global takecount2

    received1 = False
    received2 = False
    takecount1 = True
    takecount2 = True

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind(('', 5000))
    conn.listen(5)

    client, adress = conn.accept()
    print("wewconnect")
    end = False



    while not end:
        received = client.recv(255).decode()
        print(received)
        if received == "True":
            received1 = True
            takecount1 = False
        if received2 and not takecount2:
            client.send("True".encode())
            takecount2 = True
        else:
            client.send("False".encode())




def serv_j2(port):
    print("ON LANCE LE SEEEERVEUUUUUR")

    port = port
    global received1
    global received2
    global takecount1
    global takecount2

    received1 = False
    received2 = False
    takecount1 = True
    takecount2 = True

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind(('', 12800))
    conn.listen(5)
    print("att")
    client, adress = conn.accept()
    print("wewconnect")
    end = False



    while not end:
        received = client.recv(255).decode()
        print(received)
        if received == "True":
            received2 = True
            takecount2 = False
        if received1 and not takecount1:
            client.send("True".encode())
            takecount1 = True
        else:
            client.send("False".encode())
