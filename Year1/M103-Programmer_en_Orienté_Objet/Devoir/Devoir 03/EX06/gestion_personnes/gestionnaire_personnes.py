from personne import Personne
from adresse import Adresse


per = Personne("Bendada", "Mohamed", 24)
adr = Adresse("56 Lot el amal hay al inbiat", "Temara", 12000)

print(per.afficher_infos())
print(adr.afficher_adresse())
