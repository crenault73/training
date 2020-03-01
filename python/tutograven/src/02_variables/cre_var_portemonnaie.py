def main():
    # Recolter une valeur porte monnaie
    porte_monnaie = int(input("Entre la valeur du porte monnaie:"))
    # Créer un produit qui aura pour valeur 50
    produit = 50
    # Afficher la nouvelle valeur du porte monnaie, après son achat
    porte_monnaie = porte_monnaie + produit
    print("Nouvelle valeur du porte monnaie: " + str(porte_monnaie))


if __name__ == '__main__':
    main()
