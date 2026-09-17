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