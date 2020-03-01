import string

# Place de cinema
prix = 0

# Récolter de la personne
age = int(input("Quel est votre âge?"))
# Si la personne est mineur -> 7€
if age < 18:
    prix += 7
# Si la personne est majeur -> 12€
else:
    prix += 12

# Souhaitez-vous du popcorn ?
answer = (input("Souhaitez-vous du popcorn ?")).lower()
popcorn = True if answer == "yes" or answer == "y" else False
print("popcorn?: " + str(popcorn))
# si oui -> 5€
if popcorn:
    prix += 5

# Afficher le prix total à payer:
print("Le prix à payer: {}€".format(prix))
