# Exemple: Liste à partir de split
# Récuppération d'une liste à partir d'une chaine de la forme: email-pseudo-motdepasse
text = input("Entrer une chaine de la forme: email-pseudo-motdepasse ").split("-")
print(text)
print("Salut {}, ton e-mail est {}".format(text[1],text[0]))
