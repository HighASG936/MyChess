

class Coordinates:
    
    def __init__(self):
        self.board = []
        self.index_x = 0
        self.index_y = 1
        self.squares = {}
        self.start_positions = {'WR': ["A1", "H1"],  # White Rooks
                                'BR': ["A8", "H8"],  # Black Rooks
                                'WN': ["B1", "G1"],  # White Knights
                                'BN': ["B8", "G8"],  # Black Knights
                                'WB': ["C1", "F1"],  # White Bishops
                                'BB': ["C8", "F8"],  # Black Bishops
                                'WQ': ["D1"],        # White Queen
                                'BQ': ["D8"],        # Black Queen
                                'WK': ["E1"],        # White King
                                'BK': ["E8"],        # Black King
                                'WP': ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],  # White Pawns
                                'BP': ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],  # Black Pawns
                            }            
        self._fill_board_matrix()
        self._generate_matrix_of_board()
        self._put_pieces_on_board()
        
    def _fill_board_matrix(self):
        #Create matriz to chess board
        for row in range(0, 8):
            self.board.append([])
            for _ in range(0,8):
                self.board[row].append('')  
    
    def _get_list_literals_columns(self):
        """
    
        """
        return [chr(x) for x in range(ord('A'), ord('I'))]

    def _generate_matrix_of_board(self):
        """
    
        """
        letters = self._get_list_literals_columns()
        for row in letters:
            for col in range(1, len(self.board) +1):
                key = f"{row}{col}"
                self.squares[key] = [col -1, letters.index(row) +1]

    def _put_piece(self, piece, coord):
        """_summary_

        Args:
            piece (_type_): _description_
            coord (_type_): _description_
        """
        x, y = coord[self.index_x], coord[self.index_y] -1
        self.board[x][y] = piece

    def _remove_piece(self, coord):
        """_summary_

        Args:
            coord (_type_): _description_
        """
        self._put_piece('--', coord)

    def _put_pieces_on_board(self):
        #Put the set chess on board
        for key, value in self.start_positions.items():
            for pos in value:
                self._put_piece(str(key), self.squares[pos])    
        
    # def move_piece(self, move_tuple):
    #     """_summary_

    #     Args:
    #         move_tuple (_type_): _description_
    #     """
    #     origin, destiny = move_tuple
    #     ori_coords = squares[origin]
    #     ori_x, ori_y = ori_coords
               
    #     try:
    #         origin_piece_name = board[ori_x][ori_y]
    #         is_valid_piece(origin_piece_name)
    #     except Emptysquare as es:
    #         print(f"Location {origin}:[{ori_x},{ori_y}] {es.message}")            
    #     else:
    #         dest_coords = squares[destiny]
    #         remove_piece(ori_coords)
    #         put_piece(origin_piece_name, dest_coords)


    def get_board(self):
        """

        """
        return self.board



