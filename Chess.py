"""Chess game, for learning to grab images from a sprite sheet."""

from settings import Settings
from chess_set import ChessSet
from board import Board
from coordinates import Coordinates
from sys import exit
from math import sqrt
import pygame

class ChessGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        self.coords = Coordinates()
        self.locations = self.coords.get_board()
        self.tiles_centers = self.coords.tiles_centers        
        pygame.init()
        self.settings = Settings()
        self.board = Board(self)
        self.screen = pygame.display.set_mode((self.settings.board_size, self.settings.board_size))
        self.last_x, self.last_y = 0, 0
        pygame.display.set_caption("Chess")

        self.chess_set = ChessSet(self)

    def _dragging_piece(self, event):
        for sprite in self.chess_set.Pieces_Group:                                
            if sprite.rect.collidepoint(event.pos):                
                sprite.dragging = not sprite.dragging
                if sprite.dragging:                     
                    self.last_x, self.last_y = sprite.x, sprite.y

    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()                        
            elif event.type == pygame.MOUSEBUTTONDOWN:                   
                self._dragging_piece(event)

    def _snap_piece(self):
        current_position = pygame.mouse.get_pos()
        centers = self.tiles_centers
        distances = [
                        sqrt( (center[0] - current_position[0])**2  +  (center[1] - current_position[1])**2 )
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
                self.board.movs.draw_markers(sprite.name, [self.last_x, self.last_y] ) 
                sprite.rect.center = self._snap_piece()
                sprite.x, sprite.y = sprite.rect.topleft        
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
    
    