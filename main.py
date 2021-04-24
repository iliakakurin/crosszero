from random import randint
import pygame as pg
import sys

W = 600
H = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CARS = ('car1.png', 'car2.png', 'car3.png')

cross = pg.image.load(CARS[0])
zero = pg.image.load(CARS[1])
turn = 1
pressed = False
board = []

for i in range(3):
    board.append([0]*3)


def draw_grid():
    pg.draw.line(sc, BLACK, (0, 200), (600, 200))
    pg.draw.line(sc, BLACK, (0, 400), (600, 400))
    pg.draw.line(sc, BLACK, (200, 0), (200, 600))
    pg.draw.line(sc, BLACK, (400, 0), (400, 600))


def draw_board(board):
    # отобразить крестики и нолики на экране
    for i in range(0, 3):
        for j in range(0, 3):
            # поставить элемент в клетку (i, j)
            pass

def check_win(board):
    # если выиграл 1 - вернуть 1
    # если выиграл 2 - вернуть 2
    # если ничья - вернуть 3
    # если игра продолжается - вернуть 0
    pass


sc = pg.display.set_mode((W, H))

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.MOUSEBUTTONDOWN:
            p = i.pos
            pressed = True


    sc.fill(WHITE)

    draw_grid()
    if pressed:
        pressed = False
        x = p[0] // 200
        y = p[1] // 200
        board[y][x] = turn
        for row in board:
            print(row)
        print('---------')
        if turn == 1:
            turn = 2
        else:
            turn = 1

    draw_board(board)

    if check_win(board):
        print(check_win(board))
        pg.quit()
        sys.exit()

    pg.display.update()
    pg.time.delay(20)
