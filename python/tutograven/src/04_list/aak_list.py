# Créer une liste qui va stocker des pseudos

online_players=["Graven", "Anana", "Cleymax", "Bob"]
print(online_players)
print(online_players[0])
print(online_players[2])
print(online_players[len(online_players)-1])

#modifier "Graven" en "Gravenilvec"

online_players[0] = "Gravenilvec"
print(online_players)
online_players.insert(2, "Amira")
print(online_players)
online_players[2:5]=["Sam","sab","Fab"]
print(online_players)

online_players.append("Amira")
online_players.extend(["toto1", "toto2"])
online_players.remove("toto1")
del online_players[len(online_players)-1]
online_players.pop(4)
online_players.clear()

print(online_players)