def read(filename):
    file = open(filename)

    dim = int(file.readline())
    grid = []

    for i in range(dim**2):
        line = file.readline().split('\n')[0].split(' ')
        for j in range(dim**2):
            if int(line[j]) != 0:
                grid.append((i, j, int(line[j])))

    file.close()

    return dim, grid


if __name__ == "__main__":
    n, initial_grid = read('sudoku_16_16_1.txt')

from random import randint

def LireValeurs(n):
    ligne = []
    tuples = []

    
    for i in range(0, len(n),+1):
        tuples = n[i]
        
        ligne += [tuples[2], ]
        
        
        
    return ligne;
    

def cree_ligne(n):
  ligne = []

  for i in range(n):
    ligne.append(0)

  return ligne

def init_grille(n):
  
  grille = []

  for i in range(n):
    grille.append(cree_ligne(n))

  return grille

def ligne_aleatoire(n):
    ligne = []
    tuples = []

    
    for i in range(0, len(n),+1):
        tuples = n[i]
        ligne += [tuples[0], ]
        
        
        
    return ligne;

def colonne_aleatoire(n):
    colonne = []
    tuples = []

    
    for i in range(0, len(n),+1):
        tuples = n[i]
        colonne += [tuples[1], ]

        
        
    return colonne;


def affiche_grille(grille):
  dim = len(grille)

  for i in range(dim):
    for j in range(dim):
        print(grille[i][j], end=' ')
    print()
    
def verifier_chiffre(reponse):
    
    for i in range(0, len(reponse), +1):
        if reponse[i] <'0' or reponse[i] > '9':
        
            return False
    
    return True;
    
    
    
def verifier_reponse(reponse, grille):
    limite = len(grille)
    answer = True
    valeur_test=0
    
    if verifier_chiffre(reponse) == False:
        answer = False
    
    if answer != False:
        valeur_test = int(reponse)
        
    if valeur_test > limite or valeur_test < 0:
        answer = False
    
    
    return answer;
    
        
 
def sudoku():
        
    ligne_alea = ligne_aleatoire(initial_grid)
    
    colonne_alea = colonne_aleatoire(initial_grid)

    valeurs=LireValeurs(initial_grid)
 
    grille = init_grille(n*n)
   
    
    answer = True;
  
    for i in range(0, len(ligne_alea), +1):

        grille[ligne_alea[i]][colonne_alea[i]] = valeurs[i]
    
    affiche_grille(grille)
    
    for i in range(100):
    
        ligne = input("Entrez une ligne : ")
        
        while verifier_reponse(ligne, grille) == False:
             ligne = input("Cette ligne n'existe pas, choississez en une autre : ")
        
        ligne = int(ligne)
                 
        colonne = input("Entrez une colonne : ")
    
        while verifier_reponse(colonne,grille) == False:
            colonne = input("Cette colonne n'existe pas, choissisez en une autre : ")
            
        colonne = int(colonne)
    
        valeur = input("Entrez un chiffre : ")
    
        while verifier_reponse(valeur, grille) == False:
            valeur = input("Ce chiffre est incorrect, choissisez en un autre : ")
        
        valeur = int(valeur)
            
        for i in range(0,3,+1):
        
            if grille[ligne][colonne] == grille[ligne_alea[i]][colonne_alea[i]]:
                    answer=False    
                    
        if answer==False:
             print("Vous ne pouvez pas modifier cette case.");
                    
        if answer == True:
            grille[ligne][colonne] = valeur
             
        affiche_grille(grille)
        
        answer=True;

    





 
sudoku()




    

