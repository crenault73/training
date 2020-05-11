import pygame


# Définit la classe qui va gérer les projectiles

# Une classe qui représente notre joueur
class Projectile(pygame.sprite.Sprite):

    # Définir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 12
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # Tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # Verifier si le projectile rentre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # Alors on supprime le projectile
            self.remove()
            # Infliger des dégâts
            monster.damage(self.player.attack)

        # Verifier si notre projectile n'est plus présent sur l'écran
        if self.rect.x > 1080:
            # Supprimer le projectile (en dehors de l'écran)
            self.remove()
            print("All projectiles: ", self.player.all_projectiles)
