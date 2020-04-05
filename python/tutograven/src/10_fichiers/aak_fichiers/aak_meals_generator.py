# Generateur de repas

from tkinter import *
import random
import os


class MealGeneratorApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("Meal Generator")
        self.window.geometry("720x360")
        self.window.minsize(720, 400)
        self.window.maxsize(1200, 720)
        self.window.config(background="#c8e0d1")
        self.meal = " "
        # Initialization des composants
        self.frame = Frame(self.window, bg='#c8e0d1')

        # Création des composants
        self.create_elements()

        # Empaquetage
        self.frame.pack(expand=YES)

    def create_button(self):

        self.image = PhotoImage(file="image/meals.png").zoom(32).subsample(64)
        self.button = Button(self.frame, image = self.image, font=("Courrier", 30),
                                 bg='#c8e0d1',
                                 fg='white',
                                 command= self.add_suggestion)
        self.button.pack()

    def create_title(self):
        self.title = Label(self.frame, text = "Cliquer pour avoir une suggestion de repas", font=("Courrier", 20),
                                 bg='#c8e0d1',
                                 fg='white' )
        self.title.pack()

    def create_label_Suggestion(self):

        self.label = Label(self.frame, text="  ", font=("Courrier", 30),
                                 bg='#c8e0d1',
                                 fg='white')
        self.label.pack()

    def create_elements(self):
        self.create_title()
        self.create_button()
        self.create_label_Suggestion()


    def get_suggtesion(self):
        if os.path.exists("meals.txt"):
            with open("meals.txt", "r", encoding="utf-8") as file:
                liste_meal=file.readlines()
                random_choice_meal=random.choice(liste_meal)
                file.close()
            return random_choice_meal
        else:
            print("Le fichier n'existe pas")

    def add_suggestion(self):
        self.meal = self.get_suggtesion()
        self.label.config(text=self.meal)


#Afficher
App = MealGeneratorApp()
App.window.mainloop()

