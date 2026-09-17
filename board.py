from cell import Cell

def create_board():
    board = []

    for y in range(9):
        row = []
        for x in range(9):
            new_cell = Cell()
            row.append(new_cell)
        board.append(row)    
    
    print(board)
    return board

create_board()
