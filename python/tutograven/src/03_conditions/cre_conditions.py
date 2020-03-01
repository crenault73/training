# code
wallet = 5000
computer_price = 1000

# On vérifie que le prix de l'ordinateur est inférieur à 1000
print("Le prix de l'ordinateur est inférieur à 1000€: " + str(computer_price < 1000))

if computer_price < 1000:
    print("Le prix de l'ordinateur est inférieur à 1000€")
else:
    print("Non, le prix est supérieur ou égal à 1000€")

if computer_price != 1000:
    print("Le prix de l'ordinateur est différent de 1000€")
else:
    print("Oui, le prix est de 1000€")
