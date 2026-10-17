import pygame
from src.core.cell import Cell
from src.core.board import create_board, mine_placement, calculate_touching_mines
from src.gui.highscores import update_highscore, load_highscores
from src.gui.config import *
from src.gui.ui import (
    draw_raised_panel,
    draw_sunken_panel,
    draw_counter_box,
    draw_menu
)
from src.core.game import (
    reveal_cell,
    reveal_empty_area,
    toggle_flag,
    check_mine_hit,
    reveal_all_mines,
    check_win,
    get_mine_count
)

def apply_difficulty(difficulty):
    # Load the board settings for the selected difficulty
    BOARD_ROWS, BOARD_COLUMNS, MINE_COUNT, TILE_SIZE = DIFFICULTIES[difficulty]

    # Recalculate board size for the selected difficulty
    BOARD_WIDTH = TILE_SIZE * BOARD_COLUMNS
    BOARD_HEIGHT = TILE_SIZE * BOARD_ROWS

    # Recalculate window size to fit the new board
    WIDTH = BOARD_WIDTH + (OUTER_MARGIN * 2) + (BOARD_FRAME_PADDING * 2)
    HEIGHT = (
        BOARD_HEIGHT
        + TOP_PANEL_HEIGHT
        + (OUTER_MARGIN * 2)
        + (BOARD_FRAME_PADDING * 2)
    )

    # Reposition the top panel controls for the new window width
    SMILEY_BOX_X = (WIDTH - SMILEY_BOX_SIZE) // 2
    TIMER_X = WIDTH - OUTER_MARGIN - 20 - COUNTER_WIDTH

    # Reposition the home button beside the smiley
    HOME_X = SMILEY_BOX_X + SMILEY_BOX_SIZE + 12
    HOME_Y = SMILEY_BOX_Y + (SMILEY_BOX_SIZE - HOME_SIZE) // 2

    return (
    BOARD_ROWS,
    BOARD_COLUMNS,
    MINE_COUNT,
    TILE_SIZE,
    BOARD_WIDTH,
    BOARD_HEIGHT,
    WIDTH,
    HEIGHT,
    SMILEY_BOX_X,
    TIMER_X,
    HOME_X,
    HOME_Y
)

def reset_game_state():
    """Returns the default GUI game state."""
    return (
        True,   # first_click
        False,  # game_over
        False,  # lost
        False,  # won
        False,  # timer_started
        0,      # start_ticks
        0       # elapsed_seconds
    )


pygame.init()

# Open window display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Load Assets
# Hidden Tile 
hidden_tile_original = pygame.image.load(
    "src/gui/assets/hidden_tile.png"
).convert_alpha()

# Revealed light tile
revealed_light_original = pygame.image.load(
    "src/gui/assets/revealed_tile_light.png"
).convert_alpha()

# Revealed dark tile
revealed_dark_original = pygame.image.load(
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

# Difficulty menu text
menu_font = pygame.font.Font(
    "src/gui/assets/pixel_font.ttf",
    18
)

# Mine counter number
counter_font = pygame.font.Font(
    "src/gui/assets/pixel_font.ttf",
    22
)

# Overlay instruction text on game over/game won
overlay_small_font = pygame.font.Font(
    "src/gui/assets/pixel_font.ttf",
    12
)

# Flag
flag_image = pygame.image.load(
    "src/gui/assets/flag.png"
).convert_alpha()

# Standard smiley state
smiley_normal = pygame.image.load(
    "src/gui/assets/smiley.png"
).convert_alpha()

# Smiley loss state
smiley_loss = pygame.image.load(
    "src/gui/assets/smiley_loss.png"
).convert_alpha()

# Smiley win state
smiley_win = pygame.image.load(
    "src/gui/assets/smiley_win.png"
).convert_alpha()

# Home button
home_image = pygame.image.load(
    "src/gui/assets/home.png"
).convert_alpha()


# Scale assets to match tile size
hidden_tile = pygame.transform.scale(hidden_tile_original,(TILE_SIZE, TILE_SIZE))
revealed_light = pygame.transform.scale(revealed_light_original,(TILE_SIZE, TILE_SIZE))
revealed_dark = pygame.transform.scale(revealed_dark_original,(TILE_SIZE, TILE_SIZE))
mine_image = pygame.transform.scale(mine_image, (MINE_SIZE, MINE_SIZE))
flag_image = pygame.transform.scale(flag_image, (FLAG_SIZE, FLAG_SIZE))
smiley_normal = pygame.transform.scale(smiley_normal, (SMILEY_SIZE, SMILEY_SIZE))
smiley_loss = pygame.transform.scale(smiley_loss, (SMILEY_SIZE, SMILEY_SIZE))
smiley_win = pygame.transform.scale(smiley_win, (SMILEY_SIZE, SMILEY_SIZE))
home_image = pygame.transform.scale(home_image, (HOME_SIZE, HOME_SIZE))


# Set starting difficulty
current_difficulty = "beginner"

# Create board
board = create_board(Cell, BOARD_ROWS, BOARD_COLUMNS)

# Set starting game state
(
    first_click,
    game_over,
    lost,
    won,
    timer_started,
    start_ticks,
    elapsed_seconds
) = reset_game_state()

current_screen = "game"
running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Check for back button click
        if (
            current_screen == "menu"
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
        ):
            mouse_x, mouse_y = event.pos

            if (
                BACK_BUTTON_X <= mouse_x < BACK_BUTTON_X + BACK_BUTTON_WIDTH
                and BACK_BUTTON_Y <= mouse_y < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT
            ):
                current_screen = "game"
                continue

        # Check for difficulty button clicks on the menu
        if (
            current_screen == "menu"
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
        ):
            mouse_x, mouse_y = event.pos

            if (
                button_x <= mouse_x < button_x + button_width
                and beginner_y <= mouse_y < beginner_y + button_height
            ):
                current_difficulty = "beginner"

            elif (
                button_x <= mouse_x < button_x + button_width
                and intermediate_y <= mouse_y < intermediate_y + button_height
            ):
                current_difficulty = "intermediate"

            elif (
                button_x <= mouse_x < button_x + button_width
                and expert_y <= mouse_y < expert_y + button_height
            ):
                current_difficulty = "expert"
            else:
                continue
            

            (
                BOARD_ROWS,
                BOARD_COLUMNS,
                MINE_COUNT,
                TILE_SIZE,
                BOARD_WIDTH,
                BOARD_HEIGHT,
                WIDTH,
                HEIGHT,
                SMILEY_BOX_X,
                TIMER_X,
                HOME_X,
                HOME_Y
            ) = apply_difficulty(current_difficulty)

            # Resize the window for the selected difficulty
            screen = pygame.display.set_mode((WIDTH, HEIGHT))

            # Create a fresh board using the selected difficulty
            board = create_board(Cell, BOARD_ROWS, BOARD_COLUMNS)

            # Reset game state for the new difficulty
            (
            first_click,
            game_over,
            lost,
            won,
            timer_started,
            start_ticks,
            elapsed_seconds
            ) = reset_game_state()

            # Resize board tile assets for the selected difficulty
            hidden_tile = pygame.transform.scale(hidden_tile_original,(TILE_SIZE, TILE_SIZE))
            revealed_light = pygame.transform.scale(revealed_light_original,(TILE_SIZE, TILE_SIZE))
            revealed_dark = pygame.transform.scale(revealed_dark_original,(TILE_SIZE, TILE_SIZE))

            # Return to the game screen
            current_screen = "game"

            continue

        # Check for home button click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos

            if (
                HOME_X <= mouse_x < HOME_X + HOME_SIZE
                and HOME_Y <= mouse_y < HOME_Y + HOME_SIZE
            ):
                current_screen = "menu"

                highscores = load_highscores()

                # Draw difficulty menu
                (
                    button_x,
                    button_width,
                    button_height,
                    beginner_y,
                    intermediate_y,
                    expert_y
                ) = draw_menu(
                    screen,
                    WIDTH,
                    number_font,
                    menu_font,
                    highscores
                )

                pygame.display.flip()
                continue

        # Check for smiley reset click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos

            if (
                SMILEY_BOX_X <= mouse_x < SMILEY_BOX_X + SMILEY_BOX_SIZE
                and SMILEY_BOX_Y <= mouse_y < SMILEY_BOX_Y + SMILEY_BOX_SIZE
            ):
                # reset game state
                board = create_board(Cell, BOARD_ROWS, BOARD_COLUMNS)

                (
                first_click,
                game_over,
                lost,
                won,
                timer_started,
                start_ticks,
                elapsed_seconds
                ) = reset_game_state()

                # reset loop
                continue

        # Handle board left-clicks only while the game screen is active
        if (
            current_screen == "game"
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and not game_over
        ):
            mouse_x, mouse_y = event.pos

            # Convert the mouse position into a board row and column
            # Ignore clicks outside the board
            if not (
                BOARD_X <= mouse_x < BOARD_X + BOARD_WIDTH
                and BOARD_Y <= mouse_y < BOARD_Y + BOARD_HEIGHT
            ):
                continue

            # Convert screen position into board row and column
            column = (mouse_x - BOARD_X) // TILE_SIZE
            row = (mouse_y - BOARD_Y) // TILE_SIZE
            
            # Handles first-click safety, places mines, and assigns touching-mine counts
            if first_click:
                mine_placement(board, row, column, MINE_COUNT)
                calculate_touching_mines(board)

                # Start the timer on the first revealed tile
                start_ticks = pygame.time.get_ticks()
                timer_started = True

                first_click = False

            # Reveal the tile
            result = reveal_cell(board, row, column)

            # Stop processing the click if the tile could not be revealed
            if result is None:
                continue
            
            # Handle loss if the selected tile contains a mine
            if check_mine_hit(board, row, column):
                reveal_all_mines(board)
                game_over = True
                lost = True

            # cascades tiles not touching mines
            elif not board[row][column].mine and board[row][column].touching == 0:
                reveal_empty_area(board, row, column)
            
            # Check whether all safe tiles have been revealed
            if not game_over and check_win(board):
                game_over = True
                won = True

                # Check for highscore
                update_highscore(current_difficulty, elapsed_seconds)

        # Handle board right-clicks only while the game screen is active
        if (
            current_screen == "game"
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 3
            and not game_over
        ):
            mouse_x, mouse_y = event.pos

            # Convert the mouse position into a board row and column
            # Ignore clicks outside the board
            if not (
                BOARD_X <= mouse_x < BOARD_X + BOARD_WIDTH
                and BOARD_Y <= mouse_y < BOARD_Y + BOARD_HEIGHT
            ):
                continue

            # Convert screen position into board row and column
            column = (mouse_x - BOARD_X) // TILE_SIZE
            row = (mouse_y - BOARD_Y) // TILE_SIZE

            # Flag or unflag the tile
            toggle_flag(board, row, column)

    if current_screen == "menu":
        continue

    # Update timer while the game is active
    if timer_started and not game_over:
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000

    # Keep the timer within the 3-digit display
    elapsed_seconds = min(elapsed_seconds, 999)

    # Fills entire window background
    screen.fill(BACKGROUND_COLOR)

    # Draw top control panel
    draw_raised_panel(
        screen,
        SMILEY_BOX_X,
        SMILEY_BOX_Y,
        SMILEY_BOX_SIZE,
        SMILEY_BOX_SIZE,
        BACKGROUND_COLOR
    )

    # Center the smiley in the top panel
    smiley_x = SMILEY_BOX_X + (SMILEY_BOX_SIZE - SMILEY_SIZE) // 2
    smiley_y = SMILEY_BOX_Y + (SMILEY_BOX_SIZE - SMILEY_SIZE) // 2

    # Draw the correct smiley for the current game state
    if lost:
        screen.blit(smiley_loss, (smiley_x, smiley_y))
    elif won:
        screen.blit(smiley_win, (smiley_x, smiley_y))
    else:
        screen.blit(smiley_normal, (smiley_x, smiley_y))

    # Draw home button beside the smiley
    screen.blit(home_image, (HOME_X, HOME_Y))
    # Draw recessed board frame
    draw_sunken_panel(
        screen,
        BOARD_X - BOARD_FRAME_PADDING,
        BOARD_Y - BOARD_FRAME_PADDING,
        BOARD_WIDTH + (BOARD_FRAME_PADDING * 2),
        BOARD_HEIGHT + (BOARD_FRAME_PADDING * 2),
        BACKGROUND_COLOR
    )

    # Update mine counter
    mine_total = get_mine_count(board, MINE_COUNT)

    # Draw mine counter box
    draw_counter_box(
        screen,
        COUNTER_X,
        COUNTER_Y,
        COUNTER_WIDTH,
        COUNTER_HEIGHT,
        COUNTER_BACKGROUND
    )

    # Render the remaining mine count as a 3-digit number
    counter_surface = counter_font.render(
        f"{mine_total:03}",
        False,
        COUNTER_TEXT_COLOR
    )

    # Create a rectangle for the counter text and center it in the counter box
    counter_rect = counter_surface.get_rect(
        center=(
            COUNTER_X + COUNTER_WIDTH // 2,
            COUNTER_Y + COUNTER_HEIGHT // 2
        )
    )

    # Draw the mine counter number on the screen
    screen.blit(counter_surface, counter_rect)

    # Draw timer box
    draw_counter_box(
        screen,
        TIMER_X,
        TIMER_Y,
        COUNTER_WIDTH,
        COUNTER_HEIGHT,
        COUNTER_BACKGROUND
    )

    # Render timer as a 3-digit number
    timer_surface = counter_font.render(
        f"{elapsed_seconds:03}",
        False,
        COUNTER_TEXT_COLOR
    )

    timer_rect = timer_surface.get_rect(
        center=(
            TIMER_X + COUNTER_WIDTH // 2,
            TIMER_Y + COUNTER_HEIGHT // 2
        )
    )

    screen.blit(timer_surface, timer_rect)

    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):

            # Calculate tile position
            x = BOARD_X + column * TILE_SIZE
            y = BOARD_Y + row * TILE_SIZE   

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

    # Draw win or loss overlay
    if won or lost:
        overlay_surface = pygame.Surface(
            (OVERLAY_WIDTH, OVERLAY_HEIGHT),
            pygame.SRCALPHA
        )

        overlay_surface.fill(OVERLAY_BACKGROUND)

        # Center the overlay on the board
        overlay_x = BOARD_X + (BOARD_WIDTH - OVERLAY_WIDTH) // 2
        overlay_y = BOARD_Y + (BOARD_HEIGHT - OVERLAY_HEIGHT) // 2

        # Draw the transparent overlay on top of the board
        screen.blit(overlay_surface, (overlay_x, overlay_y))

        # Choose the overlay message based on the game result
        if won:
            overlay_message = "YOU WIN!"
        else:
            overlay_message = "GAME OVER"

        # Render the win or loss message
        overlay_text = number_font.render(
            overlay_message,
            False,
            OVERLAY_TEXT_COLOR
        )

        # Center the message inside the overlay
        overlay_text_rect = overlay_text.get_rect(
            center=(
                overlay_x + OVERLAY_WIDTH // 2,
                overlay_y + OVERLAY_HEIGHT // 2
            )
        )

        # Draw the win or loss message on the overlay
        screen.blit(overlay_text, overlay_text_rect)

        # Render restart instructions
        restart_text = overlay_small_font.render(
            "CLICK SMILEY TO RESTART",
            False,
            OVERLAY_TEXT_COLOR
        )
        
        # Center the restart instructions under the main message
        restart_text_rect = restart_text.get_rect(
            center=(
                overlay_x + OVERLAY_WIDTH // 2,
                overlay_y + OVERLAY_HEIGHT // 2 + 35
            )
        )

        # Draw the restart instructions
        screen.blit(restart_text, restart_text_rect)

    pygame.display.flip()

pygame.quit()