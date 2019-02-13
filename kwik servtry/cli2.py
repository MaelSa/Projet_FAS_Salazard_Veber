def client2():

    import socket
    import time
    hote = "localhost"
    port = 5000

    ledr = False
    ledb = False

    end = False

    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    print("Connexion établie avec le serveur sur le port {}".format(port))
    while not end:
        messtosend = input("What ?")
        connexion_avec_serveur.send(messtosend.encode())
        recev = connexion_avec_serveur.recv(255).decode()
        if recev == "True":
            print("LA REPONSE EST BONNE")
        if recev == "False":
            print("LA REPONSE EST FAUSSE")
        print(recev)

client2()
