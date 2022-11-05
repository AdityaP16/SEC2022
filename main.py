### main.py

import pygame

CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (44,25))

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 9, 9
SQUARE_SIZE = WIDTH//COLS
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Checkers')

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

class Game:
    def __init__(self,win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
            self._init()

    def select(self,row,col):
        if self.selected:
            result = self._move(row,col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:

            piece = self.board.get_piece(row,col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        
        return False

    def move(self,row,col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
        else:
            return False

        return True

    def change_turn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
         win.fill(BLACK)
         for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col],  self.board[piece.row][piece.col]
        piece.move(row,col)

        if row == ROWS or row == 0: #if row == max or min
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1


    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row,col,WHITE))
                    elif row > 5:
                        self.board[row].append(Piece(row,col,RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
                    
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_piece(self, row, col):
        return self.board[row][col]


class Piece:

    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1
        
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def make_king(self):
        self.king = True

    def draw(self,win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius + self.OUTLINE)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_width()//2))
        
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)

def get_row_and_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE 
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_and_col_from_mouse(pos)
        
        game.update()

    pygame.quit()


main()

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
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def execute(self):
        if self.color == 'red':
            def shield(self):
                pass
        elif self.color == 'blue':   
            def rand_elim(self):
                pass
        elif self.color == 'white':
            def temp_king(self):
                pass

