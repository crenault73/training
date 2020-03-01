# tp: Jeu du Juste prix
# Choisir un nombre en 1 et 1000
# tant que le jeu n'est pas fini
# -> Demander à l'utilisateur de rentrer un prix
# -> si il trouve le juste prix "C'est gagné!!!"
# -> sinon on afficher "C'est moins!" ou "C'est plus!"

prix = 223
proposition = -1

while proposition != prix:
    proposition = int(input("Quel est le prix? "))
    if proposition > prix:
        print("C'est moins!")
    elif proposition < prix:
        print("C'est plus!")
    else:
        print("C'est gagné!!!")
