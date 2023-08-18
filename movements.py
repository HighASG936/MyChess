
from settings import Settings
import numpy as np

class Movements:

    def __init__(self):        
        super().__init__()
        self.settings = Settings()
        offset = lambda e: int(e * (self.settings.tile_size/2))
        
        self.king = [ [offset(i), offset(j)] 
                     for i in range(-1, 2) 
                     for j in range(-1, 2)                      
                    ]   
        
        self.queen = [ [offset(i), offset(j)] 
                     for i in range(-4, 4) 
                     for j in range(-4, 4) 
                    ]    
        
        self.rook = [[offset(i), 0] for i in range(-4, 4)] + \
                    [[0, offset(j)] for j in range(-4, 4) if offset(j) != 0 ]
        
    def get_movs(self,list_moves,locate):   
        a = np.array(locate)
        b = np.array(list_moves)
        list_moves = a + b
        possible_moves = [coord.tolist() for coord in list_moves if all(x >= 0 for x in coord)]                
        return possible_moves
    
if __name__ == '__main__':
    mov = Movements()
    # print(mov.get_movs(mov.king, [0, 0]))    
    # print(mov.get_movs(mov.queen, [0, 0]))
    print(mov.get_movs(mov.rook, [0, 0]))
    
    