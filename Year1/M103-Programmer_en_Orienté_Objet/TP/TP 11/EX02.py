import tkinter as tk

# Fonction pour incrémenter le compteur
def incrementer():
    global compteur
    compteur += 1
    label_compteur.config(text=f"Compteur : {compteur}")

# Fonction pour décrémenter le compteur (sans aller sous 0)
def decrementer():
    global compteur
    if compteur > 0:
        compteur -= 1
        label_compteur.config(text=f"Compteur : {compteur}")

# Initialisation de la fenêtre Tkinter
root = tk.Tk()
root.title("Compteur Tkinter")

# Initialisation du compteur
compteur = 0

# Création des widgets
label_compteur = tk.Label(root, text=f"Compteur : {compteur}")
button_incrementer = tk.Button(root, text="+1", command=incrementer, font=("Arial", 12), bg="green", fg="white")
button_decrementer = tk.Button(root, text="-1", command=decrementer, font=("Arial", 12), bg="red", fg="white")

# Placement des widgets
label_compteur.pack(pady=20)
button_incrementer.pack(pady=10)
button_decrementer.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()
