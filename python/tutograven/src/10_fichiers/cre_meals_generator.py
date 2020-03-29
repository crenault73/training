# Generateur de repas

from tkinter import *
import random


class MyMealGeneratorApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Meal Generator")
        self.window.geometry("720x360")
        self.window.minsize(720, 432)
        self.window.maxsize(1200, 720)
        self.window.iconbitmap("images/meal.ico")
        self.window.config(background="#c8e0d1")

        self.meal_suggestion = ""

        # Initialization des composants
        self.frame = Frame(self.window, bg='#c8e0d1')

        # Création des composants
        self.create_elements()

        # Empaquetage
        self.frame.pack(expand=YES)

    def create_button_meal(self):
        # creation d'image
        width = 300
        height = 300
        self.image = PhotoImage(file="images/meals.png").zoom(32).subsample(64)
        # ajout du bouton/image
        button = Button(self.frame, image=self.image, bg='#c8e0d1', bd=2, relief=SUNKEN,
                        command=self.add_meal_suggestion)
        button.pack()

    def create_title(self):
        self.label_title = Label(self.frame, text="Clique pour générer une suggestion", font=("Courrier", 30),
                                 bg='#c8e0d1',
                                 fg='white')
        self.label_title.pack()

    def create_label_meal_suggestion(self):
        self.label_meal_suggestion = Label(self.frame, text="   ", font=("Courrier", 40), bg='#c8e0d1',
                                           fg='white')
        self.label_meal_suggestion.pack()

    def create_elements(self):
        self.create_title()
        self.create_button_meal()
        self.create_label_meal_suggestion()

    def get_suggestion(self):
        with open("meals.txt", "r", encoding="utf-8") as file:
            meals_list = file.readlines()
            meal_random_choice = random.choice(meals_list)
            file.close()
        return meal_random_choice

    def add_meal_suggestion(self):
        self.meal_suggestion = self.get_suggestion()
        self.label_meal_suggestion.config(text=self.meal_suggestion)


# Afficher
app = MyMealGeneratorApp()
app.window.mainloop()
