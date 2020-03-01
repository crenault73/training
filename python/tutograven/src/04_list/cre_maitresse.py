from statistics import mean
from random import shuffle

# Exemple: Jouer à la maitresse

notes = [8, 12, 10,
         9, 4, 20,
         14, 3, ]
print("Les notes: {}".format(notes))
shuffle(notes)
print("Les notes re-mélangées: {}".format(notes))

# Utilisation du module statistics
result = mean(notes)
print("Moyenne des notes: {}".format(result))
