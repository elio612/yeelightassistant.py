from yeelight import Bulb
from math import *
print("Modification de luminosité 'Yeelight'")
bulb = Bulb("192.168.0.34")
lum=input("Entrez une valeur (0->100) :")
if lum==():
    print("Aucune valeur définie, retour à 100%")
    lum=100
bulb.set_brightness(lum)
print("Terminé, sans erreur.")
