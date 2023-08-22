
from settings import Settings
import numpy as np
from pygame import sprite, Surface, SRCALPHA

class Movements:

    def __init__(self, chessboard):
        super().__init__()
        self.settings = Settings()
        self.markers = sprite.Group()
        self.board = chessboard
        self.surface_size = (self.settings.tile_size, self.settings.tile_size)
        self.marker_color = self.settings.marker_color
        offset = lambda a: int(a * (self.settings.tile_size))

        self.horizontal_moves = [[offset(i), 0] for i in range(-8, 9)]
        self.vertical_moves = [[0, offset(j)] for j in range(-8, 9) if offset(j) != 0 ]
        self.main_diagonal_moves = [ [offset(i), offset(i)] for i in range(-8, 9)]
        self.secondary_diagonal_moves = [ [offset(i), -offset(i)] for i in range(-8, 9)]
        self.pawn_attack_moves = [[offset(i), offset(1)] for i in [-1, 1]]
        rook = self.horizontal_moves + self.vertical_moves
        bishop = self.main_diagonal_moves + self.secondary_diagonal_moves
        queen = rook + bishop
        king = [ [offset(i), offset(j)] for i in range(-1, 2) for j in range(-1, 2)]
        pawn = [[0, offset(j)] for j in range(2)]
        knight = [[0, 0]] + \
                 [[k*offset(1), l*offset(2)] for k in [-1, 1] for l in [-1, 1] ] + \
                 [[k*offset(2), l*offset(1)] for k in [-1, 1] for l in [-1, 1] ]

        self.moves = {'K': king, 'Q': queen, 'R': rook, 'P': pawn, 'B': bishop, 'N': knight}


    def _get_all_moves(self,list_moves,locate, direction):
        a = np.array(locate)
        b = np.array(list_moves)
        list_moves = a + (direction*b)
        possible_moves = [tuple(coord)
                          for coord in list_moves
                          if all(x < self.settings.board_size for x in coord)]
        return possible_moves

    def _pawn_movements(self, name, moves, other_piece):
        # moves.remove(other_piece.coord)
        if name == 'P':
        #    for move in moves:
        #        print(dir(move))
        #        pass
            pass

    def _get_cuadrant(self, move1, move2, moves):
        if move1 == move2:
            x, y = move2            

            index_piece_in_moves_list = moves.index(move1)
            index_other_piece_in_moves_list = moves.index(move2)
            if x>0 and y>0:                
                return moves[index_piece_in_moves_list:index_other_piece_in_moves_list]
            # elif x<0 and y>0:
            #    return 2
            #elif x<0 and y<0:
            #    return 3
            #elif x>0 and x<0:
            #    return 4
        else:
            return None

    def _bishop_movements(self, piece, all_moves, other_move):
        name = piece.name[1]
        prunned_moves = []
        if name == 'B':
            for move in all_moves:
                prunned_moves.append(self._get_cuadrant(move, other_move, all_moves))
        return prunned_moves

    def _prunning_possible_moves(self, piece, all_moves, grouppieces):
        all_moves = all_moves.copy()
        prunned_moves = []
        for other_piece in grouppieces:
            other_move = other_piece.coord
            prunned_moves.append(self._bishop_movements(piece, all_moves, other_move))
            # if other_piece.coord in prunned_moves and piece.coord != other_piece.coord:
                # prunned_moves.remove(other_piece.coord)
            # self._pawn_movements(piece, prunned_moves, other_piece)        
        return prunned_moves

    def _get_possible_moves(self, piece, locate=None, grouppieces=None):
        name = piece.name[1]
        direction = piece.direction
        list_moves = self.moves[name]

        if locate == None:
            locate = piece.coord

        all_moves = self._get_all_moves(list_moves, locate, direction)
        possible_moves = self._prunning_possible_moves(piece, all_moves, grouppieces)
        return possible_moves

    def draw_markers(self, piece, locate, grouppieces=None):
        Marker_Surface = Surface(self.surface_size, SRCALPHA)
        possible_moves = self._get_possible_moves(piece, locate, grouppieces)
        for possible_mov in possible_moves:
            Marker_Surface.fill(self.marker_color)
            self.board.screen.blit(Marker_Surface, possible_mov)


