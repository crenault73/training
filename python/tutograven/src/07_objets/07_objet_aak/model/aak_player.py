
class Player:

    def __init__(self, pseudo, healt, attack):
        self.pseudo=pseudo
        self.health=healt
        self.attack=attack
        self.weapon=None
        print("Bienvenue au joueur ", self.pseudo, "/ Points de vie :", self.health, "/ Attack : ",self.attack)

    def get_pseudo(self):
        return self.pseudo

    def get_healt(self):
        return self.health

    def get_attack(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage
        print("Aie ... vous venez de subir ", damage, "dégats")


    def attack_player(self, target_player):

        damage=self.attack

        if self.has_weapon():
            damage += self.weapon.get_damage_amount()

        target_player.damage(damage)


    def set_weapon(self, weapon):
        self.weapon = weapon


    def has_weapon(self):
        self.weapon is not None


class Warrior(Player):

    def __init__(self, pseudo, healt, attack):
        super().__init__(pseudo, healt, attack)
        self.armor=3
        print("Bienvenue au guerrier ", self.pseudo, "/ Points de vie :", self.health, "/ Attack : ",self.attack)

    def damage(self, damage):
      if self.armor > 0:
          damage=0
          self.armor -= 1
      super().damage(damage)

    def blade(self):
        self.armor=3
        print("Les points d'arumure on été rechargés")

    def get_armor(self):
        return self.armor

