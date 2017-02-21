# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
import os
os.chdir("/Users/mac/Downloads/roboc")
from labyrinthe import*


class Carte(Labyrinthe):

    """Objet de transition entre un fichier et un labyrinthe."""
    

    def __init__(self, nom, chaine):
        self.nom = nom
        Labyrinthe.__init__(self,"x","0")
        self.CreerLabyrintheChaine(chaine)
        

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def Save(self):
        
        """methode permettant d'enregistrer une nouvelle carte dans un fichier"""
        chaine = ""
        for x in self.grille:
            chaine+=''.join(x)+"\n"
        if self.nom.endswith("."):
            chemin = os.path.join("cartes",self.nom+"txt")
        else:
            chemin = os.path.join("cartes",self.nom+".txt")
        with open(chemin, 'w') as fichier:
                fichier.write(chaine)
        
        
        
