import pygame
from projectile import Projectile


# Une classe qui représente notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 7
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount >= amount:
            self.health -= amount
        else:
            # Si le joueur n'a plus de point de vie
            self.health = 0
            self.game.game_over()

    def update_health_bar(self, surface):
        # Définir une couleur pour la jauge de vie (vert clair)
        bar_color = (111, 210, 46)
        # Définir une couleur pour l'arrière plan de la jauge (gris foncé)
        back_bar_color = (60, 63, 60)

        # Définir la position de notre jauge de vie ainsi que
        # sa largeur et son épaisseur
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]
        # Définir la position de l'arrière plan de notre de jauge de vie
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]

        # Dessiner notre bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def lance_projectile(self):
        # Créer une nouvelle instance du projectile et l'ajoute dans la liste de projectiles
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # Si le joueur n'est pas en collision avec un monstre:
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
