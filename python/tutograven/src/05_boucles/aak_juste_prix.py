#TP : juste prix
#choisir un nombre entre 1 et 1000
#tant que le jeu n'est pas fini
# Demander à l'utilisateur d'entrer un prix
# s'il trouve le juste prix "c'est gagné !"
# sinon on affiche c'est moins ou c'est plus
# <=>

jackpot=500
prix=int(input("Entrer un prix entre 1 et 1000 : "))


if prix==jackpot:
    print("c'est gagné !")
else:
    while prix != jackpot:
        if prix < jackpot:
            prix = int(input("saisissez un prix plus grand ! "))
        else:
            if prix > jackpot:
                prix = int(input("saisissez un prix plus petit ! "))
    print("c'est gagné !")





