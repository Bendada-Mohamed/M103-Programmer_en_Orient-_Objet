salles = ["Salle1", "Salle2", "Salle3", "Salle4"]
labos = ["Labo1", "Labo2", "Labo3"]

def afficher():
    print("Listes des salles: ", salles)


def ajouter(salle, indice=None):
    if indice is None:
        salles.append(salle)
        afficher()
    else:
        salles.insert(indice, salle)
        afficher()


def supprimer(indice=None):
    if indice is None:
        salles.pop()
        afficher()
    else:
        if 0 <= indice <= len(salles):
            del salles[indice]
            afficher()
        else:
            print("indice Invalide!")


def modifier(indice, nouvelle_salle):
    if 0 <= indice <= len(salles):
        salles[indice] = nouvelle_salle
        afficher()
    else:
        print("indice Invalide!")

# def modifier2(salle, nouvelle_salle):
#     if salle in salles:
#         salles[salles.index(salle)] = nouvelle_salle
#     else:
#         return salle," n'existe pas."

def chercher(salle):
    if salle in salles:
        return salles.index(salle)
    else:
        print(salle," n'existe pas.")


def calculer():
    return len(salles)


def etendre():
    salles.extend(labos)
    afficher()

def dictionnaire():
    # diction = {}
    # for i in range(len(salles)):
    #     diction[i+1] = salles[i]
    # print("Dictionnaire des salles :", diction)
    diction = {i + 1: salle for i, salle in enumerate(salles)}
    print("Dictionnaire des salles :", diction)


ajouter("Salle5")

ajouter("Salle6", 2)

supprimer()

supprimer(1)

modifier(1, "Salle Multimedia")

print("Salle multimedia se trouve a l'indice: ", chercher("Salle Multimedia"))

print("Nombre total de salles:", calculer())

etendre()
dictionnaire()
