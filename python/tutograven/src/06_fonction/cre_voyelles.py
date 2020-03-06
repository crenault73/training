# Tp: une fonction pour calculer le nombre de voyelles dans un mot
# definir une fonction get_vowels_numbers(mot)
# créer un compteur de voyelles
# pour chaque lettre du mot vous vérifier s'il s'agit d'une voyelle
# à la fin de la fonction, vous allez renvoyer le compteur

vowels = ["a", "à", "ä", "â", "e", "é", "è", "ë", "ê", "i", "ï", "î", "o", "ö", "ô", "u", "ù", "ü", "û", "y"]


def get_vowels_numbers(mot):
    num = 0
    for i in range(0, len(mot)):
        if mot[i] in vowels:
            num += 1
    return num


mot = input("Entrer un mot: ")
nb = get_vowels_numbers(mot)
print("Le mot " + mot + " contient " + str(nb) + " voyelles.")
