# Creer une fonction max() qui va renvoyer le résultat le plus parmi 2 valeurs
def max(a, b):
    if a > b:
        return a
    else:
        return b


first_value = input("Entrer la valeur de a: ")
second_value = input("Entrer la valeur de b: ")
max_value = max(first_value, second_value)
print("Maximum de (" + str(first_value) + "," + str(second_value) + ") est :", max_value)
