
from Chess import start_positions, new_board, get_list_squares_board


class Chess:

    def __init__(self):
        self.board = new_board()
    
    def draw_board(self):
        rows = [str(self.board[x]) + '\n' for x in range(0, len(self.board))]
        
        #print A, B, C, D... labels
        labels = get_list_squares_board()
        format_label = "{:>7}" * (len(labels) + 1)
        print(format_label.format("   ", *labels))
        
        #Print board
        for row in rows:
            format_row = "{:^2}" * (len(row) + 1)            
            print(f"{rows.index(row)}{format_row.format('', *row)}")