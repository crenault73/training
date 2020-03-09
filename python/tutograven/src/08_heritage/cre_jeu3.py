from model.cre_player import Player, Warrior
#from model.cre_player import Warrior

player = Player("Graven", 20, 2)
warrior = Warrior("DarkWarrior", 30, 4, 3)
warrior.damage(1)
warrior.damage(4)
warrior.damage(5)

if issubclass(Warrior, Player):
      print("Le guerrier est bien une spécialisation de Player.")