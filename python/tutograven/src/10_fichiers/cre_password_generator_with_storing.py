import string
from random import randint, choice
from tkinter import *


# Ajout d'un système de stockage des mots de passe


def store_password(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
        file.close()


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    store_password(password)


# Créer la fenêtre
window = Tk()

# Personnaliser cette fenêtre
window.title("Generator de mot de passe")
window.geometry("720x360")
window.minsize(720, 360)
window.maxsize(1200, 600)
window.iconbitmap("images/logo.ico")
window.config(background="#4065A4")

# Créer la Frame principale
frame = Frame(window, bg="#4065A4")

# Creation d'image
width = 300
height = 300
image = PhotoImage(file="images/privacy.png")
canvas = Canvas(frame, width=width, height=height, bg="#4065A4", bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=E)

# Créer une sous-boite
right_frame = Frame(frame, bg="#4065A4")

# Créer un titre
label_title = Label(right_frame, text="Mot de passe", font=("Helveticat, 20"), bg="#4065A4", fg="white")
label_title.pack()

# Créer un champ/entrée/input
password_entry = Entry(right_frame, font=("Helveticat, 20"), bg="#4065A4", fg="white")
password_entry.pack()

# Créer un button
generate_button = Button(right_frame, text="Générer", font=("Helveticat, 20"), bg="#4065A4", fg="white",
                         command=generate_password)
generate_button.pack(fill=X)

# On place la sous-boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

# Afficher la frame
frame.pack(expand=YES)

# Création d'une barre de menu
menu_bar = Menu(window)
# Créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Configure cette fenêtre pour ajouter la barre de menu
window.config(menu=menu_bar)

# Afficher la fenêtre
window.mainloop()
