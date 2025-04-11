languages = ["Python", "Java", "C++", "Kotlin"]
while True:
    try:
        indice = int(input("saisir un nombre de 0 a 3: "))
        print(languages[indice])
        break
    except IndexError:
        print("indice en dehors de la plage de la liste")
    except ValueError:
        print("erreur saisir un entier")