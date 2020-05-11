import random
"""
level = 2
serpent = ['S'] * level
print(serpent)
"""

level = int(input('Quel niveau de difficulté pour le jeu ? 1, 2 ou 3 ? : '))
snake = ['S'] * level
difference = 5 - level
cle = ['K'] * difference
jars = snake + cle
random.shuffle(jars)
print(jars)

