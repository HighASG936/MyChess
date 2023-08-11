import pygame
from settings import Settings

class Board:
    def __init__(self):
        self.st = Settings()
        self.running = True
        pygame.init()        
        self.screen = pygame.display.set_mode((self.st.board_size, self.st.board_size))
        pygame.display.set_caption("Chess")

    def draw_board(self):
        """_summary_
        """
        for i in range(8):
            for j in range(8):
                tile_color = self.st.tile_colors[(i + j) % 2] #Alternate Black and White 
                Board_Rect = pygame.Rect(i*self.st.tile_size, 
                                         j*self.st.tile_size, 
                                         self.st.tile_size, 
                                         self.st.tile_size)
                pygame.draw.rect(self.screen, tile_color, Board_Rect)
        