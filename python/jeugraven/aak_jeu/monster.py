import pygame
import random


# créer une classe qui va gérer la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):

        #infliger les degats
        self.health -= amount

        # verifier si son nouveau nombre de points de vie est inferieur ou égale à zéro

        if self.health <= 0:
            # réaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health



    def update_health_bar(self, surface):

        #dessiner notre barre de vie

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])

        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):

        # le déplacement ne pourra se faire uniquement que s'il n'ya pas de collision avec un groupe de joueurs
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

        # si le monstre est en collision avec le joueur
        else:
            # infliger des dégats au joueur
            self.game.player.damage(self.attack)

