# Classe qui représente le jeu
from player import Player


class Game:

    def __init__(self):
        # Generer notre joueur
        self.player = Player()
        self.pressed = {}

'''
if event.key == pygame.K_RIGHT:
    print("Déplacement vers la droite")
    game.player.move_right()
elif event.key == pygame.K_LEFT:
    print("Déplacement vers la gauche")
    game.player.move_left()
'''