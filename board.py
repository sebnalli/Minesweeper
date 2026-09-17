from random import sample

def create_board(Cell):
    """
    Creates and returns a 9 x 9 Minesweeper board filled with Cell objects.
    """
    board = []

    # Loops through each rows and inserts 9 cells and appends it to board
    for y in range(9): 
        row = []
        for x in range(9):
            new_cell = Cell()
            row.append(new_cell)
        board.append(row)    
    
    return board

def mine_placement(board):
    """
    Randomly selects 10 unique board positions and marks those cells as mines.
    """
    rows = len(board)
    columns = len(board[0])
    positions = []

    # Loops through every (x,y) index on the board and appends to positions
    for x in range(rows):
        for y in range(columns):
            single_position = (x,y)
            positions.append(single_position)

    # Randomly samples 10 positions to be mines
    mine_positions = sample(positions, 10)

    # Edit attributes of cells containing mines
    for mine in mine_positions:
        row, column = mine
        board[row][column].mine = True

    return board

def calculate_touching_mines(board):
    rows = len(board)
    columns = len(board[0])

    offsets = [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (-1,1), (1,-1), (1, 1)]

    for x in range(rows):
        for y in range(columns):

            current_cell = board[x][y]

            if current_cell.mine:
                continue
            
            for row_offset, column_offset in offsets:
                neighbor_row = x + row_offset
                neighbor_column = y + column_offset

                if (neighbor_row >= 0) and (neighbor_row <= rows - 1):
                    if (neighbor_column >= 0) and (neighbor_column <= columns - 1):
                        if board[neighbor_row][neighbor_column].mine:
                            current_cell.touching += 1

    return board
                       



            
                