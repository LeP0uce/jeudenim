from random import randint                  #Importation de la fonction randint 
class Marienbad:                            #Création de la classe Marienbad
    def __init__(self, allumettes= [1,2,3,4,5,6], joueurs= ("joueur1", "joueur2"), tas= (1,2,3,4,5,6), tour= 0 ):    #Creation du constructeur
        self.joueurs = joueurs              #attributs
        self.tas = tas
        self.allumettes = allumettes
        self.tour= tour

    def __str__(self):                      #retourne les informations du jeu grace à la méthode __str__
        return "Tas: "+str(self.tas)+"\n\nAllumettes: "+str(self.allumettes)+"\n\nProchain joueur: "+str(self.joueurs[self.tour])

    def verifie(self, n, t):            #création de la méthode verifie qui vérifie s'il y a n allumettes dans un tas t 
        if t>=1 and t<=6:
            if self.allumettes[t-1]!=0:
                if n>=1 and n<=self.allumettes[t-1]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def enlever(self, n, t):        #création de la méthode enlever qui retire n allumettes dans un tas t 
        self.allumettes[t-1] -= n

    def termine(self):          #création de la méthode termine qui fait en sorte que le jeu se termine quand il n'y a plus de n allumettes
        if self.allumettes==[0,0,0,0,0,0]:
            return True
        else:
            return False

def joueur_vs_joueur():         #création de la méthode joueur_vs_joueur qui lance le jeu entre un joueur et un autre 
    j1=input("quel est le nom du joueur 1 ? ")
    j2=input("quel est le nom du joueur 2 ? ")
    pr=randint(0,1)         #choisit un chiffre entre 0 et 1 pour determiner qui va commencer
    jeu=Marienbad(allumettes= [1,2,3,4,5,6], joueurs= (j1,j2), tour= pr)        #définit le jeu grace à la classe Marienbad
    jeu.joueurs=(j1, j2)    #ajoute les joueurs au jeu
    
    if pr==0:       #determine quel joueur commencera en premier
        print (j1, "Commencera à jouer en premier")
    else:
        print (j2, "Commencera à jouer en premier")
        

    while jeu.termine()== False:    #boucle while où tant que le jeu n'est pas terminé, le jeu continue
        print(jeu)
        t=float(input("Choisissez un tas entre 1 et 6: ")) #demande aux joueurs de choisir un tas entre 1 et 6
        t=int(t)
        
        if t<1 or t>6: 
            while t<1 or t>6:
                t=float(input("Erreur, vous ne savez pas lire! Choisissez un tas entre 1 et 6: "))  #affiche une erreur qui redemande une valeur entre 1 et 6
                t=int(t)
        n=float(input("Choisissez un nombre d'allumettes à enlever: "))     #demande le nombre d'allumettes à retirer quand il y a une erreur dans le tas
        n=int(n)
        
        if jeu.verifie(n,t)==False:         #Tant qu'un tas est vide ou n'est pas compris entre 1 et 6, cela met une erreur et demande de remettre un autre tas autre que celui qu'on a choisi de base
            if jeu.allumettes[t-1]==0:
                while jeu.allumettes[t-1]==0:
                    t=float(input("Ce tas est vide, choisissez un autre tas entre 1 et 6: "))
                    t=int(t)
                    if t<1 or t>6:
                        while t<1 or t>6:
                            t=float(input("Erreur, vous ne savez pas lire! Choisissez un tas entre 1 et 6: "))
                            t=int(t)
                n=float(input("Choisissez un nombre d'allumettes à enlever: ")) #redemande au joueur de choisir un nouveau entier
                n=int(n)                
            if n<1 or n>jeu.allumettes[t-1]:    #Tant que le nombre d'allumettes est supérieur au tas, on demande de changer la valeur de celui-ci
                while n<1 or n>jeu.allumettes[t-1]:
                    n=float(input("Erreur, vous ne pouvez retirer qu'au maximum " + str(jeu.allumettes[t-1]) + " allumette(s) ! Choisissez un nombre entre 1 et "+str(jeu.allumettes[t-1])+": "))
                    n=int(n)
            jeu.enlever(n,t)    #Quand tout est bon, on peut enfin retirer le nombre d'allumettes n dans le tas t
        else:
            jeu.enlever(n,t)
            
        if jeu.tour%2==0:       #change la valeur pour que ce soit le tour du prochain joueur
            jeu.tour=jeu.tour+1
        else:
            jeu.tour=jeu.tour-1
            
        if jeu.termine()==True:     #S'il n'y a plus d'allumettes, le jeu se termine et on annonce le vainqueur sinon on continue à jouer
            if jeu.tour%2==0:
                return "Le gagnant est "+str(jeu.joueurs[0])
            else:
                return "Le gagnant est "+str(jeu.joueurs[1])
        else:
            continue
        

def joueur_vs_ordi_idiot():     #crée la méthode pour jouer contre l'ordinateur
    j1=input("Quel est le nom du joueur 1 ? ") #ne demande que le nom du joueur car celui de l'ordinateur est déjà défini
    j2="François Pignon"
    jeu=Marienbad(allumettes= [1,2,3,4,5,6], joueurs= (j1,j2), tour= 0) #définit le jeu grace a la classe Marienbad
    jeu.joueurs=(j1, j2)        #ajoute les joueurs au jeu
    print (j1, "Commencera à jouer en premier")     #annonce que le joueur (l'humain) va commencer en premier
    
    while jeu.termine()== False:    #lance le jeu jusqu'à ce que ça se termine 
        if jeu.tour==0:
            print(jeu)
            t=float(input("Choisissez un tas entre 1 et 6: ")) #demande de choirir un tas
            t=int(t)
            
            if t<1 or t>6:      #Tant que le tas n'est pas entre 1 et 6, on va redemander de choisir un tas entre 1 et 6
                while t<1 or t>6:
                    t=float(input("Erreur, vous ne savez pas lire! Choisissez un tas entre 1 et 6: "))
                    t=int(t)
            n=float(input("Choisissez un nombre d'allumettes à enlever: "))     #demande le nombre d'allumettes à retirer
            n=int(n)

            if jeu.verifie(n,t)==False:     #Tant que un tas est vide ou n'est pas compris entre 1 et 6, cela met une erreur et demande de remettre un autre tas autre que celui qu'on a choisi initialement
                if jeu.allumettes[t-1]==0:
                    while jeu.allumettes[t-1]==0:
                        t=float(input("Ce tas est vide, choisissez un autre tas entre 1 et 6: "))
                        t=int(t)
                        if t<1 or t>6: 
                            while t<1 or t>6:
                                t=float(input("Erreur, vous ne savez pas lire! choisissez un tas entre 1 et 6: "))
                                t=int(t)
                    n=float(input("Choisissez un nombre d'allumettes à enlever: ")) #s'il y a erreur dans le tas, on redemande le nombre d'allumettes à retirer
                    n=int(n)
                if n<1 or n>jeu.allumettes[t-1]:    #Tant que n n'est pas compris entre 1 et le nombre d'allumettes restantes dans un tas, on va demander au joueur de choisir un autre nombre qui est comprus dans celui-ci
                    while n<1 or n>jeu.allumettes[t-1]:
                        n=float(input("Erreur, vous ne pouvez retirer qu'au maximum " + str(jeu.allumettes[t-1]) + " allumette(s) ! Choisissez un nombre entre 1 et "+str(jeu.allumettes[t-1])+": "))
                        n=int(n)
                jeu.enlever(n,t)  #Quand tout est bon, on peut enfin retirer le nombre d'allumettes n dans le tas t
            else:
                jeu.enlever(n,t)    #S'il n'y avait pas de problème, on peut directement retirer le nombre d'allumettes n dans le tas t
            jeu.tour=jeu.tour+1     #change le tour 
            
            if jeu.termine()==True: #si le jeu est terminé, on annonce donc le vainqueur
                if jeu.tour%2==0:
                    return "Le gagnant est "+str(jeu.joueurs[0])
                else:
                    return "Le gagnant est "+str(jeu.joueurs[1])
            else:
                continue

        else:   #Ici, c'est quand c'est au tour de l'ordinateur de jouer
            print(jeu)  #met les données de la partie en cours
            t=randint(1,6)  #L'ordinateur choisit une valeur aléatoire comprise entre 1 et 6 pour le tas puis 1 et 6 pour les allumettes
            n=randint(1,6)  

            if jeu.verifie(n,t)==False:     #Tant que le nombre d'allumettes choisit dans un tas est vide ou est supérieur au nombre d'allumettes initial dans le tas, on va demander à l'ordinateur de choisir un autre nombre d'allumettes n 
                if jeu.allumettes[t-1]==0:
                    while jeu.allumettes[t-1]==0:
                        t=randint(1,6)
                    n=randint(1,6)
                if n>jeu.allumettes[t-1]:
                    while n>jeu.allumettes[t-1]: 
                        n=randint(1,6)
                jeu.enlever(n,t) #Quand tout est bon, on retire le nombre d'allumettes n dans le tas t aléatoirement
            else:
                jeu.enlever(n,t) #Si le nombre d'allumettes n dans le tas t choisi était bon, on les retire directement 
            jeu.tour=jeu.tour-1 #change le tour
            
            if jeu.termine()==True: #Si le jeu est terminé, on annonce le vainqueur sinon on continue
                if jeu.tour%2==0:
                    return "Le gagnant est "+str(jeu.joueurs[0])
                else:
                    return "Le gagnant est "+str(jeu.joueurs[1])
            else:
                continue
    
    
