from model.cre_player import Player

player1 = Player("Graven", 20, 3)
print("Pseudo: ", player1.pseudo)
player1.damage(3)
print("Vous possedez desormais ", player1.get_health(), " points de vie.")
player2 = Player("Bob", 20, 5)
print("Pseudo: ", player2.get_pseudo())

player1.attack_player(player2)
print(player1.get_pseudo(), " attaque ", player2.get_pseudo())
print("Etat du joueur: ", player1.get_pseudo(), " / Points de vie: ", player1.get_health(), " / attack: ",
      player1.get_attack())
print("Etat du joueur: ", player2.get_pseudo(), " / Points de vie: ", player2.get_health(), " / attack: ",
      player2.get_attack())
