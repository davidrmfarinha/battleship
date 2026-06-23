# Battleship (Python Terminal Game)

Battleship is a Python-based terminal game developed as a personal challenge and built entirely without AI assistance. The project focuses on implementing game logic, terminal-based rendering, and a simple CPU opponent.

---

## Features

- Terminal-based ASCII interface
- Colorized output using `termcolor`
- Sound effects for actions and events
- Random ship placement on a 10x10 grid
- CPU opponent with:
  - Random shooting
  - Basic target-chasing logic after hits
- Turn-based gameplay between human player and CPU

---

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

### Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the game with:

```bash
python battleship.py
# Make sure your terminal window is large enough for proper rendering.
```

---

## Controls
- Arrow keys → move cursor
- Enter / Space → shoot
- Backspace (name input) → delete character

---

## Project Structure
```text
assets/          # Sound files
battleship.py    # Main game file
requirements.txt # Python dependencies
```

---

## Notes
- Developed as a personal challenge without AI assistance
- Designed for terminal play only
- Requires a sufficiently large terminal window for correct display
