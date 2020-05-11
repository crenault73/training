import pygame
import random


# Une classe qui représente le monstre
class Monster(pygame.sprite.Sprite):

    # Définir le constructeur de cette classe
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 541
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        # Infliger les dégâts
        self.health -= amount

        # Vérifier si le nouveau nombre de points de vie est >= 0
        if self.health <= 0:
            # Réapparaître comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        # Définir une couleur pour la jauge de vie (vert clair)
        bar_color = (111, 210, 46)
        # Définir une couleur pour l'arrière plan de la jauge (gris foncé)
        back_bar_color = (60, 63, 60)

        # Définir la position de notre jauge de vie ainsi que
        # sa largeur et son épaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 10, self.health, 5]
        # Définir la position de l'arrière plan de notre de jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 10, self.max_health, 5]

        # Dessiner notre bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # Le déplacement ne se fait que si il n'y a pas de collision avec un joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # Inflige des dégâts (au joueur)
            self.game.player.damage(self.attack)