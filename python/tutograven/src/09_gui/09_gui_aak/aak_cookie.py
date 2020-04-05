from tkinter import *

counter=0


#Fonctions

def reset_counter():
    counter=0
    label_counter.config(text=counter)

def add_counter():
    global counter
    counter += 1
    label_counter.config(text=counter)



#Creation de la fenetre

window = Tk()
window.title("Cookie App")
window.geometry("720x360")
window.minsize(720, 360)
window.maxsize(1200, 600)
window.config(background="#dec1aa")

#Créer la frame principale

frame = Frame(window, bg="#dec1aa")

#Création d'image

width = 300
height = 300
image = PhotoImage(file="cookie.png").zoom(10).subsample(32)

#Créer une sous boite

right_frame = Frame(frame, bg="#dec1aa")

#Création Title

label_title = Label(frame, text="Cliquer sur l'image", font=("Courrier", 25), bg="#dec1aa", fg="white")
label_title.pack()

#Création Label

label_counter = Label(frame, text="0", font=("Courrier", 40), bg="#dec1aa", fg="white")
label_counter.pack()

#Creation Boutton

button = Button(frame, image=image, bg='#dec1aa', bd=2, relief=SUNKEN, command=add_counter)
button.pack()

#Creation une barre de menu

menu_bar=Menu(window)

#Créer un premier menu
file_menu=Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Reset", command=reset_counter)
file_menu.add_command(label="Clique", command=add_counter)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)


window.config(menu=menu_bar)

#Afficher la frame

frame.pack(expand=YES)

#Afficher la fenetre
window.mainloop()