
from settings import Settings
import numpy as np
from pygame import sprite, Surface, SRCALPHA

class Movements:

    def __init__(self, chessboard):
        self.settings = Settings()
        self.markers = sprite.Group()
        self.board = chessboard
        offset = lambda e: int(e * (self.settings.tile_size))
        
        king = [ [offset(i), offset(j)] 
                    for i in range(-1, 2) 
                    for j in range(-1, 2)                      
                    ]   
        
        queen = [   [offset(i), offset(j)] 
                    for i in range(-4, 4) 
                    for j in range(-4, 4) 
                    ]    
        
        rook = [[offset(i), 0] for i in range(-4, 4)] + \
               [[0, offset(j)] for j in range(-4, 4) if offset(j) != 0 ]
        
        pawn = [  [0, offset(j)] for j in range(3)] + \
                [ [offset(i), offset(j)] for i in range(-1, 2, 2) for j in range(1)]
        
        bishop = [ [offset(i), offset(i+j)] 
                    for i in range(-4, 4) 
                    for j in range(-4, 4)
                    if i != 0
                    ]

        knight = [[offset(i), offset(2*i)] for i in range(-2, 3)] + \
                 [[offset(2*j), offset(j)] for j in range(-2, 3)  if offset(j) != 0] 
        
        self.movs = {'K': king, 'Q': queen, 'R': rook, 'P': pawn, 'B': bishop, 'N': knight}
                
    def _get_movs(self,list_moves,locate):   
        a = np.array(locate)
        b = np.array(list_moves)
        list_moves = a + b
        possible_moves = [tuple(coord) for coord in list_moves if all(x >= 0 for x in coord)]                
        return possible_moves
    
    def draw_markers(self, name, locate):
        marker_color = self.settings.marker_color
        list_movs = self.movs[name[1]]
        possible_movs = self._get_movs(list_movs, locate)
        Marker_Rect = Surface((self.settings.tile_size, self.settings.tile_size), SRCALPHA)
        
        for possible_mov in possible_movs:  
            Marker_Rect.fill(marker_color)
            self.board.screen.blit(Marker_Rect, possible_mov)
