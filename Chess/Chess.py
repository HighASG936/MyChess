
from Chess import new_board, get_list_squares_board, squares
from Chess import board, remove_piece, put_piece
from Chess import is_valid_piece, Emptysquare
from Chess import Gui

import sys

class Chess:
    
    def __init__(self):
        new_board()
        self.gui_board = Gui()
    
    def draw_board(self):
        rows = [str(board[x]) + '\n' for x in range(0, len(board))]
        
        #print A, B, C, D... labels
        labels = get_list_squares_board()
        format_label = "{:<11}" * (len(labels) + 1)
        print(format_label.format("", *labels))
        
        #Print board
        i = 1
        for row in rows:
            format_row = "{:^2}" * (len(row) + 1)            
            print(f"{i}{format_row.format('', *row)}")
            i += 1
    
    def move_piece(self, move_tuple):
        """_summary_

        Args:
            move_tuple (_type_): _description_
        """
        origin, destiny = move_tuple
        ori_coords = squares[origin]
        ori_x, ori_y = ori_coords
               
        try:
            origin_piece_name = board[ori_x][ori_y]
            is_valid_piece(origin_piece_name)
        except Emptysquare as es:
            print(f"Location {origin}:[{ori_x},{ori_y}] {es.message}")            
        else:
            dest_coords = squares[destiny]
            remove_piece(ori_coords)
            put_piece(origin_piece_name, dest_coords)
    