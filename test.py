from Automate_LE_Tuan_Minh_25_09_2023 import Automate
from Automate_LE_Tuan_Minh_25_09_2023 import verification

dictionnary = {"le": 0,"la": 0,"chat":2,"souris": 2,"martin":4, "mange":3,"la":0,"petite":1,"joli":1,"grosse":1,"blanc":1, "bleu":1,"verte":1,"dort":3,"julie":4,"jean":4,".":5}
sentence1 = "le joli chat mange."
sentence2 = "la grosse souris verte mange le joli petite chat blanc." 
sentence3 = "le joli chat joue"
sentence4 = "le joli chat joue." 

test1 = print(verification(sentence1, dictionnary))         #True
test2 = print(verification(sentence2, dictionnary))         #True
test3 = print(verification(sentence3, dictionnary))         #False
test4 = print(verification(sentence4, dictionnary))         #False