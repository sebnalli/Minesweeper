import pygame


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