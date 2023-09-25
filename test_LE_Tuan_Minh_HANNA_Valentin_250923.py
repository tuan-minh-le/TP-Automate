from Automate_LE_Tuan_Minh_HANNA_Valentin_250923 import Automate
from Automate_LE_Tuan_Minh_HANNA_Valentin_250923 import verification
from Automate_LE_Tuan_Minh_HANNA_Valentin_250923 import inputsent

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

dictionnary = {"le": 0,"la": 0,"chat":2,"souris": 2,"martin":4, "mange":3,"la":0,"petite":1,"joli":1,"grosse":1,"blanc":1, "bleu":1,"verte":1,"dort":3,"julie":4,"jean":4,".":5}
sentence1 = "le joli chat mange."
sentence2 = "la grosse souris verte mange le joli petite chat blanc." 
sentence3 = "le joli chat joue"
sentence4 = "le joli chat joue." 
sentence5 = inputsent()

test1 = print(verification(sentence1, dictionnary,etat))         #True
test2 = print(verification(sentence2, dictionnary,etat))         #True
test3 = print(verification(sentence3, dictionnary,etat))         #False
test4 = print(verification(sentence4, dictionnary,etat))         #False
test5 = print(verification(sentence5, dictionnary, etat))
