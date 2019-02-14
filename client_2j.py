def client_2j(port, ip):
    import socket
    import time
    hote = ip
    port = port

    global bonne_rep
    bonne_rep = False
    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    end = False
    print("we got connected but")
    while not end:
        
        if bonne_rep:
            print("there's a good rep")
            connexion_avec_serveur.send("True".encode())
            bonne_rep = False
        else:
            connexion_avec_serveur.send("False".encode())
        recev = connexion_avec_serveur.recv(255).decode()
        if recev == "True":
            digitalWrite(4,1)
            time.sleep(1)
            digitalWrite(4,0)
