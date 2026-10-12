import json
from pathlib import Path

def load_highscores():
    """Loads the saved high scores from the JSON file."""
    path = Path("highscores.json")

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

    path = Path("highscores.json")
    contents = json.dumps(highscores, indent=4)
    
    path.write_text(contents)

def update_highscore(difficulty, new_time):
    """Updates the saved high score if the new time is better."""
    highscores = load_highscores()

    current_best = highscores[difficulty]

    if current_best is None or new_time < current_best:
        highscores[difficulty] = new_time
        save_highscores(highscores)