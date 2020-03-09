# Simulateur de ville
# Créer 3 classes: Immeuble, Supermarché, Banque
# Superclass: Batiment
# Créer 4 immeubles, 2 supermarchés, 1 banque

from model.cre_batiment import Batiment, Immeuble, Supermarche, Banque

print("Immeuble1: ",Immeuble("5 A Rue du Général Leclerc, 91230 Montgeron", 4, 0))
print("Immeuble2: ",Immeuble("1 Boulevard Sellier, 91230 Montgeron", 4, 32))
print("Immeuble3: ",Immeuble("2-16 Rue d'Eschborn, 91230 Montgeron", 5, 9))
print("Immeuble4: ",Immeuble("6 Rue de Chalandray, 91230 Montgeron", 4, 36))

print("Supermarché Super U: ",Supermarche("110 Avenue de la République, 91230 Montgeron", 1,22))
print("Supermarché Leclerc: ",Supermarche("72 Avenue Jean Jaurès, 91230 Montgeron", 1,28))

print("Banque LCL: ",Banque("63 Avenue de la République, 91230 Montgeron", 1,12, "LCL"))
