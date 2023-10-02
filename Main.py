# Créé par Elève, le 27/09/2023 en Python 3.7
from Warriors import *

#Création des guerriers
guerrier1 = Warrior("Conan", 78)

#Création des armes
weapon1 = Weapon("Excalibur", 7)
weapon2 = Weapon("Durandal", 4)
weapon3 = Weapon("MasterSword", 10)

guerrier1.addWeapon(weapon1)
guerrier1.addWeapon(weapon2)
guerrier1.addWeapon(weapon3)


guerrier1.setSelectedWeapon("Durandal")

guerrier1.losePV(10)
print(guerrier1)
"""
 Le guerrier, quand il est victime d’une attaque, voit son niveau de vie baisser d’un certain
nombre de points (passés en argument).
 Le personnage doit pouvoir attaquer un autre personnage. Les dégâts subis par le personnage
correspondent au niveau d’attaque de l’arme en main. Toutefois, si le guerrier « Lannister »,
attaque avec l’épée « Durandal », les dégâts sont doublés. Idem si « Conan » attaque avec « Excalibur ».

Test :

Créer 2 guerriers et une épée qui sera affectée au second.
Faire en sorte que le premier soit victime d'une attaque de la part du second et afficher leurs
caractéristiques. Vérifier les dégâts subis dans toutes les configurations possibles.
"""
