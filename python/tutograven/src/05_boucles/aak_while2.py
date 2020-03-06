# un youtubeur a 2500 abonnés

subscribers_cont=2500

#il gagne 10% d'audience supplémentaire par mois
months=1

#on souhaite estimer combien aura t-il d'abonnés après deux ans

while months <= 24:
    subscribers_cont=subscribers_cont+((subscribers_cont*10)/100)
    print("Le youtubeur a {} au mois {}".format(subscribers_cont,months))
    months += 1
