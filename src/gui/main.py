import pygame

pygame.init()

# Board and tile dimensions
TILE_SIZE = 40
BOARD_SIZE = 9

WIDTH = TILE_SIZE * BOARD_SIZE
HEIGHT = TILE_SIZE * BOARD_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            
            # For each tile, calculate its pixel position
            x = column * TILE_SIZE
            y = row * TILE_SIZE

            # Create rectangle and its border
            pygame.draw.rect(screen, (180, 180, 180), (x, y, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), (x, y, TILE_SIZE, TILE_SIZE), 1)

            pygame.display.flip()

pygame.quit()