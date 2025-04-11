class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    def afficher_infos(self):
        print(f"Nom : {self.nom},"
              f"Prenom : {self.prenom},"
              f"Salaire: {self.salaire}")

