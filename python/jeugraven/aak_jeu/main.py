import pygame
from projectile import Projectile
from monster import Monster
from game import Game
from player import Player




# <>

pygame.init()

# generer la fenetre de notre jeu

pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer l'arrier plan
background = pygame.image.load('assets/bg.jpg')

# charger le joueur
player = Player()

# charger notre jeu
game = Game()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan de notre jeu
    screen .blit(background, (0, -200))

    # appliquer l'image de notre joueur
    screen.blit(game.player.image, game.player.rect)

    # appliquer l'ensemble des images du groupe de projectile
    game.player.all_projectile.draw(screen)

    #appliquer l'ensemble des images du groupe de monstres

    game.all_monsters.draw(screen)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectile:
        projectile.move()

    # recuperer les monstres de notre jeu
    for monster in game.all_monsters:
        monster.forward()


    # verifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width() :
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()


    #mettre à jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False