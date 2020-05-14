from player import Player
from monster import Monster
import pygame



# creer une seconde classe qui va représenter notre jeu

class Game:

    def __init__(self):
        #définir si notre jeu a commencé ou non
        self.is_playing = False
        # generer notre joueur lorsqu'une nouvelle partie est crée
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100 de vie, remettre le joueur en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image de notre joueur
        screen.blit(self.player.image, self.player.rect)

        # appliquer l'ensemble des images du groupe de projectile
        self.player.all_projectile.draw(screen)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # appliquer l'ensemble des images du groupe de monstres

        self.all_monsters.draw(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectile:
            projectile.move()

        # recuperer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # verifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        self.all_monsters.add(Monster(self))