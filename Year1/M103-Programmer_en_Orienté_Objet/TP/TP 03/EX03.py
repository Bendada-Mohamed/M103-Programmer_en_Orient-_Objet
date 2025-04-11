class Personnage:
    def __init__(self, nom, niveau, points_de_vie, points_attaque):
        self.nom = nom
        self.niveau = niveau
        self.point_de_vie = points_de_vie
        self.points_attaque = points_attaque
        self.inventaire = Inventaire()

class Guerrier(Personnage):
    def __init__(self, nom, niveau, points_de_vie,points_attaque, force):
        super().__init__(nom, niveau, points_de_vie, points_attaque)
        self.force = force
    def frappe_lourde(self):
        pass

class Mage(Personnage):
    def __init__(self, nom, niveau, points_de_vie, points_attaque, magie):
        super().__init__(nom, niveau, points_de_vie, points_attaque)
        self.magie = magie
    def lancer_sort(self):
        pass

class Archer(Personnage):
    def __init__(self, nom, niveau, points_de_vie, points_attaque, agilite):
        super().__init__(nom, niveau, points_de_vie, points_attaque)
        self.agilite = agilite

    def tir_precision(self):
        pass


class Arme:
    def __init__(self, nom, degats):
        self.nom = nom
        self.degats = degats
    def afficher(self):
        print(f"Arme: {self.nom}, Dégâts: {self.degats}")


class Inventaire:
    def __init__(self):
        self.inventaire = []

    def ajouter_arme(self, arme):
        self.inventaire.append(arme)
        print(f"larme {arme.nom} est ajouter avec succe!")

    def afficher_inventaire(self):
        for arme in self.inventaire:
            print(arme.afficher())

# Création des armes
epee = Arme("Epée du Dragon", 50)
baguette = Arme("Baguette Enchantée", 40)
arc = Arme("Arc Elfique", 35)

# Création de personnages
guerrier1 = Guerrier("Thorin", 5, 120, 30, 80)
mage1 = Mage("Gandalf", 7, 100, 25, 90)
archer1 = Archer("Legolas", 6, 110, 28, 85)

guerrier1.inventaire.ajouter_arme(epee)
guerrier1.inventaire.ajouter_arme(baguette)
guerrier1.inventaire.ajouter_arme(arc)

guerrier1.inventaire.afficher_inventaire()
