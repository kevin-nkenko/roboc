# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

def find(l, elem):
    """ fonction pour determiner la position d'un élément dans un tableau à deux dimensions"""
    
    for row, i in enumerate(l): 
        try:
            column = list(i).index(elem) 
        except ValueError: 
            continue
        return row, column
    return -1

#variable pour stocker la valeur de la case précédemment occupée par le robot
anciennevaleur=" "

continuer=1   



class Labyrinthe:

    """Classe représentant un labyrinthe."""
    
    
    def __init__(self, robot, obstacles): 
        self.robot = robot 
        self.grille = []
        self.obstacles= obstacles
        self.etat="encours"
        # ... 
    def CreerLabyrintheChaine(self,chaine):
        grilleBase=chaine.split("\n")
        grilleNew=[]
        for i in range(len(grilleBase)):
            grilleNew+=[[x for x in grilleBase[i]]]
        self.grille=grilleNew
 

    def __repr__(self):
        return str(self.grille)
    
    def __str__(self):
        affichage=""
        for x in self.grille:
            affichage+=''.join(x)+"\n"
        return affichage
    
    def DeplacerRobot(self,mouvement):
        try:
            global anciennevaleur
            global continuer
        
            #on recupere la position du robot 
            a,b=find(self.grille,"X")
            s,n,e,o=0,0,0,0

            #evaluation du mouvement demandé 
            if mouvement[0]=="s" or mouvement[0]=="S":
                s=int(mouvement[1:])
            if mouvement[0]=="n" or mouvement[0]=="N":
                n=int(mouvement[1:])
            if mouvement[0]=="e" or mouvement[0]=="E":
                e=int(mouvement[1:])
            if mouvement[0]=="o" or mouvement[0]=="O":
                o=int(mouvement[1:])

            #on s'assure que nous somme bien dans le cadre du labyrinthe 
            if a+s-n<len(self.grille) and a+s-n>-1 and b+e-o<len(self.grille[0]) and b+e-o>-1:
            #deplacement du robot
                if s>0:
                    for i in range(1,s+1):
                        if self.grille[a+1][b]=="O":
                            print("il y'a un mur, essayer un autre coup")
                            break
                        elif self.grille[a+1][b]=="U":
                            self.grille[a][b]=anciennevaleur
                            self.etat="termine"
                            self.grille[a+1][b]="X"
                            a+=1
                            print("vous avez gagné")
                            break
                        else: 
                            self.grille[a][b]=anciennevaleur
                            anciennevaleur=self.grille[a+1][b]
                            self.grille[a+1][b]="X"
                            a+=1

                if n>0:                       
                    for i in range(1,n+1):
                        if self.grille[a-1][b]=="O":
                            print("il y'a un mur, essayer un autre coup")
                            break
                        elif self.grille[a-1][b]=="U":
                            self.grille[a][b]=anciennevaleur
                            self.etat="termine"
                            self.grille[a-1][b]="X"
                            a-=1
                            print("vous avez gagné")
                            break
                        else:
                            self.grille[a][b]=anciennevaleur
                            anciennevaleur=self.grille[a-1][b]
                            self.grille[a-1][b]="X"
                            a-=1

                if e>0:
                    for i in range(1,e+1):
                        if self.grille[a][b+1]=="O":
                            print("il y'a un mur, essayer un autre coup")
                            break
                        elif self.grille[a][b+1]=="U":
                            self.grille[a][b]=anciennevaleur
                            self.etat="termine"
                            self.grille[a][b+1]="X"
                            b+=1
                            print("vous avez gagné")
                            break
                        else:
                            self.grille[a][b]=anciennevaleur
                            anciennevaleur=self.grille[a][b+1]
                            self.grille[a][b+1]="X"
                            b+=1

                if o>0:
                    for i in range(1,o+1):
                        if self.grille[a][b-1]=="O":
                            print("il y'a un mur, essayer un autre coup")
                            break
                        elif self.grille[a][b-1]=="U":
                            self.grille[a][b]=anciennevaleur
                            self.etat="termine"
                            self.grille[a][b-1]="X"
                            b-=1
                            print("vous avez gagné")
                            break
                        else:
                            self.grille[a][b]=anciennevaleur
                            anciennevaleur=self.grille[a][b-1]
                            self.grille[a][b-1]="X"
                            b-=1

            else:
                print("ce mouvement n'est pas permis")
            if s+n+e+o==0: print("Votre saisie semble incorrecte")
            
        except:
            print("Votre saisie semble incorrecte")
                
            
            
            
    
        
