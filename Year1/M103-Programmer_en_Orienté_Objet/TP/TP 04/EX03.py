class Employe:
    def __init__(self, nom, age, salaire):
        self.__nom = nom
        self.__age = age
        self.__salaire = salaire

    def get_nom(self):
        return self.__nom
    def get_age(self):
        return self.__age
    def get_salaire(self):
        return self.__salaire

    def set_nom(self, nom):
        self.__nom = nom
    def set_age(self, age):
        self.__age = age
    def set_salaire(self, salaire):
        self.__salaire = salaire


class Manager(Employe):
    def __init__(self, nom, age, salaire, departement):
        super().__init__(nom, age, salaire)
        self.__departement = departement
        self.__subordonnes = []

    def get_departement(self):
        return self.__departement
    def get_subordonnes(self):
        return self.__subordonnes
    def set_departement(self, departement):
        self.__departement = departement
    def set_subordonnes(self, subordonnes):
        self.__subordonnes = subordonnes

    def ajouter_subordonnes(self, employe):
        self.__subordonnes.append(employe)

emp = Employe("MOHAMED", 25, 10000)
emp1 = Employe("MAROUAN", 25, 10000)
emp2 = Employe("kHADIJA", 25, 10000)


mang = Manager("Hicham", 19, 20000, "Devops")

mang.ajouter_subordonnes(emp)
mang.ajouter_subordonnes(emp1)
mang.ajouter_subordonnes(emp2)

for emp in mang.get_subordonnes():
    print(emp.get_nom())



