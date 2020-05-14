import pygame
from player import Player
from monster import Monster


# Classe qui représente le jeu
class Game:

    def __init__(self):
        # Définir si notre jeu à commencé
        self.is_playing = False
        # Generer notre joueur et le mettre dans un groupe (groupe utilisé pour la collision)
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # Remettre le jeu à zéro: retirer les monstres, remettre le joueur à 100 points de vie, jeu en attente
        # self.all_monsters.clear()
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # Appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Récuppérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Récuppérer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # Appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # Appliquer l'ensemble des images de mon groupe de monstres
        self.all_monsters.draw(screen)

        # Vérifier si le joueur souhaite aller à gauche où à droite:
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
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
