from random import sample

def create_board(Cell, rows=9, columns=9):
    """ Creates and returns a Minesweeper board filled with Cell objects."""
    board = []

    # Loops through each row and fills it with cells
    for y in range(rows): 
        row = []
        for x in range(columns):
            new_cell = Cell()
            row.append(new_cell)
        board.append(row)    
    
    return board

def mine_placement(board, row, column, mine_count=10):
    """ Randomly selects unique board positions and marks those cells as mines."""
    rows = len(board)
    columns = len(board[0])
    positions = []

    # Loops through every (x,y) index on the board and appends to positions
    for x in range(rows):
        for y in range(columns):
            single_position = (x,y)

            # Skip the player's first selected cell so it cannot contain a mine
            if single_position == (row, column):
                continue
            
            positions.append(single_position)

    # Randomly samples positions to be mines
    mine_positions = sample(positions, mine_count)

    # Edit attributes of cells containing mines
    for mine in mine_positions:
        mine_row, mine_column = mine
        board[mine_row][mine_column].mine = True

    return board

def calculate_touching_mines(board):
    """ Calculates and stores the number of adjacent mines for each non-mine cell."""
    rows = len(board)
    columns = len(board[0])

    # Possible 8 neighboring cells
    offsets = [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,-1), (1, 1)]

    for x in range(rows):
        for y in range(columns):

            current_cell = board[x][y]

            if current_cell.mine:
                continue
            
            for row_offset, column_offset in offsets:
                # Calculate the neighboring cell's row and column
                neighbor_row = x + row_offset
                neighbor_column = y + column_offset

                # Make sure the neighboring position is inside the board
                if (neighbor_row >= 0) and (neighbor_row <= rows - 1):
                    if (neighbor_column >= 0) and (neighbor_column <= columns - 1):

                        # Increase the count if the valid neighboring cell contains a mine
                        if board[neighbor_row][neighbor_column].mine:
                            current_cell.touching += 1

    return board
                       



            
                