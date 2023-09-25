etat = {0 : [1,8,8,8,4,8],                  #Tableau de transition de l'automate ; Les etats sont representes de 0 a 9  
        1 : [8,1,2,8,8,8],                  #0 : Attente d'article
        2 : [8,2,2,3,8,8],                  #1 : Article reconnu 
        3 : [5,8,8,8,7,9],                  #2 : Nom reconnu
        4 : [8,8,8,3,8,8],                  #3 : Verbe reconnu
        5 : [8,5,6,8,8,8],                  #4 : Nom propre reconnu
        6 : [8,6,8,8,8,9],                  #5 : Plusieurs verbes reconnus
        7 : [8,8,8,8,8,9],                  #6 : Plusieurs noms reconnus  
        8 : [8,8,8,8,8,8],                  #7 : Plusieurs noms propres reconnus
        9 : [9,9,9,9,9,9]}                  #8 : Phrases incorrectes / #9 Phrases correctes (Etats de sortie) 
                                            

class Automate :
    def __init__(self):                     #Initialisation du classe Automate
        self.initial_state = 0              #Definition de l'etat d'entree
        self.accepted_state = 9             #Definition de l'etat de sortie acceptee
        self.refused_state = 8              #Definition de l'etat de sortie refusee

    def state_transition(self, word, dictionnary) :
        if word in dictionnary :                                                        #Pour chaque mot qui existe dans le dictionnaire, on parcourt le tableau de transition de l'automate en fonction de notre etat. 
            self.initial_state = etat[self.initial_state][dictionnary[word]]            #Puis, on prend en indice la valeur du mot dans le dictionnaire donne pour definir notre nouveau etat            
        else :
            self.initial_state = 8                                                      #Si le mot n'existe pas, l'etat prend la valeur associee a une phrase incorrecte

    def accepted(self):
        return self.initial_state == self.accepted_state                                #La classe Automate retourne l'un des deux etats de sortie 
    
    def refused(self):
        return self.initial_state == self.refused_state

def verification(sentence, dictionnary) :               #Prend en parametres la phrase et le dictionnaire donnee ; Retourne True si c'est une phrase correcte, False sinon
    automate = Automate()
    if sentence[-1] == '.' :                            #On separe le point a la fin du phrase avec "espace-point" permettant a Python de separer la phrase en mots / ponctuations sous forme de liste
        sentence = sentence[0:-1] + " ."
        print (sentence)
    split = sentence.split()
    for word in split :
        automate.state_transition(word,dictionnary)     #On parcourt la liste des mots separes sous forme de listes puis on applique la classe Automate sur chacun des mots
    
    if automate.accepted() :                           
        return True
    
    else : 
        return False
    


