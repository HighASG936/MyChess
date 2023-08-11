
from Chess.old_Chess import Chess        
from time import sleep
import os

def play_game(ch):
    game = [("E2", "E4"), ("E7", "E5"), ("G1", "F3"), ("B8", "C6"),
            ("F1", "C4"), ("G8", "F6"), ("D2", "D3"), ("E5", "D4"),
            ("C1", "E3"), ("D4", "E3"), ("F3", "D4"), ("F6", "D7"),
            ("E1", "G1"), ("D7", "F8"), ("D1", "E2"), ("C8", "E6"),
            ]
    ch.draw_board()
    for move in game:
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')  
        ch.move_piece(move)
        ch.draw_board()

                
if __name__ == '__main__':
    
    ch = Chess()
    ch.gui.run_gui()
    #play_game(ch)
