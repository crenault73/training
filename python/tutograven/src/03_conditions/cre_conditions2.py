# code
wallet = 5000
computer_price = 900

# Le prix de l'ordinateur est inférieur à 1000€
if computer_price <= wallet:
    print("L'achat est possible")
    wallet -= computer_price
else:
    print("L'achat n'est pas possible, vous n'avez que {}€".format(wallet))

print(computer_price)
#Pas bon !!! text = ("L'achat est possible","L'achat est impossible")[computer_price <= 1000]
text = "L'ordinateur a un prix raisonnable" if computer_price < 1000 else "L'ordinateur est cher"

print("Valeur du porte monnaie: {}€".format(wallet))
