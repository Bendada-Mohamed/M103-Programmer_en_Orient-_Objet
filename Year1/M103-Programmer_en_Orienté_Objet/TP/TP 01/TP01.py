print("salut bendada")
print("mohamed")
(print(24))

#programme qui, à partir de la saisie d'un nombre, vérifie si paire ou impaire.

nom = int(input("entrer un nombre"))
while nom == 0:
    nom = int(input("le nombre saisie est incorect saisir un autre"))
if nom % 2 == 0:
        print(nom, "est paires")
else:
        print(nom, "est inpaires")

#programme qui affiche le tableau de multiplication d’un chiffre.

chif = int(input("entrer un chiffre"))
for i in range(1,10):
    total = i * chif
    print(chif,"*",i,"=",total)

#Écrivez un programme qui résoudre l’équation ax+b = 0

a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))

# Vérifier les conditions pour résoudre l'équation
if a == 0:
    if b == 0:
        print("L'équation a une infinité de solutions.")
    else:
        print("L'équation n'a pas de solution.")
else:
    x = -b / a
    print("La solution de l'équation est : x =", x)


    #programme qui résoudre l’équation ax²+bx+c = 0

a = int(input("entrer la valeur de a"))
b = int(input("entrer la valeur de b"))
c = int(input("entrer la valeur de c"))

D = (b ** 2) - (4 * a * c)

if D >= 0 :
    X1 = (- b + D ** (1 / 2)) / 2*a
    X2 = (- b - D ** (1 / 2)) / 2*a
    print("X1 = ",X1,"X2 = ",X2)
elif D == 0 :
    X = - b / 2 * a
    print(X)
else :
    print("L'équation n'a pas de solution réelle")

  #programme qui affiche les 10 premiers chiffres

for i in range(0,11):
    print(i)

    #programme qui affiche les 10 premières multiplications de 10.

for i in range(0,11):
    multi = 10 * i
    print(10,"*",i,"=",multi)

    # programme qui affiche un compte à rebours de 10.

for i in range(10,0, -1):
    print(i)

#entiers de 0 à 15 non compris, de trois en trois, en utilisant une boucle for et l’instruction range().


for i in range(1,15,3):
    print(i,i+1,i+2)

#  Utilisez l’instruction break pour interrompre une boucle for d’affichage des entiers de 1 à 10 compris, lorsque la variable de boucle vaut 5
n = 0
while n != 5:
    n = n + 1
    print(n)

# Utilisez l’instruction continue pour modifier une boucle for d’affichage de tous entiers de 1 à 10 compris, sauf lorsque la variable de boucle vaut 5

