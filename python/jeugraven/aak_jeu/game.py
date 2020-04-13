from player import Player
from monster import Monster
import pygame



# creer une seconde classe qui va représenter notre jeu

class Game:

    def __init__(self):
        # generer notre joueur lorsqu'une nouvelle partie est crée
        self.player = Player(self)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Monster())