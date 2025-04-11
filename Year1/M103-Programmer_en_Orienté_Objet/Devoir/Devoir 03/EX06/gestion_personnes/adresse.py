class Adresse:
    def __init__(self, rue, ville, code_postal):
        self.rue = rue
        self.ville = ville
        self.code_postale = code_postal

    def afficher_adresse(self):
        return (f"Rue: {self.rue}, "
                f"Ville: {self.ville}, "
                f"Code Postale: {self.code_postale}.")
