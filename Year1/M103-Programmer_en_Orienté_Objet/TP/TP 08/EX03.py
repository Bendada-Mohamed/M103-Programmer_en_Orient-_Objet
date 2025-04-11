while True:
    try:
        nombre1 = float(input("Saisir nombre 1: "))
        print("Opérations disponibles : +  -  *  /")
        operateur = input('Saisir un operateur: ').strip()
        if operateur not in ['+', '-', '*', '/']:
            raise ValueError("Opération invalide. Veuillez choisir parmi +, -, *, /.")
        nombre2 = float(input("Saisir nombre 2: "))
        match operateur:
            case "+":
                operation = nombre1 + nombre2
                break
            case "-":
                operation = nombre1 - nombre2
                break
            case "x":
                operation = nombre1 * nombre2
            case "/":
                operation = nombre1 / nombre2
        print(f"resultats {operation}")
        break

    except ZeroDivisionError:
        print("Erreur : Division par zéro impossible. Veuillez réessayer.\n")
    except ValueError as ve:
        print(f"Erreur : {ve}\n")
    except Exception as e:
        print(f"Erreur : {e}")