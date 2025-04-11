import re #beblio dial les exp reg
class Document: # classe Document avec les attributs proteges
    _objects_compteur = 0 #initializite hade lvariable
    def __init__(self, reference, titre, auteur, nombre_de_page):
        self._reference = str(reference)
        self._titre = str(titre)
        self._auteur = str(auteur)
        self._nombre_de_page = int(nombre_de_page)
        Document._objects_compteur += 1 #kola merra tcreya chi objet ghatzade wahed
# les getters
    def get_reference(self):
        return self._reference
    def get_titre(self):
        return self._titre
    def get_auteur(self):
        return self._auteur
    def get_nombre_de_page(self):
        return self._nombre_de_page
# les setters
    def set_reference(self, reference):
        self._reference = reference
    def set_titre(self, titre):
        self._titre = titre
    def set_auteur(self, auteur):
        self._auteur = auteur
    def set_nombre_de_page(self, nombre_de_page):
        self._nombre_de_page = nombre_de_page
# methode bache yetn9es l3adade ila tsuprima chi object
    def __del__(self):
        Document._objects_compteur -= 1
# mthode str li katkhelini nafficher lobjet as string
    def __str__(self):
        return f"[{self._reference}, {self._titre}, {self._auteur}, {self._nombre_de_page}]"
#method eq li kat9aren lia reference dial jouje dial les objets
    def __eq__(self, autre):
        if isinstance(autre, Document): #hadi katgolek ila kan dak "autre" instance dial class Document
            return self._reference == autre._reference
        else:
            return False
#method calculercout en fonction de nombres de pages
    def calculercout(self):
        return f"le cout du document {self._titre} est : {2.3 * self._nombre_de_page} dhs."
#method validerreference
    def validerreference(self):
        regexp = '^[A-Z]{3}[1-9]{4}$'
        if re.match(regexp, self._reference):
            return f"reference du document {self._titre} est valider."
        else:
            return f"reference du document {self._titre} n'est pas valider."
#clss Roman
class Roman(Document):
    def __init__(self, reference, titre, auteur, nombre_de_page, editeur, annee_de_publication): # initialisation de tous les attributs
        super().__init__(reference, titre, auteur, nombre_de_page) #appel du constructeur de Document
        self._editeur = editeur
        self._annee_de_publication = annee_de_publication
    def __str__(self):
        return f"{super().__str__()[:-1]}, {self._editeur}, {self._annee_de_publication}]" # dert dik [:-1] bache n7yed dik ']'
#classe Revue
class Revue(Document):
    def __init__(self, reference, titre, auteur, nombre_de_page, mois, annee):
        super().__init__(reference, titre, auteur, nombre_de_page)
        self._mois = mois
        self._annee = annee
# method valider mois annee
    def valider_mois_annee(self):
        regexp = r"^(0[1-9]|1[0-2])/20[0-9]{2}$" # or  r"^(0[1-9]|1[0-2])/\d{4}$"
        if re.match(regexp, f'{self._mois}/{self._annee}'):
            return f"est valider"
        else:
            return f"non valider"
    def __str__(self):
        return f"{super().__str__()[:-1]}, {self._mois}, {self._annee}]"
# class Beblio
class Bibliotheque:
    def __init__(self, nom, adresse):
        self._nom = nom
        self._adresse = adresse
        self.list_documents = []
    def __str__(self):
        return f"{self._nom}, {self._adresse}, {self.list_documents}"
# method ajouter document
    def ajouter_document(self, document):
        self.list_documents.append(document)
# method chercher document
    def chercher_document(self, reference):
        for document in self.list_documents:
            if document.get_reference() == reference:
                print(f"{document.get_titre()} est trouve.")
            else:
                print("Aucun document n'est trouve avec cette reference.")
# method liste Roman
    def liste_roman(self):
        for document in self.list_documents:
            if isinstance(document, Roman):
                print(document)
# method Supprimer Document
    def supprimer_document(self, reference):
        for document in self.list_documents:
            if document.get_reference() == reference:
                del document
# method enregistrer document
    def enregistrer_document(self):
        with open('fichier.txt', 'w') as fichier:
            for document in self.list_documents:
                fichier.write(f"{document}\n")
doc1 = Document(4, 'test', 'test', 5)
doc2 = Document(4, 'test', 'test', 5)
roman1 = Roman(4, 'test', 'test', 45, 'test', 2019)
roman2 = Roman(4, 'test', 'test', 45, 'test', 2019)
revue = Revue("test", "test", "test", 45, 19, 2024)
beblio1 = Bibliotheque('test', 'test')
# del  doc1 #test ila suprimite chi objet wache ghadi yetn9ess wahed
# print(f"Object nombre: {Document._objects_compteur}") #test dial compteur des objets
# print(doc1) # jerebt nprinti doc1 direct o 3tani [4, test, test, 5]
# print(doc1.__dict__)
# print(doc1 == doc2) #test __eq__ method katjaweb be true or false
# print(doc1.calculercout()) #test  calculer le cout du document
# print(doc2.validerreference()) # test methode validerreference
# print(roman1) # test  str Roman redefinit
# print(revue.valider_mois_annee()) # text valider_mois_annee
# print(revue) # test  str Roman redefinit
# test dajout et de recherche
# beblio1.ajouter_document(doc1)
# beblio1.ajouter_document(doc2)
# beblio1.chercher_document("4")
# test list roman et enregistrer
# beblio1.ajouter_document(doc1)
# beblio1.ajouter_document(doc2)
# beblio1.ajouter_document(roman1)
# beblio1.ajouter_document(roman2)
# beblio1.ajouter_document(revue)
# beblio1.liste_roman()
# beblio1.enregistrer_document()