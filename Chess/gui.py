import pygame
import sys
from Chess.settings import Settings

class Gui:
    def __init__(self):
        self.st = Settings()
        self.running = True
        pygame.init()        
        self.screen = pygame.display.set_mode((self.st.board_size, self.st.board_size))
        pygame.display.set_caption("Chess")

    def update_game(self):
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
        pygame.display.flip()

    def game_events(self): 
        """_summary_
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
    
    def run_gui(self):
        while self.running:
            self.game_events()
            self.update_game()    
    