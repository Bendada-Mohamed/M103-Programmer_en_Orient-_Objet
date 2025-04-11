import tkinter as tk
from tkinter import messagebox

def ajouter_tache():
    tache = entry_tache.get().strip()
    if tache:  # Vérifier si l'entrée n'est pas vide
        liste_taches.insert(tk.END, tache)
        entry_tache.delete(0, tk.END)  # Effacer la zone de saisie
    else:
        messagebox.showwarning("Attention", "Veuillez entrer une tâche valide.")

def marquer_terminee(event):
    try:
        index = liste_taches.curselection()[0]  # Récupérer l'index sélectionné
        tache = liste_taches.get(index)

        # Vérifier si la tâche est déjà barrée
        if tache.startswith("✓ "):
            liste_taches.delete(index)
            liste_taches.insert(index, tache[2:])  # Enlever la coche
        else:
            liste_taches.delete(index)
            liste_taches.insert(index, "✓ " + tache)  # Ajouter une coche
    except IndexError:
        pass  # Si aucun élément n'est sélectionné, ne rien faire

def supprimer_tache():
    try:
        index = liste_taches.curselection()[0]  # Récupérer l'index sélectionné
        liste_taches.delete(index)  # Supprimer la tâche
    except IndexError:
        messagebox.showwarning("Attention", "Veuillez sélectionner une tâche à supprimer.")

# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("Gestionnaire de Tâches")
root.geometry("400x400")

# Widgets
label_instruction = tk.Label(root, text="Nouvelle tâche :", font=("Arial", 12))
entry_tache = tk.Entry(root, font=("Arial", 12))
button_ajouter = tk.Button(root, text="Ajouter", command=ajouter_tache, font=("Arial", 12), bg="green", fg="white")
liste_taches = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
button_supprimer = tk.Button(root, text="Supprimer", command=supprimer_tache, font=("Arial", 12), bg="red", fg="white")

# Placement des widgets
label_instruction.pack(pady=10)
entry_tache.pack(pady=5)
button_ajouter.pack(pady=5)
liste_taches.pack(pady=10, fill=tk.BOTH, expand=True)
button_supprimer.pack(pady=5)

# Lier un clic sur une tâche à la fonction "marquer_terminee"
liste_taches.bind("<Double-Button-1>", marquer_terminee)

# Lancement de l'application
root.mainloop()
