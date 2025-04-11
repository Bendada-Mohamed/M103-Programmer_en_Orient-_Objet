import tkinter as tk
from tkinter import messagebox


def calculer(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "+":
            resultat.set(num1 + num2)
        elif operation == "-":
            resultat.set(num1 - num2)
        elif operation == "*":
            resultat.set(num1 * num2)
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Erreur", "Division par zéro impossible")
                return
            resultat.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice Simple")
root.geometry("400x300")

# Variables
resultat = tk.StringVar()

# Widgets
label_num1 = tk.Label(root, text="Nombre 1 :", font=("Arial", 12))
entry_num1 = tk.Entry(root, font=("Arial", 12))

label_num2 = tk.Label(root, text="Nombre 2 :", font=("Arial", 12))
entry_num2 = tk.Entry(root, font=("Arial", 12))

label_resultat = tk.Label(root, text="Résultat :", font=("Arial", 12))
entry_resultat = tk.Entry(root, textvariable=resultat, font=("Arial", 12), state="readonly")

# Boutons pour les opérations
btn_add = tk.Button(root, text="+", command=lambda: calculer("+"), font=("Arial", 12), width=5, bg="lightblue")
btn_sub = tk.Button(root, text="-", command=lambda: calculer("-"), font=("Arial", 12), width=5, bg="lightblue")
btn_mul = tk.Button(root, text="×", command=lambda: calculer("*"), font=("Arial", 12), width=5, bg="lightblue")
btn_div = tk.Button(root, text="÷", command=lambda: calculer("/"), font=("Arial", 12), width=5, bg="lightblue")

# Placement des widgets
label_num1.pack(pady=5)
entry_num1.pack(pady=5)

label_num2.pack(pady=5)
entry_num2.pack(pady=5)

label_resultat.pack(pady=5)
entry_resultat.pack(pady=5)

# Placement des boutons en grille
btn_add.pack(side=tk.LEFT, padx=10, pady=10)
btn_sub.pack(side=tk.LEFT, padx=10, pady=10)
btn_mul.pack(side=tk.LEFT, padx=10, pady=10)
btn_div.pack(side=tk.LEFT, padx=10, pady=10)

# Lancement de l'application
root.mainloop()
