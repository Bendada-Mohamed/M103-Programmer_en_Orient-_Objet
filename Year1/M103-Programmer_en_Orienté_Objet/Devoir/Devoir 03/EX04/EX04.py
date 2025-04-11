import tkinter as tk
from tkinter import messagebox
import os


# Fichier de sauvegarde des contacts
NOMFICHIER = "data.txt"


# Sauvegarder les contacts dans data.txt
def sauvgarder_list():
    with open(NOMFICHIER, "w") as fichier:
        for nom, phone in contact_list:
            fichier.write(f"{nom}|{phone}\n")



# Chargement des contacts existants
def charger_contact():
    contacts = []
    if os.path.exists(NOMFICHIER):
        with open(NOMFICHIER, 'r') as fichier:
            for line in fichier:
                nom, phone = line.strip().split("|")
                contacts.append((nom, phone))
    return contacts


# Ajouter un contact
def ajouter_contact():
    nom = entry_name.get().strip()
    phone = entry_phone.get().strip()
    if nom and phone:
        contact_list.append((nom, phone))
        miseajour_listbox()
        sauvgarder_list()
    else:
        messagebox.showwarning("Attention", "Veuillez entrer un nom et un numéro de téléphone.")


# Afficher les détails d'un contact sélectionné
def afficher_contact():
    selected = listbox.curselection()
    if selected:
        indice = selected[0]
        nom, phone = contact_list[indice]
        messagebox.showwarning("Details du contact",f"Nom: {nom}\nTéléphone: {phone}")
    else:
        messagebox.showwarning("Attention", "Veuillez sélectionner un contact à afficher.")


# Modifier un contact sélectionné
def modifier_contact():
    selected = listbox.curselection()
    if selected:
        indice = selected[0]
        nom = entry_name.get().strip()
        phone = entry_phone.get().strip()
        if nom and phone:
            contact_list[indice] = (nom, phone)
            miseajour_listbox()
            sauvgarder_list()
        else:
            messagebox.showwarning("Attention", "Veuillez entrer un nom et un numéro de téléphone.")
    else:
        messagebox.showwarning("Attention", "Veuillez sélectionner un contact à modifier.")


# Supprimer un contact sélectionné
def supprimer_contact():
    selected = listbox.curselection()
    if selected:
        indice = selected[0]
        del contact_list[indice]
        sauvgarder_list()
        miseajour_listbox()

    else:
        messagebox.showwarning("Attention", "Veuillez sélectionner un contact à supprimer.")

# mettre a jour listbox
def miseajour_listbox():
    listbox.delete(0, tk.END)
    for nom, phone in contact_list:
        listbox.insert(tk.END, nom)



# Fenetre principale
root = tk.Tk()
root.title("Répertoire téléphonique.")
root.geometry("500x250")

contact_list = charger_contact()



# Champs de saisie
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Nom: ").grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Numéro de téléphone: ").grid(row=1, column=0)
entry_phone = tk.Entry(frame)
entry_phone.grid(row=1, column=1)

# Buttons
frame1 = tk.Frame(root)
frame1.pack(pady=10)
tk.Button(frame1, text="Ajouter", command=ajouter_contact).pack(fill=tk.BOTH, side=tk.LEFT)
tk.Button(frame1, text="Modifier", command=modifier_contact).pack(fill=tk.BOTH, side=tk.LEFT)
tk.Button(frame1, text="Supprimer", command=supprimer_contact).pack(fill=tk.BOTH, side=tk.LEFT)
tk.Button(frame1, text="Afficher details", command=afficher_contact).pack(fill=tk.BOTH, side=tk.LEFT)

# listbox
listbox = tk.Listbox(root, width=30, height=10)
listbox_label = tk.Label(root, text="Liste des Contacts")
listbox_label.pack()
listbox.pack()



miseajour_listbox()




# Lancer l'application
root.mainloop()