import os
import random

if os.path.exists("meals.txt"):
    with open("meals.txt", 'r+') as file:
        meals_list=file.readlines()
        meal_random_choice= random.choice(meals_list)
        print("Je vous propose aujourd'hui le repas : ", meal_random_choice)
        file.close()
else:
    print("Le document n'existe pas. Attention !!")