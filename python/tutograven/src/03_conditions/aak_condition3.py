# systeme de vérification de mot de passe
password = input("Entrer votre mot de passe : ")
password_length = len(password)

#vérifier si le mot de passe est inferieur à 8 carrecteres <>

if password_length <=8:
    print("Le mot de passe est trop court")
elif 8 < password_length <=12:
    print("mot de passe moyen !")
else:
    print("mot de passe parfait !!")