from abc import ABC, abstractmethod
import math
class FormeGeometrique(ABC):
    @abstractmethod
    def calculer_superficie(self):
        pass
    def calculer_perimetre(self):
        pass


class Cercle(FormeGeometrique):
    def __init__(self, r):
        self.r = r
    def calculer_superficie(self):
        return math.pi * (self.r ** 2)
    def calculer_perimetre(self):
        return math.pi * self.r * 2


class Carre(FormeGeometrique):
    def __init__(self, cote):
        self.cote = cote
    def calculer_perimetre(self):
        return self.cote * 4
    def calculer_superficie(self):
        return self.cote ** 2

carre = Carre(4)
cercle = Cercle(5)

print("=== Cercle ===")
print("Rayon :", cercle.r)
print("Superficie :", round(cercle.calculer_superficie(), 2))
print("Périmètre :", round(cercle.calculer_perimetre(), 2))

print("\n=== Carré ===")
print("Côté :", carre.cote)
print("Superficie :", carre.calculer_superficie())
print("Périmètre :", carre.calculer_perimetre())



