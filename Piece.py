from my_utils.sprites import Sprites
import pygame
import os
from settings import Settings

class Piece:

    def __init__(self, chess_game, *args) -> None:
        
        self.chess_game, self.image, self.name, self.color, self.coord = args        
        self.dragging = False
        self.screen = self.chess_game.screen
        self.rect = self.image.get_rect()
        self.x, self.y = self.coord
        self.possible_movs = []

        settings = Settings()
        self.get_y_coord = lambda r: r * settings.tile_size
        self.direction = self._set_direction()        
        offset = lambda a: int(a * (self.settings.tile_size))  

    def blitme(self):
        """Draw the piece at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.coord  #Coordenates of piece        
        self.screen.blit(self.image, self.rect)