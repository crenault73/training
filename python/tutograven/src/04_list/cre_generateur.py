# Générateur de phrases
# Demander en console une chaine de la forme "mot1/mot2/mot3/mot4/..."
# Transformer cette chaine en une liste
# La mélanger
# et si le nombre d'élements de cette liste est inférieure à 10
# -> Afficher les deux premiers mots
# si le nombre de mots est supérieur ou égal à 10
# -> Afficher les 3 derniers mots
# ex: corneille/mésange/verdier/rouge-gorge/merle/fauvette/moineau/pigeon/pie/geai/pic/colombe

import random

mots = input('Entrer une chaîne de caractère de la forme "mot1/mot2/mot3/mot4/...":\n').split("/")
print("La liste de mots: {}".format(mots))
random.shuffle(mots)
print("La liste de mots mélangée: {}".format(mots))

if len(mots) < 10:
    print("On affiche les 2 premiers mots: {}, {}".format(mots[0], mots[1]))
else:
    mots.reverse()
    print("On affiche les 3 derniers mots: {}, {}, {}".format(mots[2], mots[1], mots[0]))
