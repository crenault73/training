import pygame
from player import Player
from monster import Monster


# Classe qui représente le jeu
class Game:

    def __init__(self):
        # Generer notre joueur et le mettre dans un groupe (groupe utilisé pour la collision)
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def check_collision(self,sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

'''
if event.key == pygame.K_RIGHT:
    print("Déplacement vers la droite")
    game.player.move_right()
elif event.key == pygame.K_LEFT:
    print("Déplacement vers la gauche")
    game.player.move_left()
'''
