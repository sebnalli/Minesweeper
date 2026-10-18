import json
from pathlib import Path
import os
import sys

def get_highscore_path():
    """Returns the path used to store high scores."""

    # Use the macOS application support folder
    if sys.platform == "darwin":
        data_folder = Path.home() / "Library" / "Application Support" / "Minesweeper"

    # Use the Windows AppData folder
    elif sys.platform == "win32":
        data_folder = Path(os.environ["APPDATA"]) / "Minesweeper"

    # Use the standard Linux user data folder
    else:
        data_folder = Path.home() / ".local" / "share" / "Minesweeper"

    # Create the folder if it does not exist
    data_folder.mkdir(parents=True, exist_ok=True)

    return data_folder / "highscores.json"

def load_highscores():
    """Loads the saved high scores from the JSON file."""
    path = get_highscore_path()

    if path.exists():
        contents = path.read_text()
        highscores = json.loads(contents)
        return highscores

    highscores = {
        "beginner": None,
        "intermediate": None,
        "expert": None
    }

    return highscores

def save_highscores(highscores):
    """Saves the high scores to the JSON file."""

    path = get_highscore_path()
    contents = json.dumps(highscores, indent=4)
    
    path.write_text(contents)

def update_highscore(difficulty, new_time):
    """Updates the saved high score if the new time is better."""
    highscores = load_highscores()

    current_best = highscores[difficulty]

    if current_best is None or new_time < current_best:
        highscores[difficulty] = new_time
        save_highscores(highscores)