from employe import Employe
from entreprise.gestionnaire import Gestionnaire
# Création des employés
emp1 = Employe("Bennani", "Omar", 8000)
emp2 = Employe("El Amrani", "Amina", 9500)

# Création des gestionnaires
gest1 = Gestionnaire("Bouras", "Karim", 12000, "Informatique")
gest2 = Gestionnaire("Zahraoui", "Sofia", 13500, "Ressources Humaines")

# Affichage des informations
emp1.afficher_infos()
print()
emp2.afficher_infos()
print()
gest1.afficher_infos()
print()
gest2.afficher_infos()
