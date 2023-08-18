"""Module to represent a chess set, and individual pieces."""

from my_utils.sprites import Sprites
import pygame
import os

class ChessSet:
    """
    Represents a set of chess pieces.
    Each piece is an object of the Piece class.
    """

    def __init__(self, chess_game):
        """Initialize attributes to represent the overall set of pieces."""
        self.chess_game = chess_game
        self.pieces = []
        self.Pieces_Group = pygame.sprite.Group()
        self.filename = os.path.join(os.path.dirname(__file__), 'images', 'chess_pieces.bmp')    
        self.Sprites_pieces = Sprites(self.filename)
        self._load_pieces()        
        

    def _load_pieces(self):
        """Builds the overall set:
        - Loads images from the sprite sheet.
        - Creates a Piece object, and sets appropriate attributes
          for that piece.
        - Adds each piece to the list self.pieces.
        """

        # Load all piece images.              
        piece_images = self.Sprites_pieces.load_grid_images(2, 
                                                            6, 
                                                            x_margin=64,                                                                  
                                                            x_padding=72, 
                                                            y_margin=68, 
                                                            y_padding=48)

        colors = ['B', 'W']
        names = ['K', 'Q', 'R', 'B', 'N', 'P']
        i = 0
        j = 0 
        image_piece_index = 0
        for color in colors:
            for name in names:
                image = piece_images[image_piece_index]                                
                self._create_piece_object(image, color, name)
                image_piece_index += 1

    def _create_piece_object(self, image, color, name):
        board = self.chess_game.locations
        current_piece = f"{color}{name}"                
        for i in range(len(board)):
            for j in range(len(board)):
                tile = board[i][j]
                if tile == current_piece:
                    coord = (self.chess_game.settings.tile_size * j,
                             self.chess_game.settings.tile_size * i)
                    piece = Piece(self.chess_game, image, current_piece, color, coord)                                                                                
                    self.Pieces_Group.add_internal(piece)
                    piece.blitme()

class Piece:
    """Represents a chess piece."""

    def __init__(self, chess_game, image, name, color, coord):
        """Initialize attributes to represent a ches piece."""
        super().__init__()

        self.image = image
        self.name = name
        self.color = color
        self.dragging = False
        self.screen = chess_game.screen
        self.rect = self.image.get_rect()
        self.x, self.y = coord
        self.direction = self._set_direction()

    def _set_direction(self):
        if self.name[1] == 'P' and self.y > 551:
            return -1
        return 1

    def blitme(self):
        """Draw the piece at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y  #Coordenates of piece        
        self.screen.blit(self.image, self.rect)
        
