import pygame
from player import Player
from game import Game

pygame.init()

# Generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# Importer l'arrière plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# Charger un jeu
game = Game()

running = True

# Boucle tant que la variable running est vraie
while running:

    # Appliquer l'arrière-plan de notre jeu
    screen.blit(background, (0, -200))

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)

    # Récuppérer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # Récuppérer les monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # Appliquer l'ensemble des images de mon groupe de monstres
    game.all_monsters.draw(screen)

    # Vérifier si le joueur souhaite aller à gauche où à droite:
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme la fenetre
    for event in pygame.event.get():

        # que l'evenement est la fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Detecter si un joueur lache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # Détecter si la touche espace est enclenchée
            if event.key == pygame.K_SPACE:
                game.player.lance_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
