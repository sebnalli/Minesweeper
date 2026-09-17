class Cell:
    """
    Represents a single cell on the Minesweeper board.

    Each cell stores whether it contains a mine, whether it has been flagged
    or revealed by the player, and how many mines are adjacent to it.
    """
    def __init__(self, is_mine=False, is_flagged=False, touching_mine=0,is_revealed=False):
        self.mine = is_mine
        self.flagged = is_flagged
        self.touching = touching_mine
        self.revealed = is_revealed