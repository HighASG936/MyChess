
from movements import Movements
from settings import Settings
import pygame


class Board:
    def __init__(self, chess_game):
        self.chess_game = chess_game
        self.settings = Settings()        
        self.screen = pygame.display.set_mode((self.settings.board_size, self.settings.board_size))
        self.movs = Movements(self)
        self.running = True
        pygame.init()        
       
        pygame.display.set_caption("Chess")
    
    def draw_board(self):
        """_summary_
        """
        for i in range(self.settings.board_n):
            for j in range(self.settings.board_n):                
                tile_color = self._set_tile_color([i,j])
                Board_Rect = pygame.Rect(i*self.settings.tile_size, 
                                         j*self.settings.tile_size, 
                                         self.settings.tile_size, 
                                         self.settings.tile_size)
                pygame.draw.rect(self.screen, tile_color, Board_Rect)

    def _set_tile_color(self, coord):
        i, j = coord
        tile_color = self.settings.tile_colors[(i + j) % 2] #Alternate Black and White        
        return tile_color 
    
