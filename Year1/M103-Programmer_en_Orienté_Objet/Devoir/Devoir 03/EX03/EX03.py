import math
from abc import ABC, abstractmethod


# Exception
class FormeNotFound(Exception):
    pass


# Interface
class Imprimante(ABC):
    @abstractmethod
    def imprimer_forme(self):
        pass


# Class de Base Forme
class Forme(ABC):
    def __init__(self, couleur, nom):
        self.couleur = couleur
        self.nom = nom


    def afficher_details(self):
        return (f"Nom: {self.nom}, "
                f"Couleur: {self.couleur}")


    @abstractmethod
    def calculer_petimetre(self):
        pass

    @abstractmethod
    def calculer_surface(self):
        pass


    # Enregister details
    def enregistrer_details(self):
        with open("forme.txt", 'a', encoding="utf-8") as file:
            file.write(f"{self.__class__.__name__} ({self.nom}, {self.couleur}): Périmètre = {self.calculer_petimetre()}"
                       f", Surface = {self.calculer_surface()}\n")


# Sous-class Cylindre
class Cylindre(Forme, Imprimante):
    def __init__(self,couleur, nom, rayon, hauteur):
        super().__init__(couleur, nom)
        self.__rayon = rayon
        self.__hauteur = hauteur


    # Getters
    def get_rayon(self):
        return self.__rayon

    def get_hauteur(self):
        return self.__hauteur
    # Setters
    def set_rayon(self, rayon):
        self.__rayon = rayon
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    # Afficher details
    def afficher_details(self):
        return (f"{super().afficher_details()}, "
                f"Rayon: {self.__rayon}, "
                f"Hauteur: {self.__hauteur}.")

    # Calculer Périmètre
    def calculer_petimetre(self):
        return round((2 * math.pi * self.__rayon), 2)


    # Calculer Surface
    def calculer_surface(self):
        return round((2 * math.pi * self.__rayon * (self.__rayon + self.__hauteur)), 2)


    # Imprimer
    def imprimer_forme(self):
        print(f"Impression de {self.nom}...")


# Sous-class Sphere
class Sphere(Forme, Imprimante):
    def __init__(self, couleur, nom, rayon1):
        super().__init__(couleur, nom)
        self.__rayon1 = rayon1


    # Getters
    def get_rayon1(self):
        return self.__rayon1


    # Setters
    def set_rayon1(self, rayon1):
        self.__rayon1 = rayon1


    # Afficher details
    def afficher_details(self):
        return (f"{super().afficher_details()}, "
                f"Rayon1: {self.__rayon1}.")


    # Calculer Perimetre
    def calculer_petimetre(self):
        perimetre = 2 * math.pi * self.__rayon1
        return round(perimetre, 2)


    # Calculer Surface
    def calculer_surface(self):
        surface = 4 * math.pi * (self.__rayon1 ** 2)
        return round(surface, 2)


    # Imprimer
    def imprimer_forme(self):
        print(f"Impression de {self.nom}...")


# Sous-class Cube
class Cube(Forme, Imprimante):
    def __init__(self, couleur, nom, cote):
        super().__init__(couleur, nom)
        self.__cote = cote


    # Getters
    def get_cote(self):
        return self.__cote


    # Setters
    def set_cote(self, cote):
        self.__cote = cote


    # Afficher details
    def afficher_details(self):
        return (f"{super().afficher_details()}, "
                f"Côté: {self.__cote}.")


    # Calculer Perimetre
    def calculer_petimetre(self):
        perimetre = self.__cote * 12
        return round(perimetre)


    # Calculer Surface
    def calculer_surface(self):
        return  round((6 * (self.__cote ** 2)), 2)

    # Imprimer
    def imprimer_forme(self):
        print(f"Impression de {self.nom}...")


# sous-class Disque
class Disque(Forme, Imprimante):
    def __init__(self, couleur, nom, rayon2):
        super().__init__(couleur, nom)
        self.__rayon2 = rayon2


    # Getters
    def get_rayon2(self):
        return self.__rayon2


    # Setters
    def set_rayon1(self, rayon2):
        self.__rayon2 = rayon2


    # Afficher details
    def afficher_details(self):
        return (f"{super().afficher_details()}, "
                f"Rayon2: {self.__rayon2}.")


    # Calculer surface
    def calculer_surface(self):
        return round((2 * math.pi * self.__rayon2), 2)


    # Calculer permetre
    def calculer_petimetre(self):
        return round((math.pi * (self.__rayon2 ** 2)), 2)



    # Imprimer
    def imprimer_forme(self):
        print(f"Impression de {self.nom}...")


# Création des objets
cylindre = Cylindre("Rouge", "Cylindre1", 5, 10)
sphere = Sphere("Bleu", "Sphere1", 7)
cube = Cube("Vert", "Cube1", 4)
disque = Disque("Jaune", "Disque1", 6)

# Polymorphisme
objects = [cylindre, sphere, cube, disque]
for objt in objects:
    print(objt.afficher_details())
    objt.enregistrer_details()
    objt.imprimer_forme()