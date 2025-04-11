class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    def afficher_informations(self):
        print(f"nom : {self.__nom} "
              f"age : {self.__age}")

    def get_nom(self):
        return self.__nom
    def get_age(self):
        return self.__age
    def set_nom(self, nom):
        self.__nom = nom
    def set_age(self, age):
        self.__age = age


class Employe(Personne):
    def __init__(self, nom, age, poste, salaire):
        super().__init__(nom, age)
        self.__poste = poste
        self.__salaire = salaire

    def afficher_informations(self):
        super().afficher_informations()
        print(f"poste : {self.__poste} "
              f"salaire : {self.__salaire}")

    def get_poste(self):
        return self.__poste
    def get_salaire(self):
        return self.__salaire
    def set_salaire(self, salaire):
        self.__salaire = salaire
    def set_poste(self, poste):
        self.__poste = poste

per = Personne("bendada", 25)
emp = Employe("benmina", 18, "frontend", 20000)

per.get_age()
per.get_nom()
per.set_age(17)
per.set_nom("marouan")

emp.get_poste()
emp.get_salaire()

emp.set_poste("backend")
emp.set_salaire(6000)

emp.afficher_informations()