from ..employe import Employe
class Gestionnaire(Employe):
    def __init__(self, nom, prenom, salaire, departement):
        super().__init__(nom, prenom, salaire)
        self.departement = departement

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Departement : {self.departement}")
