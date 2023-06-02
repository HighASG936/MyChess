
import pygame
from board import Board
from settings import Settings
from chess_set import ChessSet
class Chess:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.chess_set = ChessSet(self)
        self.screen = pygame.display.set_mode((self.settings.screen_height,
                                               self.settings.screen_width)
                                              )
        pygame.display.set_caption("Chess")
        self.board = Board(self)


    def draw_set(self):
        #Draw black king
        king = self.chess_set.pieces[0]
        king.x, king.y =  self.board.board_rect.x * 4, self.board.board_rect.y
        king.blitme()

        #Draw black queen
        queen = self.chess_set.pieces[1]
        queen.x, queen.y =  self.board.board_rect.x * 5, self.board.board_rect.y
        queen.blitme()

        # Draw black rooks, knights and bishops
        for piece_index in range(2,5):
            piece = self.chess_set.pieces[piece_index]
            piece.y = self.board.board_rect.y

            #Draw left pieces
            x_offset = piece_index - 1
            piece.x =  self.board.board_rect.x * x_offset
            piece.blitme()

            #Draw right pieces
            piece = self.chess_set.pieces[6-piece_index]
            x_offset = piece_index + 4
            piece.x =  self.board.board_rect.x * x_offset
            piece.blitme()

        # Draw a row of black pawns.
        pawn = self.chess_set.pieces[5]
        pawn.y = self.board.board_rect.y + self.settings.cell_long
        for column in range(1, 9):
            pawn.x = self.board.board_rect.x * column
            pawn.blitme()


        # Draw a row of white pawns.
        pawn = self.chess_set.pieces[11]
        pawn.y = self.settings.board_long - (1.5 * self.settings.cell_long)
        for column in range(1, 9):
            pawn.x = self.board.board_rect.x * column
            pawn.blitme()

        #Draw black king
        king = self.chess_set.pieces[6]
        king.x, king.y =  self.board.board_rect.x * 4, self.settings.board_long - (0.5 * self.settings.cell_long)
        king.blitme()

        #Draw black queen
        queen = self.chess_set.pieces[7]
        queen.x, queen.y =  self.board.board_rect.x * 5, self.settings.board_long - (0.5 * self.settings.cell_long)
        queen.blitme()

        # Draw black rooks, knights and bishops
        for piece_index in range(8,11):
            piece = self.chess_set.pieces[piece_index]

            piece.y = self.settings.board_long - (0.5 * self.settings.cell_long)

            #Draw left pieces
            x_offset = piece_index - 7
            piece.x =  self.board.board_rect.x * x_offset
            piece.blitme()

            #Draw right pieces
            piece = self.chess_set.pieces[18-piece_index]
            x_offset = piece_index -2
            piece.x =  self.board.board_rect.x * x_offset
            piece.blitme()


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.board.draw_board()
        #self.draw_set()
        pygame.display.flip()

    def _check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        while True:
            self._check_events()
            self._update_screen()

if __name__ == '__main__' :
    ch = Chess()
    ch.run()
