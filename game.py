import time

def display_board(board):
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
            if board[x][y].flagged:
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

def reveal_cell(board, row, column):
    """Reveals the selected cell if it is not flagged or already revealed."""
    if board[row][column].flagged:
        print("\nTile is flagged.\n")
        return 
    elif board[row][column].revealed:
       print("\nTile is already revealed.\n")
       return
    else:
       board[row][column].revealed = True
       return board
    
def reveal_empty_area(board, row, column):
    """
    Recursively reveals neighboring cells when the selected cell has no adjacent mines.
    Stops expanding when it reaches numbered, flagged, or already revealed cells.
    """
    current_cell = board[row][column]

    rows = len(board)
    columns = len(board[0])

    if current_cell.touching > 0:
        return
    else:
        offsets = [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,-1), (1, 1)]

        # Calculate the neighboring cell's row and column
        for row_offset, column_offset in offsets:
                neighbor_row = row + row_offset
                neighbor_column = column + column_offset

                # Make sure the neighboring position is inside the board
                if (neighbor_row >= 0) and (neighbor_row <= rows - 1):
                    if (neighbor_column >= 0) and (neighbor_column <= columns - 1):

                        # Check cell conditions: flagged & revealed        
                        if board[neighbor_row][neighbor_column].flagged:
                            continue
                        elif board[neighbor_row][neighbor_column].revealed:
                            continue
                        else:
                            board[neighbor_row][neighbor_column].revealed = True
                            if board[neighbor_row][neighbor_column].touching: 
                                reveal_empty_area(board, neighbor_row, neighbor_column)

def toggle_flag(board, row, column):
    """Toggles the flagged state of the selected cell."""
    current_cell = board[row][column]

    if current_cell.revealed:
        print("\nCannot flag a revealed tile.\n")
        return
    
    if not current_cell.flagged:
        current_cell.flagged = True
    else:
        current_cell.flagged = False

    return board

def check_mine_hit(board, row, column):
    """
    Checks whether the selected cell contains a mine.

    Returns True if the player hit a mine, otherwise returns False.
    """
    current_cell = board[row][column]

    if current_cell.mine:
        return True
    else:
        return False

def check_win(board):
    """
    Checks whether all non-mine cells on the board have been revealed.

    Returns True if the player has won, otherwise returns False.
    """
    rows = len(board)
    columns = len(board[0])

    for x in range(rows):
        for y in range(columns):

            if board[x][y].mine:
                continue

            if not board[x][y].revealed:
                return False
        
    return True

def get_mine_count(board):
    """
    Calculates the number of mines remaining based on the number of placed flags.

    Returns the remaining mine count.
    """
    rows = len(board)
    columns = len(board[0])
    mine_total = 10

    for x in range(rows):
        for y in range(columns):

            if board[x][y].flagged:
                mine_total -= 1

    return mine_total

def reveal_all_mines(board):
    """Reveals all mine cells on the board."""
    rows = len(board)
    columns = len(board[0])

    for x in range(rows):
        for y in range(columns):

            if board[x][y].mine:
                board[x][y].revealed = True

    return board

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
    display_board(board)

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



