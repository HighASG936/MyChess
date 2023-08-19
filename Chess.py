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
        for piece in self.chess_set.Pieces_Group:                                
            if piece.rect.collidepoint(event.pos):                
                piece.dragging = not piece.dragging
                if piece.dragging:                     
                    
                    self.last_x, self.last_y = piece.rect.topleft                      
                    piece.possible_movs = self.board.movs._get_possible_movs(piece, piece.coord)                    
                    break
        print(piece.x, piece.y)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()                        
            elif event.type == pygame.MOUSEBUTTONDOWN:                   
                self._dragging_piece(event)

    def _snap_piece(self, piece):
        current_x, current_y = pygame.mouse.get_pos()
        movs = piece.possible_movs
        distances = [
                        sqrt( (mov_x - current_x)**2  +  (mov_y - current_y)**2 )
                        for mov_x, mov_y in movs
                    ]
        min_distance_index = distances.index(min(distances))
        new_pos = movs[min_distance_index]    
        return new_pos
                                
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.board.draw_board()                
        
        for piece in self.chess_set.Pieces_Group:  
            if piece.dragging:        
                self.board.movs.draw_markers(piece, [self.last_x, self.last_y] ) 
                piece.rect.topleft = self._snap_piece(piece)
                piece.x, piece.y = piece.rect.topleft
                break
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
    
    