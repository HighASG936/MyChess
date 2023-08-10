
start_positions = { 'WR': ["A1", "H1"],  # White Rooks
                    'BR': ["A8", "H8"],  # Black Rooks
                    'WH': ["B1", "G1"],  # White Knights
                    'BH': ["B8", "G8"],  # Black Knights
                    'WB': ["C1", "F1"],  # White Bishops
                    'BB': ["C8", "F8"],  # Black Bishops
                    'WQ': ["D1"],        # White Queen
                    'BQ': ["D8"],        # Black Queen
                    'WK': ["E1"],        # White King
                    'BK': ["E8"],        # Black King
                    'WP': ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],  # White Pawns
                    'BP': ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],  # Black Pawns
                }

board = []
index_x = 1
index_y = 0
squares = None

def get_list_squares_board():
    """
    
    """
    return [chr(x) for x in range(ord('A'), ord('I'))]

def get_squares_coordinates():
    """

    """
    squares = {}
    letters = get_list_squares_board()
    
    for x in letters:
        for y in range(1, len(board) +1):
            key = f"{x}{y}"
            squares[key] = [letters.index(x) +1, y -1]        
    return squares

def put_piece(piece, coord):
    """_summary_

    Args:
        piece (_type_): _description_
        coord (_type_): _description_
    """
    x, y = coord[index_x], coord[index_y] -1
    board[x][y] = piece
        
def new_board():        
    """_summary_
    """    
    squares = get_squares_coordinates()    
    #Create matriz to chess board
    for row in range(0, 8):
        board.append([])
        for _ in range(0,8):
            board[row].append('--')    
    
    #Put the set chess on board
    for key, value in start_positions.items():
        for pos in value:
            put_piece(str(key), squares[pos])
    return board
