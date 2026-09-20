import pygame
from src.core.cell import Cell
from src.core.board import create_board, mine_placement, calculate_touching_mines
from src.core.game import reveal_cell, reveal_empty_area, toggle_flag

pygame.init()

# Board and tile dimensions
TILE_SIZE = 70
BOARD_SIZE = 9

# Flag and mine size
FLAG_SIZE = 50
MINE_SIZE = 60

WIDTH = TILE_SIZE * BOARD_SIZE
HEIGHT = TILE_SIZE * BOARD_SIZE

# Open window display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Load Assets
# Hidden Tile 
hidden_tile = pygame.image.load("src/gui/assets/hidden_tile.png").convert_alpha()

# Revealed light tile
revealed_light = pygame.image.load(
    "src/gui/assets/revealed_tile_light.png"
).convert_alpha()

# Revealed dark tile
revealed_dark = pygame.image.load(
    "src/gui/assets/revealed_tile_dark.png"
).convert_alpha()

# Mine
mine_image = pygame.image.load(
    "src/gui/assets/mine.png"
).convert_alpha()

# Touching mine number
number_font = pygame.font.Font(
    "src/gui/assets/pixel_font.ttf",
    28
)

# Flag
flag_image = pygame.image.load(
    "src/gui/assets/flag.png"
).convert_alpha()

# Corresponding colors to numbers
NUMBER_COLORS = {
    1: (0, 0, 255),
    2: (0, 128, 0),
    3: (255, 0, 0),
    4: (0, 0, 128),
    5: (128, 0, 0),
    6: (0, 128, 128),
    7: (0, 0, 0),
    8: (128, 128, 128),
}

# Scale assets to match tile size
hidden_tile = pygame.transform.scale(hidden_tile, (TILE_SIZE, TILE_SIZE))
revealed_light = pygame.transform.scale(revealed_light, (TILE_SIZE, TILE_SIZE))
revealed_dark = pygame.transform.scale(revealed_dark, (TILE_SIZE, TILE_SIZE))
mine_image = pygame.transform.scale(mine_image, (MINE_SIZE, MINE_SIZE))
flag_image = pygame.transform.scale(flag_image, (FLAG_SIZE, FLAG_SIZE))
# Create board
board = create_board(Cell)

first_click = True

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos

            # Convert the mouse position into a board row and column
            column = mouse_x // TILE_SIZE
            row = mouse_y // TILE_SIZE

            # Handles first-click safety, places mines, and assigns touching-mine counts
            if first_click:
                mine_placement(board, row, column)
                calculate_touching_mines(board)
                first_click = False

            # Reveal the tile
            reveal_cell(board, row, column)

            # cascades tiles not touching mines
            if not board[row][column].mine and board[row][column].touching == 0:
                reveal_empty_area(board, row, column)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_x, mouse_y = event.pos

            # Convert the mouse position into a board row and column
            column = mouse_x // TILE_SIZE
            row = mouse_y // TILE_SIZE

            # Flag or unflag the tile
            toggle_flag(board, row, column)

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):

            # Calculate tile position
            x = column * TILE_SIZE
            y = row * TILE_SIZE

            current_cell = board[row][column]

            # If the current cell is revealed, display revealed tile
            if current_cell.revealed:
                
                # Checkerboards the revealed tile assets
                if (row + column) % 2 == 0:
                    screen.blit(revealed_light, (x, y))
                else:
                    screen.blit(revealed_dark, (x, y))

                # Display mine if touched
                if current_cell.mine:
                    mine_x = x + (TILE_SIZE - MINE_SIZE) // 2
                    mine_y = y + (TILE_SIZE - MINE_SIZE) // 2

                    screen.blit(mine_image, (mine_x, mine_y))
                
                # Displays touching mine count
                elif current_cell.touching > 0:
                    # Render the touching-mine number as a drawable image
                    number_surface = number_font.render(
                        str(current_cell.touching),
                        False,
                        NUMBER_COLORS[current_cell.touching]
                    )

                    # Center the number inside the current tile
                    number_rect = number_surface.get_rect(
                        center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2)
                    )

                    # Draw the number on top of the revealed tile
                    screen.blit(number_surface, number_rect)

            # Otherwise display a hidden tile
            else:
                screen.blit(hidden_tile, (x, y))

                # Draw flag on top of hidden tile
                if current_cell.flagged:
                    flag_x = x + (TILE_SIZE - FLAG_SIZE) // 2
                    flag_y = y + (TILE_SIZE - FLAG_SIZE) // 2

                    screen.blit(flag_image, (flag_x, flag_y))


    pygame.display.flip()

pygame.quit()