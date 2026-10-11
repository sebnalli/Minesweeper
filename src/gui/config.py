# Board dimensions
TILE_SIZE = 60
BOARD_ROWS = 9
BOARD_COLUMNS = 9

# Mine count constant
MINE_COUNT = 10

# Difficulty settings
DIFFICULTIES = {
    "beginner": (9, 9, 10, 60),
    "intermediate": (16, 16, 40, 40),
    "expert": (16, 30, 99, 42)
}

BOARD_WIDTH = TILE_SIZE * BOARD_COLUMNS
BOARD_HEIGHT = TILE_SIZE * BOARD_ROWS

# Asset sizes
FLAG_SIZE = 40
MINE_SIZE = 50
SMILEY_SIZE = 65
SMILEY_BOX_SIZE = 70
HOME_SIZE = 30

# Outer UI layout
OUTER_MARGIN = 16
TOP_PANEL_HEIGHT = 100
BOARD_FRAME_PADDING = 10

# Counter displays
COUNTER_WIDTH = 90
COUNTER_HEIGHT = 50

# Position the counter inside the top-left panel area
COUNTER_X = OUTER_MARGIN + 20
COUNTER_Y = OUTER_MARGIN + (TOP_PANEL_HEIGHT - COUNTER_HEIGHT) // 2

# Counter colors
COUNTER_BACKGROUND = (50, 35, 40)
COUNTER_TEXT_COLOR = (255, 70, 140)

# Position of the board inside the window
BOARD_X = OUTER_MARGIN + BOARD_FRAME_PADDING
BOARD_Y = OUTER_MARGIN + TOP_PANEL_HEIGHT + BOARD_FRAME_PADDING

WIDTH = BOARD_WIDTH + (OUTER_MARGIN * 2) + (BOARD_FRAME_PADDING * 2)
HEIGHT = (
    BOARD_HEIGHT
    + TOP_PANEL_HEIGHT
    + (OUTER_MARGIN * 2)
    + (BOARD_FRAME_PADDING * 2)
)

# Position the smiley box in the center of the top panel
SMILEY_BOX_X = (WIDTH - SMILEY_BOX_SIZE) // 2
SMILEY_BOX_Y = OUTER_MARGIN + (TOP_PANEL_HEIGHT - SMILEY_BOX_SIZE) // 2

# Position the home button beside the smiley
HOME_X = SMILEY_BOX_X + SMILEY_BOX_SIZE + 12
HOME_Y = SMILEY_BOX_Y + (SMILEY_BOX_SIZE - HOME_SIZE) // 2

# Position the timer inside the top-right panel area
TIMER_X = WIDTH - OUTER_MARGIN - 20 - COUNTER_WIDTH
TIMER_Y = COUNTER_Y

# Colors
BACKGROUND_COLOR = (190, 170, 175)

# Number colors
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

# Difficulty button colors
BEGINNER_COLOR = (80, 160, 90)
INTERMEDIATE_COLOR = (220, 150, 60)
EXPERT_COLOR = (190, 70, 70)
