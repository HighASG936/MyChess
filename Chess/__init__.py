


class Emptysquare(Exception):
    def __init__(self, message):
        self.message = message        
    
    
# def new_board():        
#     """_summary_
#     """    
    
#     #Create matriz to chess board
#     for row in range(0, 8):
#         board.append([])
#         for _ in range(0,8):
#             board[row].append('--')  
    
#     squares = _get_squares_coordinates()
    
#     #Put the set chess on board
#     for key, value in start_positions.items():
#         for pos in value:
#             _put_piece(str(key), squares[pos])


# def is_valid_piece(piece_name):
#     if piece_name == '--':
#         raise Emptysquare("is empty")




