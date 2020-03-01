# Les listes

# Créer une liste qui va stocker des pseudos pour simuler un jeux en ligne
# Graven, Ananas, Max, etc

online_players = ["Graven", "Ananas", "Max", "Bob"]

print(online_players)
print(online_players[0])
print(online_players[2])
print(online_players[len(online_players) - 1])

# Modifier "Graven" -> "Gravenilevec"
online_players[0] = "Gravenilevec"
online_players.insert(3, "BernardGamer123")
online_players[4:5] = ["Paul", "Jack"]
print("Liste modifiée: " + str(online_players))

# En ajouter d'autres
# On imagine qu'un joueur "Gamer123" se connecte
online_players.append("Gamer123")
print("Ajout d'un joueur: " + str(online_players))
online_players.extend(["Gogumer1er", "Gigi2k"])
print("Ajout de plusieurs joueurs: " + str(online_players))

# On imagine que le joueur "Ananas" se déconnecte
online_players.pop(1)
print("Le joueur Ananas se déconnecte: " + str(online_players))
del online_players[3]
print("Le joueur Paul se déconnecte: " + str(online_players))
online_players.remove("Gigi2k")
print("Le joueur Gigi2k se déconnecte: " + str(online_players))

# On imagine que la partie est terminée, et que tous le joueurs sont supprimés
online_players.clear()
print("Suppression de tous les joueurs de la liste: " + str(online_players))
