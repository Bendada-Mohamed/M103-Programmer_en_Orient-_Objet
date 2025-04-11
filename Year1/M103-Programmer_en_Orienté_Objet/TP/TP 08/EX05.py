while True:
    try:
        valeurNumerique = float(input("saisir une valeur en metre : "))
        convertion = valeurNumerique * 1000
    except ValueError:
        print("Erreur : Saisir un nombre")
    except Exception as e:
        print(f"Erreur: {e}")