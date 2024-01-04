
from settings import Settings

class Prunner:
    
    def __init__(self):
        """ """
        self.is_pair = lambda n: n%2 == 0
        self.settings = Settings()        
        self.into_range = lambda p, o: p[0]>=o[0] and p[1]>=o[1]
        
        board_size = self.settings.board_size
        self.into_board = lambda p: 0>p[0]>board_size and 0>p[1]>board_size
        self.is_Positive = lambda x1, x2: x1 > x2
        self.is_Negative = lambda x1, x2: x1 < x2
        self.prunned_moves = []
    
    def _prunning(self, oc, pc, cuadrant, move):
        """ """
        if (
             self.is_pair(cuadrant) and self.into_range(oc, pc)) or \
             (not self.is_pair(cuadrant) and self.into_range(pc, oc)
            ):
            self.prunned_moves.append(move)
    
    def _get_cuadrant(self, oc, pc):
        x1, y1 = oc
        x2, y2 = pc
        if self.is_Positive(x1, x2) and self.is_Positive(y1, y2):
            return 1 
        elif self.is_Negative(x1, x2) and self.is_Positive(y1, y2):
            return 2
        elif self.is_Negative(x1, x2) and self.is_Negative(y1, y2):
            return 3
        else:
            return 4
    
    def _eval_coords(self, oc, pc, move):
        """ """
        cuadrant = self._get_cuadrant(oc, pc)
        self._prunning(oc, pc, cuadrant, move)
    
    
    def get_prunned_moves(self, all_moves, oc, pc):
        """ """
        self.prunned_moves = []
        
        if oc in all_moves: 
            for move in all_moves:
                if self.into_board(move):
                    self._eval_coords(oc, pc, move)
            return self.prunned_moves
        else:
            return all_moves

        
        