import pygame
init.pygame()
class power_ups:
    
    padding = 13
    outline = 3

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()


    def calc_pos(self):
        self.x = SQUARE_SIZE * col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * row + SQUARE_SIZE // 2
    
    def execute(self):
        if color == red:
            def shield(self):
                pass
        elif color == blue:   
            def rand_elim(self):
                pass
        else:
            def temp_king(self):
                pass

