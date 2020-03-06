

text=input("Entrer une chaine de la forme (email-pseudo-motdepasse) : ").split("-")
print(text)
print("Salut {} , ton email est : {}, ton mot de passe est : {}".format(text[1], text[0], text[2]))