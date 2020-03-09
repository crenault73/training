

def get_voyelles1(chaine):
    list_voyelles=['a','o','e','u','i','y', 'é', 'è', 'à']
    cpt=0
    i=0
    for lettre in chaine:
        if lettre in list_voyelles:
            cpt+=1
    print("le mot {} contient {} voyelles".format(chaine, cpt))

def get_voyelles2(chaine):
    list_voyelles=['a','o','e','u','i','y', 'é', 'è', 'à']
    cpt=0

    for i in range(0, len(chaine)):
        if chaine[i] in list_voyelles:
            cpt+=1
    print("le mot {} contient {} voyelles".format(chaine, cpt))






mot=input("Entrer un mot : ")
print(mot)
get_voyelles1(mot)
get_voyelles2(mot)


