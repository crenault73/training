# exemple: système de vérification de mot de passe
password = input("Entrez votre mot de passe:")
password_len = len(password)

# Vérifier si le mot de passe à au moins 8 caractères:
if password_len <= 8:
    print("Mot de passe trop court!")
elif password_len > 8 and password_len <= 12:
    print("Mot de passe moyen.")
else:
    print("Mot de passe parfait!")

print("Le mot de passe: " + password)
