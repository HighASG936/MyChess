
class Settings:

    def __init__(self):

        self.padding = 100

        #Cell settings
        self.cell_long = 100
        self.black_cell_color = (10, 10, 10)
        self.white_cell_color = (100, 100, 100)

        # Board settings
        self.board_long = self.cell_long * 8

        #Screen settings
        self.screen_width = self.board_long + self.padding
        self.screen_height = self.board_long + 100 + self.padding
        self.bg_color = (150, 150, 150)

