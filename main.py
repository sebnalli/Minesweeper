from cell import Cell
from board import create_board, mine_placement, calculate_touching_mines
from game import *


def start_game():
    
    board = create_board(Cell)
    display_board(board)

    while True:
        row, column = get_player_move()
        mine_placement(board, row, column)