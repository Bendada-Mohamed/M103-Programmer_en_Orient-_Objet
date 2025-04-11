class Personne:
    def __init__(self, nom, age, adresse):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_adresse(self):
        return self.__adresse

    def set_nom(self, nom):
        self.__nom = nom

    def set_age(self, age):
        self.__age = age

    def set_adresse(self, adresse):
        self.__adresse = adresse

class Etudiant(Personne):
    def __init__(self, nom, age, adresse, matricule, classe):
        super().__init__(nom, age, adresse)
        self.__matricule = matricule
        self.__classe = classe

    def get_matricule(self):
        return self.__matricule
    def set_matricule(self, matricule):
        self.__matricule = matricule

    def get_clase(self):
        return self.__classe

    def set_classe(self, classe):
        self.__classe = classe

etu = Etudiant("bendada", 25, "temara", 12, "dev104")

print(f"Nom :{etu.get_nom()},"
      f"Age :{etu.get_age()},"
      f"Adresse :{etu.get_adresse()},"
      f"Matricule :{etu.get_matricule()},"
      f"Classe : {etu.get_clase()}")
etu.set_adresse("rabat")
print(f"Nom :{etu.get_nom()},"
      f"Age :{etu.get_age()},"
      f"Adresse :{etu.get_adresse()},"
      f"Matricule :{etu.get_matricule()},"
      f"Classe : {etu.get_clase()}")


