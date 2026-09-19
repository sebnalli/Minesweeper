from cell import Cell
from board import create_board, mine_placement, calculate_touching_mines
from game import *
import time


def start_game():
    """Runs a complete game of Minesweeper from setup until the player wins or loses."""
    
    # Create and Display Board
    board = create_board(Cell)
    print()
    display_board(board)

    # Receieve first move, place mines while handeling first-click case
    row, column = get_player_move()
    start_time = time.time()
    mine_placement(board, row, column)

    # Assign touching mine numbers to tiles
    calculate_touching_mines(board)
    reveal_cell(board, row, column)

    # Cascade effect on tiles not touching mines
    current_cell = board[row][column]
    if current_cell.touching == 0:
        reveal_empty_area(board, row, column)

    # Handles rare case of one move victory
    if check_win(board):
        handle_win(board, start_time)
        return

    while True:

        elapsed_time = int(time.time() - start_time)

        print()
        display_board(board)

        # Displays mine and time total
        mine_total = get_mine_count(board)
        print(f"Mines: {mine_total}")
        print(f"Time: {elapsed_time}")

        row, column = get_player_move()
        action = get_turn_action()

        if action == 'R':

            current_cell = board[row][column]

            result = reveal_cell(board, row, column)
            
            if result is None:
                continue

            if check_mine_hit(board, row, column):
                handle_loss(board, start_time)
                break

            else:
                if current_cell.touching == 0:
                    reveal_empty_area(board, row, column)

                if check_win(board):
                    handle_win(board, start_time)
                    break

        else:
            toggle_flag(board, row, column)

def main():
    while True:

        start_game()

        while True:
            play_again = input("\nWould you like to play again? (Y|N)\n").strip().upper()

            if play_again == 'Y':
                break

            elif play_again == 'N':
                    print("Thank you for playing!")
                    return
            else:
                print("Please enter Y or N.")
                continue

if __name__ == "__main__":
    main()