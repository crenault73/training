import random

print("Bienvenue dans le jeu !")

# compteur clés magiques
keys = 0

while keys != 3:
    print("Vous disposez de 5 jarres, chosissez 1, 2, 3, 4 ou 5")

    # le choix aléatoire de la jarre qui fait perdre notre joueur
    snake_jar = random.randint(1, 5)  # nombre au hasard entre 1 et 5

    # demander a notre joueur de mettre une valeur
    choix = int(input("choisissez un numéro de jarre : "))

    # vérification

    if choix != snake_jar:
        print("Gagné ! Vous obtenez une clé magique ! la jarre infectée etait la numéro ", snake_jar)
        keys += 1
        print("Vous avez actuellement : ", keys, "/3 clés")
    else:
        print("Perdu ! un serpent apparait !")

        #si le joueur n'a pas de clé
        if keys > 0:
            keys -= 1
            print("Vous avez actuellement : ", keys, "/3 clés")

print("Tu deviens le roi du temps ! ")