

class Prunner:
    
    def __init__(self):
        """ """
        self.is_pair = lambda n: n%2 == 0
        self.into_range = lambda p, o: p[0] >= o[0] and p[1] >= o[1]
        self.is_Positive = lambda x: x > 0
        self.is_Negative = lambda x: x < 0
        self.prunned_moves = []
    
    def _prunning(self, oc, op, cuadrant, move):
        """ """
        if (
             self.is_pair(cuadrant) and self.into_range(op, pc)) or \
             (not self.is_pair(cuadrant) and self.into_range(pc, op)
            ):
            self.prunned_moves.append(move)
    
    def _get_cuadrant(self, coord):
        x, y = coord
        if self.is_Positive(x) and self.is_Positive(y):
            return 1 
        elif self.is_Negative(x) and self.is_Positive(y):
            return 2
        elif self.is_Negative(x) and self.is_Negative(y):
            return 3
        else:
            return 4
    
    def _eval_coords(self, oc, pc, move):
        """ """
        cuadrant = self._get_cuadrant(oc)
        self._prunning(oc, pc, cuadrant, move)
    
    
    def get_prunning_moves(self, all_moves, oc, pc):
        """ """
        self.prunned_moves = []
        
        if oc in all_moves: 
            for move in all_moves:
                self._eval_coords(all_moves, oc, pc, move)
        else:
            return all_moves

# if __name__ == "__main__":
    # prunner = Prunner()
    # pc = piece.coord
    # for other_piece in pieces:
    #     oc = other_piece.coord
    #    posible_moves = prunner.get_prunning_moves(all_moves, oc, pc)
        
        