class Weapon:
    __name = ""
    __attack = 0

    def __init__(self, name, attack):
        self.__name = name
        self.__attack = attack

    def getName(self):
        return self.__name

    def getAttack(self):
        return self.__attack

    def __str__(self):
        return self.__nom + " " + str(self.__attack)