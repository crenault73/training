from model.aak_player import Player
from model.aak_weapon import Weapon


player1 = Player("Amira", 20, 3)
player2 = Player("Sam", 50, 10)
print("Pseudo : ",player1.get_pseudo())
player1.damage(3)
print("Vous possedez désormais ", player1.get_healt(), "points")

#print("Bienvenue au joueur ", player1.pseudo)
#print("Bienvenue au joueur ", player2.pseudo)

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())
print("Bienvenue au joueur ", player1.get_pseudo(), "/ Points de vie :", player1.get_healt(), "/ Attack : ", player1.get_attack())
print("Bienvenue au joueur ", player2.get_pseudo(), "/ Points de vie :", player2.get_healt(), "/ Attack : ", player2.get_attack())

knife=Weapon("Couteau", 3)
player1.set_weapon(knife)


player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())
print("Bienvenue au joueur ", player1.get_pseudo(), "/ Points de vie :", player1.get_healt(), "/ Attack : ", player1.get_attack())
print("Bienvenue au joueur ", player2.get_pseudo(), "/ Points de vie :", player2.get_healt(), "/ Attack : ", player2.get_attack())



player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())
print("Bienvenue au joueur ", player1.get_pseudo(), "/ Points de vie :", player1.get_healt(), "/ Attack : ", player1.get_attack())
print("Bienvenue au joueur ", player2.get_pseudo(), "/ Points de vie :", player2.get_healt(), "/ Attack : ", player2.get_attack())





