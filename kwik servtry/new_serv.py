import socket
import _thread

def serv(port, num_client):
    print("ON LANCE LE SEEEERVEUUUUUR")
    hote = ''
    port = port
    global received1
    global received2
    global takecount1
    global takecount2

    received1 = 0
    received2 = 0
    takecount1 = 0
    takecount2 = 0

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((hote, port))
    conn.listen(5)

    client, adress = conn.accept()
    print("wewconnect")
    end = False

    br1 = False
    br2 = False


    while not end:
        received = client.recv(255).decode()
        print(received)
        if received == "True":
            if num_client == 1:
                received1 = "True"
                takecount1 = 1
            else:
                received2 = "True"
                takecount2 = 1
        if num_client == 1 and received2 == "True" and takecount2 == 1:
            client.send("True".encode())
            takecount2 = 0
        elif num_client == 2 and received1 == "True" and takecount1 == 1:
            client.send("True".encode())
            takecount1 = 0
        else:
            client.send("False".encode())
