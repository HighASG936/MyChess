
from settings import Settings
import numpy as np
from pygame import sprite, Surface, SRCALPHA

class Movements:

    def __init__(self, chessboard):
        self.settings = Settings()
        self.markers = sprite.Group()
        self.board = chessboard
        self.surface_size = (self.settings.tile_size, self.settings.tile_size)
        self.marker_color = self.settings.marker_color 
        
        offset = lambda e: int(e * (self.settings.tile_size))

        king = [ [offset(i), offset(j)] 
                    for i in range(-1, 2) 
                    for j in range(-1, 2)                      
                    ]       
        
        rook = [[offset(i), 0] for i in range(-8, 9)] + \
               [[0, offset(j)] for j in range(-8, 9) if offset(j) != 0 ]
                
        bishop = [ [offset(i), k*offset(i)] for i in range(-8, 9) for k in [-1, 1]]

        queen = rook + bishop

        pawn = [[0, offset(j)] for j in range(3)] + \
               [[offset(i), offset(1)] for i in [-1, 1]]

        knight = [[k*offset(1), l*offset(2)] for k in [-1, 1] for l in [-1, 1] ] + \
                 [[k*offset(2), l*offset(1)] for k in [-1, 1] for l in [-1, 1] ] 
        
        self.movs = {'K': king, 'Q': queen, 'R': rook, 'P': pawn, 'B': bishop, 'N': knight}


    def _get_all_movs(self,list_moves,locate, direction):   
        a = np.array(locate)
        b = np.array(list_moves)
        list_moves = a + (direction*b)
        possible_moves = [tuple(coord) 
                          for coord in list_moves 
                          if all(x <= self.settings.board_size for x in coord)]                
        return possible_moves
    
    def _get_possible_movs(self, sprite, locate=None):
        
        if locate == None:
            locate = sprite.coord
        
        name = sprite.name[1]
        direction = sprite.direction
        list_movs = self.movs[name]
        return self._get_all_movs(list_movs, locate, direction)
    
    def draw_markers(self, sprite, locate):                  
        Marker_Surface = Surface(self.surface_size, SRCALPHA)         
        possible_movs = self._get_possible_movs(sprite, locate)            
        for possible_mov in possible_movs:  
            Marker_Surface.fill(self.marker_color)
            self.board.screen.blit(Marker_Surface, possible_mov)


