import socket
import threading
import time

def serv_mono(port, ip):
    hote = ip
    port = port

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((hote, port))
    conn.listen(5)

    client, adress = conn.accept()
    print("we're connected")
    t1 = time.time()
    end = False
    
    while not end:
        received = client.recv(255).decode()
        print(received)
        num = ["0","1","2","3","4","5","6","7","8","9"]
        if received[0] in num:
            print("it happened guys")
            t2 = time.time()
            score = int(received)
            temps = t2 - t1
            end = True

    print("Score : ", score)
    print("Temps : ", temps)

    while 1:
        a = input("finished")

serv_mono(5000, '')
