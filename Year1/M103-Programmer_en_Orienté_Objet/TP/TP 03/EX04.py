class Paiment:
    def __init__(self, montant, date):
        self.montant = montant
        self.date = date

class CarteDeCredit(Paiment):
    def __init__(self, montant, date, numero_de_carte):
        super().__init__(montant, date)
        self.numero_de_carte = numero_de_carte
    def effectuer_paiment(self):
        print(f"Paiement de {self.montant} DH par carte {self.numero_de_carte} le {self.date}.")


class PayPal(Paiment):
    def __init__(self, montant, date, adresse_email):
        super().__init__(montant, date)
        self.adresse_email = adresse_email
    def connexion_paypal(self):
        print(f"Connexion à PayPal avec {self.adresse_email}... Paiement de {self.montant} DH le {self.date}.")

class VirementBancaire(Paiment):
    def __init__(self, montant, date, compte_bancaire):
        super().__init__(montant, date)
        self.compte_bancaire = compte_bancaire
    def initier_virement(self):
        print(f"Virement de {self.montant} DH depuis le compte {self.compte_bancaire} le {self.date}.")

class Client:
    def __init__(self, nom, adrese, moyen_de_paiment):
        self.nom = nom
        self.adrese = adrese
        self.moyen_de_paiment = moyen_de_paiment

    def effectuer_paiment(self):
        if isinstance(self.moyen_de_paiment, CarteDeCredit):
            self.moyen_de_paiment.effectuer_paiment()
        elif isinstance(self.moyen_de_paiment, PayPal):
            self.moyen_de_paiment.connexion_paypal()
        elif isinstance(self.moyen_de_paiment, VirementBancaire):
            self.moyen_de_paiment.initier_virement()
        else:
            print("fuck you bro!")
# Création des moyens de paiement
paiement_cb = CarteDeCredit(500, "2025-04-01", "1234-5678-9012-3456")
paiement_paypal = PayPal(250, "2025-04-02", "client@example.com")
paiement_virement = VirementBancaire(1000, "2025-04-03", "MA123456789")

# Création des clients
client1 = Client("Yasmine", "Casablanca", paiement_cb)
client2 = Client("Omar", "Fès", paiement_paypal)
client3 = Client("Sara", "Marrakech", paiement_virement)

# Simulation des paiements
print("--- Paiements en cours ---")
client1.effectuer_paiment()
client2.effectuer_paiment()
client3.effectuer_paiment()


