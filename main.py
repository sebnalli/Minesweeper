from cell import Cell
from board import create_board, mine_placement, calculate_touching_mines
from game import *
import time


def start_game():
    
    # Create and Display Board
    board = create_board(Cell)
    display_board(board)

    # Receieve first move, place mines while handeling first-click case
    row, column = get_player_move()
    start_time = time.time()
    mine_placement(board, row, column)

    calculate_touching_mines(board)
    reveal_cell(board, row, column)

    current_cell = board[row][column]
    if current_cell.touching == 0:
        reveal_empty_area(board, row, column)

    while True:

        elapsed_time = int(time.time() - start_time)

        display_board(board)

        mine_total = get_mine_count(board)
        print(f"Mines: {mine_total}")
        print(f"Time: {elapsed_time}")

        row, column = get_player_move()
        action = get_turn_action()

        if action == 'R':
            reveal_cell(board, row, column)
            current_cell = board[row][column]

            if check_mine_hit(board, row, column):
                pass

            else:
                if current_cell.touching == 0:
                    reveal_empty_area(board, row, column)

                if check_win(board):
                    pass

        else:
            toggle_flag(board, row, column)






