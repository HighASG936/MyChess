"""Chess game, for learning to grab images from a sprite sheet."""

from settings import Settings
from chess_set import ChessSet
from board import Board
from coordinates import Coordinates
import sys
import pygame
import math
import os
from time import sleep

class ChessGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        self.coords = Coordinates()
        self.locations = self.coords.get_board()
        self.tiles_centers = self.coords.get_snap_coordinates()
        pygame.init()
        self.settings = Settings()
        self.board = Board()
        self.screen = pygame.display.set_mode((self.settings.board_size, self.settings.board_size))
        pygame.display.set_caption("Chess")

        self.chess_set = ChessSet(self)

    def _dragging_piece(self, event):
        for sprite in self.chess_set.Pieces_Group:                                
            if sprite.rect.collidepoint(event.pos):
                sprite.dragging = not sprite.dragging        
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()                        
            elif event.type == pygame.MOUSEBUTTONDOWN:                   
                self._dragging_piece(event)

    def _snap_piece(self):
        current_position = pygame.mouse.get_pos()
        centers = self.tiles_centers
        distances = [
                        math.sqrt( (center[0] - current_position[0])**2  +  (center[1] - current_position[1])**2 )
                        for center in centers
                    ]
        min_distance_index = distances.index(min(distances))
        new_pos = centers[min_distance_index]    
        return new_pos
                                
    def _update_screen(self):        
        self.screen.fill(self.settings.bg_color)
        self.board.draw_board()                
        
        for sprite in self.chess_set.Pieces_Group:  
            if sprite.dragging:                
                sprite.rect.center = self._snap_piece()
        
        self.chess_set.Pieces_Group.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()            

if __name__ == '__main__':
    chess_game = ChessGame()
    chess_game.run_game()
    
    