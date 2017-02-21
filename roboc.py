# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import pickle
import os
#vous pouveez décocher la commande suivante et renseigner un changement de repertoire
#os.chdir("/Users/mac/Downloads/roboc")

from carte import*

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            
            # Création d'une carte
            cartes+=[Carte(nom_carte,contenu)]


# Si il y a une partie sauvegardée, le bloc try est exécuté sinon on cree ouvre une nouvelle carte

try:
    chemin = os.path.join("cartes", "partiesenregistrees.xyz")
    if os.path.isfile(chemin):
        with open(chemin, 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            carteEnJeu = mon_depickler.load()
            reponse=raw_input("voulez vous continuer la partie enregistrée? O/N ")
            while 1:
                if reponse=="O" or reponse=="o" :               
                    break
                elif reponse=="n" or reponse=="N" :
                    raise EOFError(" nouvelle partie")
                    break
    else:
        raise EOFError(" nouvelle partie")
                

except EOFError:
        # On affiche les cartes existantes
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))
    print(" ")
                      
    partie=0
    while(not partie):
        try:
            partie=int(raw_input("Entrez un numéro de labyrinthe pour commencer à jouer une nouvelle partie: "))
            if partie not in range(1, len(cartes)+1):
                print("Saisie invalide")
                partie=0
            else:
                carteEnJeu=cartes[partie-1]
        except:
            print("Saisie invalide")
            partie=0
    

# ... Complétez le programme ...



while carteEnJeu.etat=="encours": 
    print(carteEnJeu)
    deplacement=raw_input("Entrez votre déplacement ou entrez Q pour enregister et quitter: ")
    if deplacement == "q" or deplacement =="Q":
        print("A bientot pour une autre partie")
        break
    else:
        carteEnJeu.DeplacerRobot(deplacement)
        print(" ")
    chemin = os.path.join("cartes", "partiesenregistrees.xyz")
    with open(chemin, 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(carteEnJeu)
    
print(carteEnJeu)
if carteEnJeu.etat=="termine":
    os.remove(chemin)
    
       