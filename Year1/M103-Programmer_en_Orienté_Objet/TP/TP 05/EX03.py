from abc import ABC, abstractmethod
class CompteBancaire(ABC):
    valeur_arbitraire = 0.01
    def __init__(self, solde):
        self._solde = solde

    def get_solde(self):
        return self._solde

    def add_solde(self, solde):
        self._solde += solde

    @abstractmethod
    def calculer_interets(self):
        pass

class CompteEpargne(CompteBancaire):
    def calculer_interets(self):
        return self.get_solde() * CompteEpargne.valeur_arbitraire

class CompteCourant(CompteBancaire):
    def calculer_interets(self):
        return "les comptes courants nont pas dinterets!"


compteEpargne = CompteEpargne(0)
compteCourant = CompteCourant(0)

compteCourant.add_solde(5000)
compteEpargne.add_solde(5000)

print(compteEpargne.calculer_interets())
print(compteCourant.calculer_interets())