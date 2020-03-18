# TP Cookie clicker
# 1 Créer une fenêtre avec un cookie au centre
# 2 Créer un compteur
# 3 Une boutique

from tkinter import *


class MyCookieApp:
    global cookie_count

    def __init__(self):
        self.window = Tk()
        self.window.title("My Cookie App")
        self.window.geometry("720x480")
        self.window.minsize(720, 480)
        self.window.maxsize(1200, 800)
        self.window.iconbitmap("cookie.ico")
        self.window.config(background="#dec1aa")

        self.cookie_count = 0

        # Initialization des composants
        self.frame = Frame(self.window, bg='#dec1aa')

        # Création des composants
        self.create_elements()

        # Empaquetage
        self.frame.pack(expand=YES)

    def create_button_cookie(self):
        # creation d'image
        width = 300
        height = 300
        self.image = PhotoImage(file="cookie.png").zoom(32).subsample(64)
        # ajout du bouton/image
        button = Button(self.frame, image=self.image, bg='#dec1aa', bd=2, relief=SUNKEN,
                        command=self.add_cookie)
        button.pack()

    def create_title(self):
        self.label_title = Label(self.frame, text="Clique sur le cookie", font=("Courrier", 40), bg='#dec1aa',
                                 fg='white')
        self.label_title.pack()

    def create_label_counter(self):
        self.label_counter = Label(self.frame, text="0", font=("Courrier", 40), bg='#dec1aa',
                                   fg='white')
        self.label_counter.pack()

    def reset_counter(self):
        self.cookie_count = 0
        self.label_counter.config(text=self.cookie_count)

    def create_menu(self):
        # Création d'une barre de menu
        menu_bar = Menu(self.window)
        # Créer un premier menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Reset", command=self.reset_counter)
        file_menu.add_command(label="Quitter", command=self.window.quit)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)

        # Configure cette fenêtre pour ajouter la barre de menu
        self.window.config(menu=menu_bar)

    def create_elements(self):
        self.create_title()
        self.create_button_cookie()
        self.create_label_counter()
        self.create_menu()

    def add_cookie(self):
        self.cookie_count += 1
        self.label_counter.config(text=self.cookie_count)


# afficher
app = MyCookieApp()
app.window.mainloop()
