# Lecture de fichier
import os
import random

filename = "meals.txt"

# On vérifie l'existence du fichier
if os.path.exists(filename):
    with open(filename, "r",encoding="utf-8") as file:
        meals_list = file.readlines()
        meal_random_choice = random.choice(meals_list)
        print("Je vous propose aujourd'hui le repas", meal_random_choice)
        file.close()
else:
    print("Le document", filename, "n'existe pas")
