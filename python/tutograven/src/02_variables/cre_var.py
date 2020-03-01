def main():
    #Création d'une variable 'username' ayant pour valeur 'crenault'
    username = "Christophe"
    #Création d'une variable 'age' ayant pour valeur 46
    age = 19
    #Affiche le username et age
    print(username, age)
    #Change la valeur de l'age
    age = 45
    #Affiche la nouvelle valeur de l'age
    print(age)
    age = age + 1
    print(age)

    print ("Salut "+username+", vous avez "+str(age))


if __name__ == '__main__':
    main()