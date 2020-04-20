import random

print("Bienvenue dans le jeu !")

# choix du paramétrage

# compteur clés magiques
keys = 0

while keys != 3:
    level = int(input('Quel niveau de difficulté pour le jeu ? 1, 2 ou 3 ? : '))
    snake = ['s'] * level
    difference = 5 - level
    cle = ['k'] * difference
    jars = snake + cle
    random.shuffle(jars)
    print(jars)

    # demander a notre joueur de mettre une valeur
    choix = int(input("choisissez un numéro de jarre : "))

    # vérification

    if jars[choix-1] == 'k':
        print("Gagné ! Vous obtenez une clé magique ! la jarre infectée etait la numéro ", jars)
        keys += 1
        print("Vous avez actuellement : ", keys, "/3 clés")
    else:
        print("Perdu ! un serpent apparait !")

        #si le joueur n'a pas de clé
        if keys > 0:
            keys -= 1
            print("Vous avez actuellement : ", keys, "/3 clés")

print("Tu deviens le roi du temps ! ")