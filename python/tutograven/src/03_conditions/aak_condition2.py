wallet = 600
computer_price=1000

#<>

if computer_price <= wallet:
    print("l'achat est possible ! ")
    wallet= wallet - computer_price
    print("il vous reste " + str(wallet))
else:
    print("l'achat n'est pas possible, vous n'avez que {}".format(wallet))
