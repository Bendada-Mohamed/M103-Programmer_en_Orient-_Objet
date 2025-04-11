import tkinter as tk

def convertir():
    try:
        celsius = float(entry_celsius.get())  # Récupérer la valeur entrée
        fahrenheit = (celsius * 9/5) + 32  # Conversion
        label_resultat.config(text=f"Température en Fahrenheit : {fahrenheit:.2f}°F")
    except ValueError:
        label_resultat.config(text="Veuillez entrer un nombre valide.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Convertisseur de Température")

# Création des widgets
label_instruction = tk.Label(root, text="Entrez la température en Celsius :")
entry_celsius = tk.Entry(root)
button_convertir = tk.Button(root, text="Convertir", command=convertir)
label_resultat = tk.Label(root, text="")

# Placement des widgets dans la fenêtre
label_instruction.pack(pady=10)
entry_celsius.pack(pady=5)
button_convertir.pack(pady=10)
label_resultat.pack(pady=10)

# Lancer la boucle principale
root.mainloop()
