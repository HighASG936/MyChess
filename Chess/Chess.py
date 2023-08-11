"""Chess game, for learning to grab images from a sprite sheet."""

from settings import Settings
from chess_set import ChessSet
from board import Board
from coordinates import Coordinates
import sys
import pygame


class ChessGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        self.coords = Coordinates()
        self.locations = self.coords.get_board()
        pygame.init()
        self.settings = Settings()
        self.board = Board()
        self.screen = pygame.display.set_mode((self.settings.board_size, self.settings.board_size))
        pygame.display.set_caption("Chess")

        self.chess_set = ChessSet(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):        
        self.screen.fill(self.settings.bg_color)
        self.board.draw_board()
        self.chess_set.update_board()
        #self.chess_set.draw_piece('BN', 2, 3)
        
        # Draw a row of black pieces.
        #for index, piece in enumerate(self.chess_set.pieces[:6]):
        #    piece.x = index * 100
        #    piece.blitme()

        # Draw a row of white pieces.
        #for index, piece in enumerate(self.chess_set.pieces[6:]):
        #    piece.x = index * 100
        #    piece.y = 100
        #    piece.blitme()

        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

if __name__ == '__main__':
    chess_game = ChessGame()
    chess_game.run_game()