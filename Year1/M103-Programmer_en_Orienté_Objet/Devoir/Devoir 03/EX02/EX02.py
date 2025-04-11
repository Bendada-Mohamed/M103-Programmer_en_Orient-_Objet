import re


def valider_numero_carte_nationale(numero):
    format = r"^[A-Z]{2}\d{5}$"
    return re.match(format, numero)

numero = input("Saisir un numéro de carte qui conforme à cette format: (AB00000): ")

if valider_numero_carte_nationale(numero):
    print("numero de carte national est valide!")
else:
    print("invalid numero de carte national!")