while True:
    try:
        nomFicher = input("fournir le nom de fichier a ouvrir: ")
        with open(nomFicher, 'r') as fichier:
            data = fichier.read()
            print(data)
        break
    except FileNotFoundError:
        print("fichier nexiste pas")
    except PermissionError:
        print("vous navez pas la permission pour ouvrir ce fichier")
    except Exception as e:
        print(f"Erreur {e}")
