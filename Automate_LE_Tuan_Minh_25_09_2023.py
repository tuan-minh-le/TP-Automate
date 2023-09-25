etat = {0 : [1,8,8,8,4,8],
        1 : [8,1,2,8,8,8],
        2 : [8,8,2,3,8,8],
        3 : [5,8,8,8,7,9],
        4 : [8,8,8,3,8,8],
        5 : [8,5,6,8,8,8],
        6 : [8,6,8,8,8,9],
        7 : [8,8,8,8,8,9]}


class Automate :
    def __init__(self):
        self.initial_state = 0
        self.final_state = 9

    def state_transition(self, word) :
        self.initial_state = etat[self.initial_state][dict["word"]]

    def accepted(self):
        return self.initial_state in self.final_state

def verification(sentence, automate) :
    for word in sentence :
        automate.state_transition(word)
    
    if automate.accepted():
        return True
    
    else : 
        return False
    


