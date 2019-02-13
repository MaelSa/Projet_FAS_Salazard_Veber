def client1():
    import socket
    import time
    from grovepi import *
    hote = "192.168.1.53"
    port = 12800

    ledr = False
    ledb = False

    end = False
    print("oui ?")
    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    print("Connexion établie avec le serveur sur le port {}".format(port))
    while not end:
        messtosend = input("What ?")
        connexion_avec_serveur.send(messtosend.encode())
        recev = connexion_avec_serveur.recv(255).decode()
        if recev == "True":
            print("LA REPONSE EST BONNE")
            digitalWrite(4,1)
            time.sleep(1)
            digitalWrite(4,0)
        if recev == "False":
            print("LA REPONSE EST FAUSSE")
        print(recev)
