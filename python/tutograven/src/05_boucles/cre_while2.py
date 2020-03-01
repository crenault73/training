# Un youtubeur Gravinou, 2500 abonnés
subscriber_count = 2500

# Il gagne 10% d'audience supplémentaire par mois
month = 0

# On souhaite estimer combien il aura d'abonnés après 2 ans (24 mois)
while month < 24:
    # Augmenter l'audience
    subscriber_count *= 1.1
    # Afficher le nombre d'abonnés
    print("Vous avez {:d} abonnés.".format(int(subscriber_count)))
    # On passe au mois suuivant
    month += 1
