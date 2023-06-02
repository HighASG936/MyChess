
import pygame
from pygame.sprite import Sprite

class Board(Sprite):

    def __init__(self, ch):
        super().__init__()
        self.settings = ch.settings
        self.screen = ch.screen
        self.screen_rect = ch.screen.get_rect()
        #self.chess_set = ch.chess_set()
        self.board_rect = pygame.Rect(0,0, self.settings.board_long, self.settings.board_long)

        self.positions = {'a1': (0,0), 'b1': (0,0), 'c1': (0,0), 'd1': (0,0), 'e1': (0,0), 'f1': (0,0), 'g1': (0,0), 'h1': (0,0),
                          'a2': (0,0), 'b2': (0,0), 'c2': (0,0), 'd2': (0,0), 'e2': (0,0), 'f2': (0,0), 'g2': (0,0), 'h2': (0,0),
                          'a3': (0,0), 'b3': (0,0), 'c3': (0,0), 'd3': (0,0), 'e3': (0,0), 'f3': (0,0), 'g3': (0,0), 'h3': (0,0),
                          'a4': (0,0), 'b4': (0,0), 'c4': (0,0), 'd4': (0,0), 'e4': (0,0), 'f4': (0,0), 'g4': (0,0), 'h4': (0,0),
                          'a5': (0,0), 'b5': (0,0), 'c5': (0,0), 'd5': (0,0), 'e5': (0,0), 'f5': (0,0), 'g5': (0,0), 'h5': (0,0),
                          'a6': (0,0), 'b6': (0,0), 'c6': (0,0), 'd6': (0,0), 'e6': (0,0), 'f6': (0,0), 'g6': (0,0), 'h6': (0,0),
                          'a7': (0,0), 'b7': (0,0), 'c7': (0,0), 'd7': (0,0), 'e7': (0,0), 'f7': (0,0), 'g7': (0,0), 'h7': (0,0),
                          'a8': (0,0), 'b8': (0,0), 'c8': (0,0), 'd8': (0,0), 'e8': (0,0), 'f8': (0,0), 'g8': (0,0), 'h8': (0,0),
                          }

    def set_coordinates(self):
        for position in positions.keys:
            position = (33, 33)


    def draw_board(self):
        #Draw overall board
        self.board_rect.center = self.screen_rect.center
        pygame.draw.rect(self.screen, self.settings.white_cell_color, self.board_rect)
        factor = 1
        for row in range(0, 8):
            factor = not factor
            left_offset = self.settings.cell_long * factor
            flag_color = False
            for column in range(0,7):
                flag_color = not flag_color
                if flag_color == True:
                    cell_color = self.settings.black_cell_color
                else:
                    cell_color = self.settings.white_cell_color

                self.cell_rect = pygame.Rect(0,0, self.settings.cell_long, self.settings.cell_long)
                self.cell_rect.left = (self.settings.cell_long * column) + int(self.board_rect.left) + left_offset
                self.cell_rect.top = int(self.board_rect.top) + ( self.settings.cell_long * row)
                pygame.draw.rect(self.screen, cell_color, self.cell_rect)


