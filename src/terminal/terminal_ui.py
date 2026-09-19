import time
from src.core.game import *

def display_board(board, game_over=False):
    """
    Displays the Minesweeper board in the terminal with row and column labels.

    Each cell is shown based on whether it is flagged, hidden, revealed, or a mine.
    """
    rows = len(board)
    columns = len(board[0])

    # Print column headers 
    print("  " + " ".join(chr(65 + i) for i in range(columns)))

    # Print row label
    for x in range(rows):

        print(x + 1, end=" ")

        for y in range(columns):

            # Display each cell based on whether it is flagged, hidden, revealed, or a mine
            if game_over and board[x][y].mine and board[x][y].revealed:
                print("*", end=" ")

            elif board[x][y].flagged:
                print("F", end=" ")

            elif not board[x][y].revealed:
                print("#", end=" ")

            elif not board[x][y].mine:
                if board[x][y].touching:
                    print(f"{board[x][y].touching}", end=" ")
                else:
                    print(" ", end=" ")

            else:
                print("*", end=" ")

        print()

def get_player_move():
    """
    Prompts the player for a valid Minesweeper coordinate.

    Converts the entered coordinate into zero-based row and column indexes
    and returns them as a tuple.
    """
    while True:
        coordinate = input("\nPlease input a valid coordinate: ").strip()

        if len(coordinate) == 2 and coordinate[0].isalpha() and coordinate[1].isdigit():
           
            column_letter = coordinate[0].upper()
            row_number = int(coordinate[1])

            if "A" <= column_letter <= "I" and 1 <= row_number <= 9:
                # Convert the user-facing row number to a zero-based board index
                row = row_number - 1
                # Convert column letters A-I into zero-based indexes 0-8
                column = ord(column_letter) - ord("A") 

                return row, column

            else:
                print("Coordinate is out of range.")
                continue

        else:
            print("Invalid coordinate format.")
            continue 

def get_turn_action():
    """
    Prompts the player to choose whether to reveal or flag a cell.

    Returns either 'R' for reveal or 'F' for flag.
    """
    while True:
        action = input("Reveal or Flag (R/F)").strip().upper()
        if action != 'R' and action != 'F': continue
        return action
    
def handle_loss(board, start_time):
    """Handles the end of the game after the player reveals a mine."""
    final_time = int(time.time() - start_time)

    reveal_all_mines(board)
    display_board(board, True)

    print("\nGame Over! Nice Try.\n")
    print(f"Final Time: {final_time} seconds")

    return False
    
def handle_win(board, start_time):
    """Handles the end of the game after all safe cells have been revealed."""
    final_time = int(time.time() - start_time)
    display_board(board)
    print("\nCongratulations! You Win!\n")
    print(f"Final Time: {final_time} seconds")

    return False