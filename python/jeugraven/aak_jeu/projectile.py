import pygame

# <>


# définir la classe qui va gérer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    # définir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectile.remove(self)


    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # vérifier si le projectile entre en collision avec un monstre

        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprimer le projectile
            self.remove()
            #infliger des dégats
            monster.damage(self.player.attack)

        # verifier si notre projectile n'est plus présent dans notre screen
        if self.rect.x > 1080:
            #supprimer le projectile
            self.remove()
            print("Projectile supprimé")




