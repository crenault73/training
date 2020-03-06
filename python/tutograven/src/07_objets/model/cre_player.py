# Player

class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur: ", pseudo, " / Points de vie: ", health, " / attack: ", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage
        print("Aïe... vous venez de subir ", damage, " points de dégats!")

    def attack_player(self, target_player):
        if self.weapon is not None:
            target_player.damage(self.attack + self.weapon.get_damage())
        else:
            target_player.damage(self.attack)

    def set_weapon(self, weapon):
        self.weapon = weapon
