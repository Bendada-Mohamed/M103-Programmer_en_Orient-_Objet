while True:
    try:
        nombre1 = float(input("saisir nombre 1: "))
        nombre2 = float(input("saisir nombre 2: "))
        division = nombre1 / nombre2
    except ValueError:
        print("Erreur : Veuillez entrer uniquement des valeurs numériques.\n)")
    except ZeroDivisionError:
        print("Erreur : Division par zéro impossible. Veuillez réessayer.\n")
    else:
        print(f"division de {nombre1} sur {nombre2} est : {division}")
        break