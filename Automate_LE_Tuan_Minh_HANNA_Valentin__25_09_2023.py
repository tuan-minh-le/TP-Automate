class Automate :
    def __init__(self):                     #Initialisation du classe Automate
        self.initial_state = 0              #Definition de l'etat d'entree
        self.accepted_state = 9             #Definition de l'etat de sortie acceptee
        self.refused_state = 8              #Definition de l'etat de sortie refusee

    def state_transition(self, word, dictionnary, etat) :
        if word in dictionnary :                                                        #Pour chaque mot qui existe dans le dictionnaire, on parcourt le tableau de transition de l'automate en fonction de notre etat. 
            self.initial_state = etat[self.initial_state][dictionnary[word]]            #Puis, on prend en indice la valeur du mot dans le dictionnaire donne pour definir notre nouvel etat            
        else :
            self.initial_state = 8                                                      #Si le mot n'existe pas, l'etat prend la valeur associee a une phrase incorrecte

    def accepted(self):
        return self.initial_state == self.accepted_state                                #La classe Automate retourne l'un des deux etats de sortie 
    
    def refused(self):
        return self.initial_state == self.refused_state

def verification(sentence, dictionnary,etat) :               #Prend en parametres la phrase et le dictionnaire donne ; Retourne True si c'est une phrase correcte
    automate = Automate()
    if sentence[-1] == '.' :                            #On separe le point a la fin du phrase avec "espace-point" permettant a Python de separer la phrase en mots / ponctuations sous forme de liste
        sentence = sentence[0:-1] + " ."
    split = sentence.split()
    for word in split :
        automate.state_transition(word,dictionnary,etat)     #On parcourt la liste des mots separes sous forme de listes puis on applique la classe Automate sur chacun des mots
    
    return automate.accepted()                        


