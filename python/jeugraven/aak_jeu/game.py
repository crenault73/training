import pygame

from player import Player

# creer une seconde classe qui va représenter notre jeu

class Game:

    def __init__(self):
        # generer notre joueur lorsqu'une nouvelle partie est crée
        self.player = Player()
        self.pressed = {}