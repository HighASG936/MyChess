
class Movements:

    def __init__(self):
        super().__init__()
        
    
    def get_movs_king(self, locate):
        possible_movs = []
        x, y = locate
        possible_movs.append(locate)
        possible_movs.append([x, y+1])

        return possible_movs
    
