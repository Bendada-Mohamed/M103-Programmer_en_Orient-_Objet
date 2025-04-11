from abc import ABC, abstractmethod


class Media(ABC):
    @abstractmethod
    def get_info(self):
        pass
    @abstractmethod
    def calculer_frais_location(self, duree: int):
        pass

class Livre(Media):
    def __init__(self, titre, auteur, prix_par_jour):
        self.titre = titre
        self.auteur = auteur
        self.prix_par_jour = prix_par_jour

    def get_info(self):
        return (f"Titre : {self.titre},"
                f"Auteur : {self.auteur},"
                f"Prix par jour : {self.prix_par_jour} Dhs")

    def calculer_frais_location(self, duree: int):
        return self.prix_par_jour * duree


class Magazine(Media):
    def __init__(self, titre, auteur, prix_par_jour):
        self.titre = titre
        self.auteur = auteur
        self.prix_par_jour = prix_par_jour

    def get_info(self):
        return (f"Titre : {self.titre},"
                f"Auteur : {self.auteur},"
                f"Prix par jour : {self.prix_par_jour} Dhs")

    def calculer_frais_location(self, duree: int):
        return self.prix_par_jour * duree

class Dvd(Media):
    def __init__(self, titre, auteur, prix_par_jour):
        self.titre = titre
        self.auteur = auteur
        self.prix_par_jour = prix_par_jour

    def get_info(self):
        return (f"Titre : {self.titre},"
                f"Auteur : {self.auteur},"
                f"Prix par jour : {self.prix_par_jour} Dhs")

    def calculer_frais_location(self, duree):
        return self.prix_par_jour * duree

class Bibliotheque:
    def __init__(self):
        self.bibliotheque = []

    def ajouter_media(self, media):
        self.bibliotheque.append(media)

    def afficher_mediatheque(self):
        if not self.bibliotheque:
            print("la biblio est vide")
        else:
            for media in self.bibliotheque:
                print(media.get_info())

    def calculer_frais_location_total(self, duree: int):
        duree_total = 0
        for media in self.bibliotheque:
            duree_total += media.calculer_frais_location(duree)
        print(f"frais de location total pour {duree} jours : {duree_total:.2f} Dhs")
        return  duree_total

biblio = Bibliotheque()
livre1 = Livre("1984", "George Orwell", 2.0)
magazine1 = Magazine("Science & Vie", "Collectif", 1.5)
dvd1 = Dvd("Inception", "Christopher Nolan", 3.0)

biblio.ajouter_media(livre1)
biblio.ajouter_media(magazine1)
biblio.ajouter_media(dvd1)

print("\nListe des médias :")
biblio.afficher_mediatheque()

print("\nCalcul des frais de location pour 5 jours :")
biblio.calculer_frais_location_total(5)




