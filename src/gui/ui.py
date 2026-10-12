import pygame
from src.gui.config import (
    BACKGROUND_COLOR,
    BACK_BUTTON_X,
    BACK_BUTTON_Y,
    BACK_BUTTON_WIDTH,
    BACK_BUTTON_HEIGHT,
    COUNTER_BACKGROUND,
    COUNTER_TEXT_COLOR,
    BEGINNER_COLOR,
    INTERMEDIATE_COLOR,
    EXPERT_COLOR
)

def draw_raised_panel(screen, x, y, width, height, fill_color):
    """
    Draws a raised classic-style panel with light top/left edges
    and dark bottom/right edges.
    """

    LIGHT_EDGE = (240, 220, 225)
    DARK_EDGE = (110, 90, 95)
    BORDER_SIZE = 4

    # Panel background
    pygame.draw.rect(
        screen,
        fill_color,
        (x, y, width, height)
    )

    # Top edge
    pygame.draw.rect(
        screen,
        LIGHT_EDGE,
        (x, y, width, BORDER_SIZE)
    )

    # Left edge
    pygame.draw.rect(
        screen,
        LIGHT_EDGE,
        (x, y, BORDER_SIZE, height)
    )

    # Bottom edge
    pygame.draw.rect(
        screen,
        DARK_EDGE,
        (x, y + height - BORDER_SIZE, width, BORDER_SIZE)
    )

    # Right edge
    pygame.draw.rect(
        screen,
        DARK_EDGE,
        (x + width - BORDER_SIZE, y, BORDER_SIZE, height)
    )


def draw_sunken_panel(screen, x, y, width, height, fill_color):
    """
    Draws a sunken classic-style panel with dark top/left edges
    and light bottom/right edges.
    """

    LIGHT_EDGE = (240, 220, 225)
    DARK_EDGE = (110, 90, 95)
    BORDER_SIZE = 4

    # Panel background
    pygame.draw.rect(
        screen,
        fill_color,
        (x, y, width, height)
    )

    # Top edge
    pygame.draw.rect(
        screen,
        DARK_EDGE,
        (x, y, width, BORDER_SIZE)
    )

    # Left edge
    pygame.draw.rect(
        screen,
        DARK_EDGE,
        (x, y, BORDER_SIZE, height)
    )

    # Bottom edge
    pygame.draw.rect(
        screen,
        LIGHT_EDGE,
        (x, y + height - BORDER_SIZE, width, BORDER_SIZE)
    )

    # Right edge
    pygame.draw.rect(
        screen,
        LIGHT_EDGE,
        (x + width - BORDER_SIZE, y, BORDER_SIZE, height)
    )

def draw_counter_box(screen, x, y, width, height, fill_color):
    """
    Draws a recessed box for the mine counter or timer.
    """

    draw_sunken_panel(
        screen,
        x,
        y,
        width,
        height,
        fill_color
    )

def draw_menu(screen, width, number_font, menu_font, highscores):
    """
    Draws the difficulty selection menu.
    """

    # Draw menu background
    screen.fill(BACKGROUND_COLOR)

    # Draw back button
    pygame.draw.rect(
        screen,
        COUNTER_BACKGROUND,
        (BACK_BUTTON_X, BACK_BUTTON_Y, BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT)
    )

    # Render back button text
    back_text = menu_font.render(
        "BACK",
        False,
        COUNTER_TEXT_COLOR
    )

    # Center the back button text
    back_rect = back_text.get_rect(
        center=(
            BACK_BUTTON_X + BACK_BUTTON_WIDTH // 2,
            BACK_BUTTON_Y + BACK_BUTTON_HEIGHT // 2
        )
    )

    # Draw back button text
    screen.blit(back_text, back_rect)

    # Render menu title
    menu_title = number_font.render(
        "MINESWEEPER",
        False,
        COUNTER_TEXT_COLOR
    )

    # Center the menu title
    menu_title_rect = menu_title.get_rect(
        center=(width // 2, 100)
    )

    # Draw menu title
    screen.blit(menu_title, menu_title_rect)

    # Set difficulty button size
    button_width = 220
    button_height = 55

    # Center difficulty buttons
    button_x = (width - button_width) // 2

    beginner_y = 170
    intermediate_y = 270
    expert_y = 370

    # Draw beginner button
    pygame.draw.rect(
        screen,
        BEGINNER_COLOR,
        (button_x, beginner_y, button_width, button_height)
    )

    # Get beginner high score
    beginner_score = highscores["beginner"]

    # Format beginner high score
    if beginner_score is None:
        beginner_best = "BEST: ---"
    else:
        beginner_best = f"BEST: {beginner_score:03}"

    # Render beginner high score
    beginner_best_text = menu_font.render(
        beginner_best,
        False,
        COUNTER_TEXT_COLOR
    )

    # Center beginner high score under the button
    beginner_best_rect = beginner_best_text.get_rect(
        center=(
            button_x + button_width // 2,
            beginner_y + button_height + 18
        )
    )

    # Draw beginner high score
    screen.blit(beginner_best_text, beginner_best_rect)

    # Draw intermediate button
    pygame.draw.rect(
        screen,
        INTERMEDIATE_COLOR,
        (button_x, intermediate_y, button_width, button_height)
    )

    # Get intermediate high score
    intermediate_score = highscores["intermediate"]

    # Format intermediate high score
    if intermediate_score is None:
        intermediate_best = "BEST: ---"
    else:
        intermediate_best = f"BEST: {intermediate_score:03}"

    # Render intermediate high score
    intermediate_best_text = menu_font.render(
        intermediate_best,
        False,
        COUNTER_TEXT_COLOR
    )

    # Center intermediate high score under the button
    intermediate_best_rect = intermediate_best_text.get_rect(
        center=(
            button_x + button_width // 2,
            intermediate_y + button_height + 18
        )
    )

    # Draw intermediate high score
    screen.blit(intermediate_best_text, intermediate_best_rect)

    # Draw expert button
    pygame.draw.rect(
        screen,
        EXPERT_COLOR,
        (button_x, expert_y, button_width, button_height)
    )

    # Get expert high score
    expert_score = highscores["expert"]

    # Format expert high score
    if expert_score is None:
        expert_best = "BEST: ---"
    else:
        expert_best = f"BEST: {expert_score:03}"

    # Render expert high score
    expert_best_text = menu_font.render(
        expert_best,
        False,
        COUNTER_TEXT_COLOR
    )

    # Center expert high score under the button
    expert_best_rect = expert_best_text.get_rect(
        center=(
            button_x + button_width // 2,
            expert_y + button_height + 18
        )
    )

    # Draw expert high score
    screen.blit(expert_best_text, expert_best_rect)


    # Render difficulty button text
    beginner_text = menu_font.render(
        "BEGINNER",
        False,
        (255, 255, 255)
    )

    intermediate_text = menu_font.render(
        "INTERMEDIATE",
        False,
        (255, 255, 255)
    )

    expert_text = menu_font.render(
        "EXPERT",
        False,
        (255, 255, 255)
    )

    # Center difficulty button text
    beginner_rect = beginner_text.get_rect(
        center=(
            button_x + button_width // 2,
            beginner_y + button_height // 2
        )
    )

    intermediate_rect = intermediate_text.get_rect(
        center=(
            button_x + button_width // 2,
            intermediate_y + button_height // 2
        )
    )

    expert_rect = expert_text.get_rect(
        center=(
            button_x + button_width // 2,
            expert_y + button_height // 2
        )
    )

    # Draw difficulty button text
    screen.blit(beginner_text, beginner_rect)
    screen.blit(intermediate_text, intermediate_rect)
    screen.blit(expert_text, expert_rect)

    return (
    button_x,
    button_width,
    button_height,
    beginner_y,
    intermediate_y,
    expert_y
    )