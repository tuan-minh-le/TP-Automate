from Automate_LE_Tuan_Minh_HANNA_Valentin_250923 import Automate
from Automate_LE_Tuan_Minh_HANNA_Valentin_250923 import verification
from Automate_LE_Tuan_Minh_HANNA_Valentin_250923 import inputsent

def main(dictionnary,etat) :
    sentence = inputsent()
    return verification(sentence, dictionnary, etat)
