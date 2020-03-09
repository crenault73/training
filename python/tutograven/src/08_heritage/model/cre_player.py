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
        print("Dealing Damage: ", damage)
        self.health -= damage
        print("Aïe... ", self.pseudo, " vient de subir ", str(damage), " points de dégats!")

    def attack_player(self, target_player):
        if self.weapon is not None:
            target_player.damage(self.attack + self.weapon.get_damage())
        else:
            target_player.damage(self.attack)

    def set_weapon(self, weapon):
        self.weapon = weapon


class Warrior(Player):

    def __init__(self, pseudo, health, attack, armor):
        super().__init__(pseudo, health, attack)
        self.armor = armor
        print("Bienvenue au guerrier: ", pseudo, " / Points de vie: ", health, " / attack: ", attack, " / armure: ",
              self.armor)

    def damage(self, damage):
        # Subit aucun dégat si points d'armure >= damage,
        # sinon damage - points d'armure si armure > 0
        # si armure < 0, subit tous les dégats
        if self.armor > 0:
            self.armor -= damage
            damage = 0 if self.armor > 0 else -self.armor
        super().damage(damage)

    def blade(self):
        self.armor = 3
        print("Les points d'armure ont été rechargés")

    def get_armor(self):
        return self.armor
