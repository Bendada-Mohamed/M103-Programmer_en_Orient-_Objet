class Vehicule:
    def __init__(self, immatriculation, capacite, vitesse_max):
        self.immatriculation = immatriculation
        self.capacite = capacite
        self.vitess_max = vitesse_max

class Camion(Vehicule):
    def __init__(self, immatriculation, capacite, vitesse_max, charge_max):
        super().__init__(immatriculation, capacite, vitesse_max)
        self.charge_max = charge_max

    def charger_marchandises(self):
        print(f"Camion {self.immatriculation} : Chargement des marchandises (max {self.charge_max} kg)...")


class Fourgon(Vehicule):
    def __init__(self, immatriculation, capacite, vitesse_max, volume_max):
        super().__init__(immatriculation, capacite, vitesse_max)
        self.volume_max = volume_max

    def charger_colis(self):
        print(f"Fourgon {self.immatriculation} : Chargement des colis (volume max {self.volume_max} m3)...")


class Moto(Vehicule):
    def __init__(self, immatriculation, capacite, vitesse_max, cylindree):
        super().__init__(immatriculation, capacite, vitesse_max)
        self.cylindree = cylindree

    def livrer_rapidement(self):
        print(f"Moto {self.immatriculation} : Livraison rapide avec cylindrée de {self.cylindree} cm3...")

class MissionTransport:
    def __init__(self, depart, arrivee, date):
        self.depart = depart
        self.arrivee = arrivee
        self.date = date
        self.vehicule = None

    def assigner_vehicule(self, vehicule):
        self.vehicule = vehicule
        print(f"Mission du {self.date} de {self.depart} à {self.arrivee} : Véhicule {vehicule.immatriculation} assigné.")

    def executer_mission(self):
        if isinstance(self.vehicule, Camion):
            self.vehicule.charger_marchandises()
        elif isinstance(self.vehicule, Fourgon):
            self.vehicule.charger_colis()
        elif isinstance(self.vehicule, Moto):
            self.vehicule.livrer_rapidement()
        else:
            print("Aucun véhicule assigné ou type inconnu.")



# Création des véhicules
camion1 = Camion("123-ABC", 10000, 90, 15000)
fourgon1 = Fourgon("456-DEF", 3000, 110, 12)
moto1 = Moto("789-GHI", 200, 130, 600)

# Création des missions
mission1 = MissionTransport("Casablanca", "Rabat", "2025-04-01")
mission2 = MissionTransport("Fès", "Meknès", "2025-04-02")
mission3 = MissionTransport("Agadir", "Essaouira", "2025-04-03")

# Assignation des véhicules
mission1.assigner_vehicule(camion1)
mission2.assigner_vehicule(fourgon1)
mission3.assigner_vehicule(moto1)


mission3.executer_mission()
