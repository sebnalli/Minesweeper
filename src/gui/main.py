import pygame
from src.core.cell import Cell
from src.core.board import create_board

pygame.init()

# Board and tile dimensions
TILE_SIZE = 40
BOARD_SIZE = 9

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

# Scale assets to match tile size
hidden_tile = pygame.transform.scale(hidden_tile, (TILE_SIZE, TILE_SIZE))
revealed_light = pygame.transform.scale(revealed_light, (TILE_SIZE, TILE_SIZE))
revealed_dark = pygame.transform.scale(revealed_dark, (TILE_SIZE, TILE_SIZE))

# Create board
board = create_board(Cell)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

            # Otherwise display a hidden tile
            else:
                screen.blit(hidden_tile, (x, y))

    pygame.display.flip()

pygame.quit()