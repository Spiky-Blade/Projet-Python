from Weapon import *

class Warrior:
    __name = ""
    __PV = 0
    __selectedWeapon = None

    def __init__(self, name, PV):
        self.__nom = nom
        self.__PV = PV
        self.__weapons = []
        self.__selectedWeapon = None

    def getName(self):
        return self.__name

    def getPV(self):
        return self.__PV

    def __str__(self):
        return self.__nom + " à " + str(self.__PV) + " PV. Son arme principal est " + str(self.__armeEnMain.getNom())

    def addWeapon(self, w:Weapon):
        if len(self.__weapons) < 5:
            self.__weapons.append(w)

    def getWeapons(self):
        return self._weapons

    def getSelectedWeapon(self):
        return self.__selectedWeapon

    def setSelectedWeapon(self, weaponToSet):
        for weapon in self.__weapons:
            if weapon.getNom().lower() == weaponToSet.lower():
                self.__selectedWeapon = weapon

    def losePV(self, pvToRemove):
        self.__PV -= pvToRemove

    def attaquer(self, AttackingWarrior, AttackedWarrior):
        AttackedWarrior.losePV(AttackingWarrior.__armeEnMain.getAttack)
