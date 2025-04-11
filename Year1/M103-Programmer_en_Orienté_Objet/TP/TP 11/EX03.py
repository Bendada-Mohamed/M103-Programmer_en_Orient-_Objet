import tkinter as tk

def calculer_carre():
    try:
        nombre = float(entry_nombre.get())  # Récupérer la valeur entrée
        carre = nombre ** 2  # Calcul du carré
        label_resultat.config(text=f"Résultat : {carre:.2f}")  # Afficher le résultat
    except ValueError:
        label_resultat.config(text="Veuillez entrer un nombre valide.")  # Message d'erreur

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calcul du Carré")
root.geometry("300x200")

# Création des widgets
label_instruction = tk.Label(root, text="Entrez un nombre :", font=("Arial", 12))
entry_nombre = tk.Entry(root, font=("Arial", 12))
button_calculer = tk.Button(root, text="Calculer", command=calculer_carre, font=("Arial", 12))
label_resultat = tk.Label(root, text="", font=("Arial", 14), fg="blue")

# Placement des widgets
label_instruction.pack(pady=10)
entry_nombre.pack(pady=5)
button_calculer.pack(pady=10)
label_resultat.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()
