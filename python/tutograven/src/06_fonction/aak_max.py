#Crée une fonction max :
# <=>

def max(a, b):
    if a > b:
        return a
    else:
        return b

first_value=int(input("Entrer la premiere valeur : "))
seconde_value=int(input("Entrer la deuxieme valeur : "))
max_value=max(first_value,seconde_value)
print("la valeur max est : {}".format(max_value))

