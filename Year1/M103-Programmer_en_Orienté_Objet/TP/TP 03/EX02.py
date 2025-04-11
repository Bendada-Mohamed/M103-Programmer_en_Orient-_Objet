class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


class Livre(Produit):
    def __init__(self, nom, prix, auteur):
        super().__init__(nom, prix)
        self.auteur = auteur
    def afficher_auteur(self):
        print(f"nom: {self.nom},"
              f"prix : {self.prix},"
              f"auteur : {self.auteur}")


class Vetement(Produit):
    def __init__(self, nom, prix, taille):
        super().__init__(nom, prix)
        self.taille = taille
    def afficher_taille(self):
        print(f"nom: {self.nom},"
              f"prix : {self.prix},"
              f"auteur : {self.taille}")

class Electronique(Produit):
    def __init__(self, nom, prix, marque):
        super().__init__(nom, prix)
        self.marque = marque
    def afficher_marque(self):
        print(f"nom: {self.nom},"
              f"prix : {self.prix},"
              f"auteur : {self.marque}")


class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.panier = []

    def ajouter_au_panier(self, produit):
        self.panier.append(produit)
        print(f"le produit {produit.nom} est Ajouter avec Succe!")

    def afficher_panier(self):
        for produit in self.panier:
            if isinstance(produit, Livre):
                produit.afficher_auteur()
            elif isinstance(produit, Vetement):
                produit.afficher_taille()
            elif isinstance(produit, Electronique):
                produit.afficher_marque()
            else:
                print("sire t9awed")

livre1 = Livre("Le Petit Prince", 70, "Antoine de Saint-Exupéry")
vetement1 = Vetement("T-shirt Noir", 120, "L")
electronique1 = Electronique("Smartphone", 2500, "Samsung")

# Création d'un client
client1 = Client("Youssef", "Rabat, Maroc")

# Ajout des produits au panier
client1.ajouter_au_panier(livre1)
client1.ajouter_au_panier(vetement1)
client1.ajouter_au_panier(electronique1)

client1.afficher_panier()
