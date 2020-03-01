
age = int(input ("Quel age avez vous ? "))
pop = input("Voulez vous du popcorn ? ")
prix_mineur= 7
prix_majeur=12

if age < 18:
    if pop == "oui":
        prix_mineur += 5
        print("Vous devez payer " + str(prix_mineur) +"  euros")
    else:
        print("Vous devez payer " + str(prix_mineur) +" euros")
else:
    if pop == "oui":
        prix_majeur += 5
        print("Vous devez payer " + str(prix_majeur) + " euros ")
    else:
        print("Vous devez payer " + str(prix_majeur) + " euros ")

