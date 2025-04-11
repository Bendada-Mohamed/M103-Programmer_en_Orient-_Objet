class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def afficher_infos(self):
        return (f"Nom: {self.nom}, "
                f"Prenom: {self.prenom}, "
                f"Age: {self.age}. ")