from render import *
from tkinter import *
from math import *

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

#La fonction "lire_valeurs" sert à récupérer les valeurs des cases préremplies au début du sudoku.

def lire_valeurs(initial_grid):
    valeurs = []

    #"i" parcourt l'ensemble des listes se trouvant dans la liste "initial_grid" et la liste "valeurs" en récupère la valeur se trouvant à l'indice 2, qui correpsond à la valeur de la case.
    for i in initial_grid:
        
        valeurs += [i[2], ]       
        
    return valeurs;

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

#La fonction "ligne_bloquee" sert à récupérer les numéros de lignes où doivent se trouver les valeurs des cases non modifiables.

def ligne_bloquee(initial_grid):
    ligne = []

    #"i" parcourt l'ensemble des listes se trouvant dans la liste "initial_grid" et la liste "ligne" en récupère la valeur se trouvant à l'indice 0, qui correpsond à la ligne de la case.
    for i in initial_grid:

        ligne += [i[0], ]     
        
    return ligne;

#La fonction "colonne_bloquee" sert à récupérer les numéros de colonnes où doivent se trouver les valeurs des cases non modifiables.

def colonne_bloquee(initial_grid):
    colonne = []
    
    #"i" parcourt l'ensemble des listes se trouvant dans la liste "initial_grid" et la liste "colonne" en récupère la valeur se trouvant à l'indice 1, qui correpsond à la colonne de la case.
    for i in initial_grid:
        
        colonne += [i[1], ]
               
    return colonne;


def affiche_grille(grille):
  dim = len(grille)

  for i in range(dim):
    for j in range(dim):
        print(grille[i][j], end=' ')
    print()
    
#La fonction "verifier_chiffre" sert à vérifier que le caractère passé en paramètre est bien un chiffre.   
    
def verifier_chiffre(reponse):
    
    #i parcourt chaque caractère de la chaine "reponse" et si l'un d'eux n'est pas un chiffre (compris entre le caractère '0' et le caractère '9') alors la fonction renvoie false.
    for i in reponse:
        if i <'0' or i > '9':

            return False
    
    return True;

#La fonction "verifier_nb" sert un véfifier que le nombre entier passé en paramètre correspond bien au nombre 4, 9 ou 16.

def verifier_nb(nb):
    
    if nb != '4' and nb != '9' and nb != '16':
        return False
    
    return True;

#La fonction "verifier_reponse_ligne" sert à vérifier que la valeur entrée en paramètre dans réponse permet bien de sélectionner une ligne de la grille passée en paramètres.
    
def verifier_reponse_ligne(reponse, grille):
    limite = len(grille)-1
    answer = True
    valeur_test=0
    
    #Si "reponse" est vide alors la fonction renvoie True et, de cette manière, recommence au début.
    if reponse == "":
        return True
    
    if verifier_chiffre(reponse) == False:
        print("Ceci n'est pas un nombre correct. Veuillez entrez un nombre entier positif.")
        answer = False
    
    #Si la réponse est bien un nombre, alors on la convertit en entier.
    if answer != False:
        valeur_test = int(reponse)
     
    #On vérifie que la réponse est en adéquation avec le nombre de lignes dans la grille. 
    if valeur_test > limite or valeur_test < 0:
        print("Cette ligne n'existe pas. Veuillez entrez un numéro de ligne correct.")
        answer = False
    
    
    return answer;

#La fonction "verifier_reponse_colonne" sert à vérifier que la valeur entrée en paramètre dans réponse permet bien de sélectionner une colonne de la grille passée en paramètres.

def verifier_reponse_colonne(reponse, grille):
    limite = len(grille)-1
    answer = True
    valeur_test=0
    
    if reponse == "":
        return True
    
    if verifier_chiffre(reponse) == False:
        print("Ceci n'est pas un nombre correct. Veuillez entrez un nombre entier positif.")
        answer = False
    
    if answer != False:
        valeur_test = int(reponse)
        
    if valeur_test > limite or valeur_test < 0:
        print("Cette colonne n'existe pas. Veuillez entrez un numéro de ligne correct.")
        answer = False
    
    
    return answer;

#La fonction "verifier_reponse_valeur" sert à vérifier que la valeur que souhaite inscrire le joueur dans une des cases du sudoku est valable ou non.

def verifier_reponse_valeur(reponse, grille, liste):
    limite = len(grille)
    answer = True
    valeur_test=0
    
    if reponse == "":
        return True
    
    elif verifier_chiffre(reponse) == False:
        print("Ce nombre n'est pas valide. Veuillez entrez un nombre entier positif.")
        return False
    
    elif answer != False:
        valeur_test = int(reponse)
        
    #Si le joueur tente d'entrer une valeur qui ne se trouve pas dans la liste "liste" passée en paramètres alors la fonction renvoie false.    
    if answer == True:
        for i in liste:
        
            if int(reponse) == i:
                return True
            else:
                
                answer = False
        
    if answer == False:
        print("Ce nombre n'est pas valide. Choississez un nombre parmis ceux qui vous sont proposés.")
        
    return answer;

#La fonction "recuperer_colonne" sert à récupérer, dans une grille entrée en paramètres, la colonne où se trouve l'indice entrée en paramètres.
    
def recuperer_colonne(grille, indice):
    colonne = []
    
    #"e" parcout chaque liste contenue dans la liste "grille" et colonne récupère la valeur de chaque liste se trouvant à l'indice "indice" entrée en paramètres.
    for e in grille:
         
         colonne += [e[indice], ]

        
    return colonne

#La fonction "recuperer_valeurs_bloc4" sert à récuper les valeurs d'un bloc colonne par colonne danns une grille de 4 lignes.
def recuperer_valeurs_bloc4(liste, colonne_jouee):
        
        bloc = []
        
        #On regarde dans quel bloc le joueur a joué et on en stocke les valeurs dans la variable "bloc".
        if colonne_jouee==0 or colonne_jouee ==1:
            for e in range(0, 2):
                bloc += [liste[e], ]
        
        else:
            for e in range(2, 4):
                bloc += [liste[e], ]
                
        return bloc
    
def recuperer_valeurs_bloc9(liste, colonne_jouee):
        
        bloc = []
        
        if 0<=colonne_jouee<=2:
            for e in range(0, 3):
                bloc += [liste[e], ]
        
        elif 3<=colonne_jouee<=5:
            for e in range(3, 6):
                bloc += [liste[e], ]
                
        else:
            for e in range(6, 9):
                bloc += [liste[e], ]
                
        return bloc
    
def recuperer_valeurs_bloc16(liste, colonne_jouee):
        
        bloc = []
        
        if 0<=colonne_jouee<=3:
            for e in range(0, 4):
                bloc += [liste[e], ]
                       
        elif 4<=colonne_jouee<=7:
            for e in range(7, 8):
                bloc += [liste[e], ]
                
        elif 8<=colonne_jouee<=12:
            for e in range(8, 13):
                bloc += [liste[e], ]        
                
        else:
            for e in range(13, 16):
                bloc += [liste[e], ]
                
        return bloc
    

#La fonction "recuperer_bloc" sert à récupérer, dans une grille entrée en paramètres, les valeurs qui correspondent, dans le sudoku, au bloc où se trouve l'indice entrée en paramètres.

def recuperer_bloc(grille, ligne_jouee, colonne_jouee):
    
    bloc = []
    bloc_maj = []
    
    #On regarde sur une grille de combien de lignes joue le joueur et on va récupérer les valeurs du bloc ligne par ligne.
    if len(grille[0])==4:
        
        #On regarde dans quel bloc le joueur a joué et on en stocke les valeurs dans la variable "bloc".
        if ligne_jouee==0 or ligne_jouee ==1:
            for e in range(0, 2):
                liste = grille[e]
                
                bloc += [recuperer_valeurs_bloc4(liste, colonne_jouee), ] 
    
        else:
            for e in range(2, 4):
                liste = grille[e]
                
                bloc += [recuperer_valeurs_bloc4(liste, colonne_jouee), ]    
                        
    if len(grille[0])==9:
            
        if 0<=ligne_jouee<=2:
            for e in range(0, 3):
                liste = grille[e]
                
                bloc += [recuperer_valeurs_bloc9(liste, colonne_jouee), ]  
                
        elif 3<=ligne_jouee<=5:
            for e in range(3, 6):
                liste = grille[e]
                
                bloc += [recuperer_valeurs_bloc9(liste, colonne_jouee), ]
                
        else:
            for e in range(6, 9):
                liste = grille[e]
                
                bloc += [recuperer_valeurs_bloc9(liste, colonne_jouee), ]
                
    if len(grille[0])==16:
            
        if 0<=ligne_jouee<=3:
            for e in range(0, 4):
                liste = grille[e]
                
                bloc += [recuperer_valeurs_bloc16(liste, colonne_jouee), ]
                
        elif 4<=ligne_jouee<=7:
            for e in range(4, 8):
                liste = grille[e]
                
                bloc += [recuperer_valeurs_bloc16(liste, colonne_jouee), ]
                
        elif 8<=ligne_jouee<=11:
            for e in range(8, 12):
                liste = grille[e]
                
                bloc += [recuperer_valeurs_bloc16(liste, colonne_jouee), ]
                
        else:
            for e in range(12, 16):
                liste = grille[e]
                
                bloc += [recuperer_valeurs_bloc16(liste, colonne_jouee), ]
    
    #On stocker l'ensemble des valeurs de chaque ligne du bloc au sein d'une seule liste qu'on stocke dans la variable "block_maj".
    for liste in bloc:
        for element in liste:
            bloc_maj += [element, ]
    
    
    return bloc_maj
        

#La fonction "proposer_nombres" sert à sélectionner les nombres qui peuvent être joués par la joueur dans une case qui a préalablement sélectionné.

def proposer_nombres(grille, ligne_jouee, colonne_jouee):
    analyser_grille = grille[ligne_jouee]
    nombres_possibles = [0,]
    nombres_ligne = []
    min = 0
    answer = True
    colonne = recuperer_colonne(grille, colonne_jouee)
    bloc = recuperer_bloc(grille, ligne_jouee, colonne_jouee)
    
    #On récupère la valeur minimale de la ligne où se trouve la case où veut jouer le joueur. 
    for e in analyser_grille:
        if min>e:
            min = e
    
    #On récupère l'ensemble des nombres se trouvant dans la ligne où le joueur veut jouer et on les stocker dans la variable "nombres_ligne".
    for e in analyser_grille:
        if e != 0:
            nombres_ligne += [e, ]
    
    #On prend l'ensemble des valeurs entres "min" et la longueur de la grille et pour chacune on vérifie qu'elle ne se trouve pas déjà dans la liste, la colonne et le bloc et si c'est le cas on l'ajoute à la lite "nombres_possibles".
    for e in range(len(analyser_grille)):
        min +=1

        for e in nombres_ligne:
            if min ==e:
                answer = False
        for e in colonne:
            if min ==e:
                answer = False
        for e in bloc:
            if min ==e:
                answer = False
        if answer == True:
            nombres_possibles += [min, ]
        answer = True
    
    
            
    return nombres_possibles

#La fonction "afficher_nombres" sert à afficher les valeurs d'une liste passée en paramètres.

def afficher_nombres(l):
    dim = len(l)

    for i in range(dim):
        print(l[i], end=' ')
    print()
    
#La fonction "jouer_suduko_valeur" permet de sélectionne une ligne et une colonne d'une grille et d'inscrire une valeur dans la case qui s'y trouve.    
    
def jouer_sudoku_valeur(grille):
        
    ligne = input("Entrez une ligne ou appuyez sur Entrée pour annuler : ")
    
    while verifier_reponse_ligne(ligne, grille) == False:
        ligne = input("Entrez une ligne ou appuyez sur Entrée pour annuler : ")
    
    #Si la ligne est vide, cela veut dire que le joueur a appuyé sur "Entrée" et qu'il souhaite donc annuler le coup, on rénitialise donc l'ensemble des variables.
    if ligne =="":
        colonne, valeur = "", ""
        return ligne, colonne, valeur
     
    colonne = input("Entrez une colonne ou appuyez sur Entrée pour annuler : ")
    
    while verifier_reponse_colonne(colonne,grille) == False:
        colonne = input("Entrez une colonne ou appuyez sur Entrée pour annuler : ")
        
    if colonne =="":
        valeur =""
        return ligne, colonne, valeur
            
            
    nombres_possibles = proposer_nombres(grille, int(ligne), int(colonne))
       
    print("Vous pouvez jouer ces nombres : "), afficher_nombres(nombres_possibles)
        
    
    valeur = input("Entrez un chiffre ou appuyez sur Entrée pour annuler  : ")
    
    while verifier_reponse_valeur(valeur, grille, nombres_possibles) == False:
        valeur = input("Entrez un chiffre ou appuyez sur Entrée pour annuler  : ")
        

    return ligne, colonne, valeur

#La fonction "lire_grille" vérifie qu'il n'y a pas de zéro dans la grille passée en paramètres et renvoie false si c'est le cas.

def lire_grille(grille):
    
    for i in grille:
        for e in i:
            if e == 0:
                return False
            
    return True

#La fonction "nb_cases" sert à comopter le nombre de cases comportant des zéros dans la grille passée en paramètres. 

def nb_cases(grille):
    nb_cases = 0
    
    for i in grille:
        for e in i:
            if e == 0:
                nb_cases +=1
                
    print("Il reste "+ str(nb_cases) + " cases à remplir.")
                
    return nb_cases

#La fonction "annuler_coup" permet d'annuler le coup joué précédemment à partir de l'historique. 

def annuler_coup(grille, historique, annuler):
    
    #Si la case où a joué le joueur précedemment était vide (donc un 0), il faut réecrire un "?". Sinon on récrit l'ancienne valeur tout simplement.
    if  historique[3][len(historique[3])-1]==0:
                    
                    grille[historique[0][len(historique[0])-1]][historique[1][len(historique[1])-1]] = 0                    
                    write(historique[0].pop(), historique[1].pop(), "?", "green")
                    
    else:
                    write(historique[0].pop(), historique[1].pop(), historique[3].pop(), "blue")
                    
    historique[2].pop()
    historique[3].pop()
    if historique[0] == []:
                annuler = 'N'
    else:
                print("Le dernier coup joué ( "+str(historique[0][len(historique[0])-1]) +" , "+ str(historique[1][len(historique[1])-1])+" ) : "+str(historique[3][len(historique[3])-1])+" -> "+str(historique[2][len(historique[2])-1]))
                annuler = input("Voulez-vous l'annuler ? [O]ui / [N]on : ")
    return annuler

#La fonction "parametres_grille" permet de défininir l'ensemble des paramètres de la grille qui servira au joueur à jouer au sudoku.

def parametres_grille():
    
    nb = input("Sur combien de lignes voulez vous jouer ? 4, 9 ou 16 ? :")
    
    while verifier_nb(nb) == False:
        nb = input("Cette reponse n'est pas correcte, veuillez choisir 4, 9 ou 16 :")
        
    if nb =='4':
        n, initial_grid = read('sudoku_4_4_1.txt')
    if nb=='9':
        choix = input("Voulez jouer  sur le Soduku '1' ou '2' ?")
        while choix != "1" and choix != "2":
            choix = input("Cette réponse n'est pas correcte. Veuillez écrire '1' ou '2' : ")
        if choix == "1" or choix =="2":
            n, initial_grid = read('sudoku_9_9_'+str(choix)+'.txt')
    if nb=='16':
        choix = input("Voulez jouer  sur le Soduku '1' ou '2' ?")
        while choix != "1" and choix != "2":
            choix = input("Cette réponse n'est pas correcte. Veuillez écrire '1' ou '2' : ")
        if choix == "1"  or choix =="2":
            n, initial_grid = read('sudoku_16_16_'+str(choix)+'.txt')
    
    nb = int(nb)
    
    nb = sqrt(nb)
    
    nb = int(nb)
    
    draw_sudoku_grid(nb)
    
    grille = init_grille(n*n)
    
    ligne_bloq = ligne_bloquee(initial_grid)
    
    colonne_bloq = colonne_bloquee(initial_grid)
        
    valeurs=lire_valeurs(initial_grid)
        
    grille = dessiner_grille(initial_grid, ligne_bloq, colonne_bloq, valeurs, grille)
    
    return grille, ligne_bloq, colonne_bloq

#La fonction "dessiner_grille" permet de remplir le sudoku initiale à l'aide de la fonction "write" du module render. 
    
def dessiner_grille(initial_grid, ligne_bloq, colonne_bloq, valeurs, grille):
     
     #On commencer par mettre des "?" sur l'ensemble du sudoku.
     for i in range(0, len(initial_grid), +1):
            ligne =i
            
            for i in range(0, len(initial_grid), +1):
    
               colonne=i
               write(ligne, colonne, "?", "green")
     
     #On place ensuite les valeurs prédéfinies.
     for i in range(0, len(initial_grid), +1):
       
            write(ligne_bloq[i], colonne_bloq[i], valeurs[i], "red")
            grille[ligne_bloq[i]][colonne_bloq[i]] = valeurs[i]
            
     return grille
    
#La fonction "freecells" récupère l'indice d'une case dans la grille (ligne et cologne) au sein d'une liste quand celle-ci est vide et la stocke dans la variable "freecells".   
def freecells(grille):
    
    freecells = []
    case=[]
    pos_ligne = 0
    pos_colonne = 0
    
    #Si la case contient "0", on la stocke dans une liste "case" puis on stocke cette liste dans la variable "freecells".
    for liste in grille:
        for element in liste:
            if element == 0:
                case += [[pos_ligne, pos_colonne] ]
                freecells += case
            pos_colonne += 1
        pos_colonne = 0
        pos_ligne +=1
    
    return freecells

#La fonction "résolution_automatique" résout automatiquement la grille passée en paramètres.
def resolution_automatique(grille):
    
    #A chaque fois que la fonction est appelée, on stocker l'ensemble des cases diposnibles dans la variable "cases_dispos". De cette manière, avec la récusivité, on pourra avancer case par case au sein de la grille.
    cases_dispo = freecells(grille)
    
    #Si la variable "cases disponibles" est vide, cela signifie qu'il n'y pas plus de cases disponibles et donc que le sudoku est résolu. On arrête la fonction en renvoyant True.
    if len(cases_dispo) == 0:
        return True
    
    ligne = cases_dispo[0][0]
    colonne = cases_dispo[0][1]
    
    #On commence par calculer l'ensemble des solutions possibles pour la première case libre du sudoku.
    nombres_possibles = proposer_nombres(grille, int(ligne), int(colonne))
    
    #Pour l'ensemble des solutions possibles, hormis 0, on va tester si cette solution permet de résoudre le sudoku.
    for e in range(1, len(nombres_possibles)):
        nombres_possibles = proposer_nombres(grille, int(ligne), int(colonne))
        grille[ligne][colonne] = nombres_possibles[e]
        write(ligne, colonne, nombres_possibles[e], "blue")
        cases_dispo = freecells(grille)
        
        #Tant que la fonction ne renvoie pas True, et donc que le sudoku n'est pas résolu, on passe à la case suivante et on répète l'opération en appeleant à nouveau la fonction.
        if resolution_automatique(grille) == True:
            return True

        #Si l'ensemble de solutions n'a pas permis de résoudre le sudoku, on assigne la valeur zéro à la case afin de la rendre à nouveau disponible et ainsi revenir en arrière.
        grille[ligne][colonne] = 0
        write(ligne, colonne, "?", "green")
        cases_dispo = freecells(grille)     
      
    
#La fonction "jouer_sudoku" est la principale fonction du programme, celle permettant de jouer au sudoku.    
 
def jouer_sudoku():
    
        grille, ligne_bloq, colonne_bloq = parametres_grille()
        
        joueur = input("Voulez-vous jouer sur le sudoku ou bien que l'ordinateur le résoude ? Ecrivez 'jouer' ou 'résoudre' : ")
        
        while joueur != "jouer" and joueur != "résoudre" and joueur != "Jouer" and joueur != "Résoudre":
            joueur = input("Cette réponse n'est pas correcte. Veuillez écrire 'jouer' ou 'résoudre' : ")
            
        if joueur == "résoudre" or joueur == "Résoudre":
            return resolution_automatique(grille)
        
        historique = [[],[],[], []]
        
        #Tant que la grille contient des 0, le joueur devra jouer.
        while lire_grille(grille)==False:
            
            nb_cases(grille)
            
            ligne = ""
            colonne = ""
            valeur = ""
            
            #Le joueur devra jouer tant que que les variables "ligne", "colonne" et "valeur" ne contiennent par un nombre.
            while ligne == "" or colonne == "" or valeur == "":
                
                ligne, colonne, valeur = jouer_sudoku_valeur(grille)
                
            
            ligne = int(ligne)
            
            colonne = int(colonne)
            
            valeur = int(valeur)
        
            answer=True
            
            #Si le joueur tente de modifier une case préremplie la fonction renvoie un message d'erreur.
            for i in range(0,len(ligne_bloq)):
        
               if ligne==ligne_bloq[i] and colonne ==colonne_bloq[i]:
                       answer=False    
                    
            if answer==False:
                 print("Vous ne pouvez pas modifier cette case.");
            
            #Une fois que le joueur a joué, on modifie la case et on on ajoute l'ensemble des informations sur le coup joué (ligne jouée, colonne jouée, valeur ajoutée, ancienne valeur de la case) dans l'historique.
            if answer == True:
                 historique[3].append(grille[ligne][colonne])
                 if valeur == 0:
                      write(ligne, colonne, "?", "green")
                 else:
                      write(ligne, colonne, valeur, "blue")
                 grille[ligne][colonne] = valeur
                 historique[2].append(valeur)
                 historique[1].append(colonne)
                 historique[0].append(ligne)
                 
            if answer == True:
                print("Le dernier coup joué ( "+str(historique[0][len(historique[0])-1]) +" , "+ str(historique[1][len(historique[1])-1])+" ) : "+str(historique[3][len(historique[3])-1])+" -> "+str(historique[2][len(historique[2])-1]))
            
                annuler = input("Voulez-vous l'annuler ? [O]ui / [N]on : ")
            
                
                while annuler != 'O' and annuler != 'N' and annuler != 'o' and annuler != 'n':
                       annuler = input("Cette réponse n'est pas valide. Veuillez choissir la lettre 'O' pour oui ou 'N' pour non.")
                   

            
                while annuler == 'O' or annuler == 'o' and historique[0] != []:
                    annuler = annuler_coup(grille, historique, annuler)
                
            answer=True;
             
        print("Félicitations, vous avez rempli ce sudoku !")
        
        wait_quit()
        
        

jouer_sudoku()
        
    






