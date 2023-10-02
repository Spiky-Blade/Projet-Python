class Weapon:
    __nom = ""
    __attack = 0

    def __init__(self, nom, attack):
        self.__nom = nom
        self.__attack = attack

    def getNom(self):
        return self.__nom

    def getAttack(self):
        return self.__attack

    def __str__(self):
        return self.__nom + " " + str(self.__attack)