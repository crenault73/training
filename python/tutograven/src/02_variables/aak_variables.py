def main():
    username = 'Amira'
    age = 29
    print("l\'age d\'" + username + " aujourd'hui est "+ str(age) +" ans")
    age = age +1
    print("l\'age d\'" + username + " le 19 septembre prochain sera "+ str(age) +" ans")

    note1 = int(input("Entrez la première note : "))
    note2 = int(input("Entrez la deuxième note : "))
    note3 = int(input("Entrez la troisième note : "))
    moyenne = (note1+note2+note3)/3
    print("la moyenne est : "+ str(moyenne))
if __name__ == '__main__':
    main()
