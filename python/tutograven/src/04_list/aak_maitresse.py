from random import shuffle
from statistics import mean

#exemple

notes = [8, 12, 10,
         9,4, 20]

print(notes)
result = mean(notes)
print("La moyenne de l'élève est {}".format(result))
shuffle(notes)
print(notes)
