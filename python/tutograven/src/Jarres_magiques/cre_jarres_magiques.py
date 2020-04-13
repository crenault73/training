import random

print("Bienvenue dans le jeu !")
# Choix du paramétrage/niveau de difficulté
level = int(input("Ecrit 1: facile, 2: Moyen, 3: Difficile"))
print("Vous disposez de 5 jarres devant vous. Choisissez 1, 2, 3, 4 ou 5")

# compteur clés magiques
trousseaux = 0

while trousseaux != 3:

    # Tableau qui va contenir chacune des jars
    jars = ["K"] * (5 - level)
    snakes = ["S"] * level
    jars.extend(snakes)

    # Melange mes jarres
    random.shuffle(jars)
    print(jars)
    # le choix aléatoire de la jarre qui fait perdre notre joueur
    snake_jar = random.randint(1, 5)  # nombre au hasard entre 1 et 5

    # demander a notre joueur de mettre une valeur
    choix = int(input("Choisissez un numéro de jarre : "))

    # vérification

    if jars[choix - 1] == "K":  # Gagné !
        print("Gagné ! Vous obtenez une clé magique ! la jarre infectée était la numéro ", snake_jar)
        trousseaux += 1
        print("Vous avez actuellement : ", trousseaux, "/3 clés")
    else:
        print("Perdu ! un serpent apparait !")

        # si le joueur n'a pas de clé
        if trousseaux > 0:
            trousseaux -= 1
            print(f"Vous avez actuellement : {trousseaux}/3 clés")

print("Tu deviens le roi du temps ! ")
