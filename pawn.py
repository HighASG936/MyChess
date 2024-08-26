from my_utils.sprites import Sprites
import pygame
import os
from settings import Settings
import Piece

class Pawn:

    def __init__(Piece, self, chess_game, *args) -> None:
        Piece.chess_game, Piece.image, Piece.name, Piece.color, Piece.coord = args        
        Piece.dragging = False
        Piece.screen = Piece.chess_game.screen
        Piece.rect = Piece.image.get_rect()
        Piece.x, Piece.y = Piece.coord
        Piece.possible_movs = []

        settings = Settings()
        get_y_coord = Piece.get_y_coord()
        self.direction = self._set_direction()  
        offset = Piece.offset

        self.pawn_attack_moves = [[offset(i), offset(1)] for i in [-1, 1]]
        movement_pawn = [[0, offset(j)] for j in range(2)]


    def _set_direction(self) -> int:
        """axuliar method to obtain the direction of the pawn"""
        if self.y > self.get_y_coord(5):
            return -1
        return 1