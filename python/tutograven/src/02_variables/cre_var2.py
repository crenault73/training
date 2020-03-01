def main():
    # Recolter une premiere note
    note1 = int(input("Entrer la première note:"))
    # Recolter la deuxieme note
    note2 = int(input("Entrer la deuxième note:"))
    # Recolter la troisieme note
    note3 = int(input("Entrer la troisième note:"))
    # Calculer la moyenne
    result = (note1 + note2 + note3) / 3
    # Affiche le résultat
    print("La moyenne est: " + str(result))


if __name__ == '__main__':
    main()
