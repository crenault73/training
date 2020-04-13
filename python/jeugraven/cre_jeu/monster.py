import pygame


# Une classe qui représente le monstre
class Monster(pygame.sprite.Sprite):

    # Définir le constructeur de cette classe
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 541
        self.velocity = 3

    def forward(self):
        # Le déplacement ne se fait que si il n'y a pas de collision avec un joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
