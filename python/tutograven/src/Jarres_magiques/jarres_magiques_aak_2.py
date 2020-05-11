import random

print("Bienvenue dans le jeu !")

# choix du paramétrage

level = int(input("Ecrivez 1:Facile, 2:Moyen, 3:Difficile : "))

# compteur clés magiques
keys = 0

while keys != 3:
    print("Vous disposez de 5 jarres, chosissez 1, 2, 3, 4 ou 5")

    # tableau qui contient chacune des jarres
    jars = ['k', 'k', 'k', 'k', 'k']
    print(jars)


    # une boucle qui va tourner autant de fois qu'il doit y avoir de serpent
    for i in range(0, level):
        print("1 serpent a été ajouté dans une jarre")
        jars[i] = 'S'

    # melanger les jarres
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