import pygame
from game import Game

pygame.init()

# Generer la fenetre de notre jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# Importer l'arrière plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# Charger notre banière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = int(screen.get_width() / 4)

# Charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = int(screen.get_width() / 3.33)
play_button_rect.y = int(screen.get_height() / 2)

# Charger un jeu
game = Game()

running = True

# Boucle tant que la variable running est vraie
while running:

    # Appliquer l'arrière-plan de notre jeu
    screen.blit(background, (0, -200))

    # Vérifier que le jeu est lancé
    if game.is_playing:
        # Déclencher les instructions de la partie
        game.update(screen)
    # Sinon le jeu n'est pas encore commencé
    else:
        # Ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verification pour savoir si la souris est en collision avec le bouton play
            if play_button_rect.collidepoint(event.pos):
                # Mettre le jeu en mode lancé
                game.start()