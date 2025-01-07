# CheckMate AI

A **Python-based CheckMate AI** offering both **command-line** and **graphical (Pygame)** interfaces. You can **drag and drop** pieces in the GUI, or take turns typing moves in the CLI. Supports **Human vs AI** (Minimax + Alpha-Beta) or **Two-human** mode. All standard  rules are included—check, checkmate, castling, en passant, and promotions.

---

## Features

### Multiple Modes
- **CLI**: Command-line interface with text-based board display.  
- **GUI**: Pygame-based board, similar to .com’s drag-and-drop style.  
- **Human vs. AI** or **Two Humans** (in both CLI or GUI).

### Minimax AI (Alpha-Beta)
- Material-based **Evaluator**.  
- Configurable search depth.  
- Can be extended with advanced heuristics (move ordering, transposition tables, etc.).

### Legal Move Generation
- Separates pseudo-legal from fully legal moves, ensuring no pinned-piece or illegal captures.  
- Automatic **check/checkmate/stalemate** detection.

### Move Highlighting (GUI)
- Shows squares a dragged piece can move to.  
- Rejects drops on illegal squares.

### Piece Images
- Store your **PNG** piece images in `assets/` (e.g., `wP.png`, `bQ.png`).  
- Easily replace them with your own artwork or alternate piece sets.

---

## Installation & Requirements

- **Python 3.7+** (or newer).
- **Pygame** (for GUI mode). Install it via:
  ```bash
  pip install pygame
  ```

Clone or download this repository and navigate into its folder:
```bash
git clone https://github.com/your-username/CheckMate-AI.git
cd CheckMate-AI
```

### Directory Structure
```
CheckMate-AI/
├── main.py            # Entry point for CLI or GUI
├── game_manager.py    # Handles game flow, turns, AI calls
├── gui.py             # Pygame interface (drag-and-drop, highlighting)
├── board.py           # Board logic, piece placement, move legality checks
├── search.py          # AI search (Minimax, Alpha-Beta)
├── move.py            # Move class (start, end, piece, capture, etc.)
├── evaluator.py       # Evaluate board states (material, etc.)
├── pieces/
│   ├── __init__.py
│   ├── piece.py
│   ├── pawn.py
│   ├── rook.py
│   ├── knight.py
│   ├── bishop.py
│   ├── queen.py
│   └── king.py
├── assets/
│   ├── wP.png         # White Pawn image
│   ├── wR.png         # White Rook image
│   ├── ... etc. ...
│   ├── bP.png         # Black Pawn image
│   ├── bR.png         # Black Rook image
│   └── ...
└── README.md          # This file
```

- **assets/**: Contains your piece images (one for each piece/color).
- **pieces/**: Specialized classes for each  piece type.
- **board.py**: The heart of the engine, sets up the board and enforces rules.
- **game_manager.py**: Orchestrates game turns, interacts with players or AI.
- **gui.py**: Implements the Pygame-based drag-and-drop interface.
- **search.py**: Contains AI logic (Minimax with alpha-beta pruning).

---

## Usage

Open a terminal in the `CheckMate-AI/` directory after installing dependencies.

### 1. GUI Mode
```bash
python main.py
```
Launches a Pygame window with drag-and-drop movement.  
By default, White is a human player and Black is the AI (or whichever configuration you set).

**How to play (GUI):**
- Click and hold on a piece to drag it; legal moves highlight.
- Release over a valid square to finalize the move.
- Close the window or press `Ctrl+C` in terminal to exit.

### 2. CLI Mode (Human vs. AI)
```bash
python main.py --cli
```
Displays an ASCII board in the terminal.  
White enters moves in standard algebraic notation (e.g., `e2e4`), then the AI plays automatically.

#### Sample CLI Session

```bash
> python main.py --cli
  8  r n b q k b n r
  7  p p p p p p p p
  6  . . . . . . . .
  5  . . . . . . . .
  4  . . . . . . . .
  3  . . . . . . . .
  2  P P P P P P P P
  1  R N B Q K B N R
     a b c d e f g h

WHITE's move (e.g. 'e2e4' or 'quit'): e2e4

  8  r n b q k b n r
  7  p p p p p p p p
  6  . . . . . . . .
  5  . . . . . . . .
  4  . . . . P . . .
  3  . . . . . . . .
  2  P P P P . P P P
  1  R N B Q K B N R
     a b c d e f g h

BLACK (AI) is thinking...
AI played: b8c6

  8  r . b q k b n r
  7  p p p p p p p p
  6  . . n . . . . .
  5  . . . . . . . .
  4  . . . . P . . .
  3  . . . . . . . .
  2  P P P P . P P P
  1  R N B Q K B N R
     a b c d e f g h

WHITE's move (e.g. 'e2e4' or 'quit'):
```

Type `quit` at any time to end the game.

### 3. CLI Mode (Two Humans)
```bash
python main.py --cli --2p
```
Disables the AI, letting two local players both enter moves.  
Useful for testing or playing a friend via a terminal.

---

## Contributing

We welcome contributions for bug fixes, AI enhancements, or new features.

1. Fork the repository and clone locally.
2. Create a new branch for your feature or fix (e.g., `git checkout -b feature/polish-gui`).
3. Commit and push your changes.
4. Open a Pull Request, describing your changes thoroughly.

### Potential areas to improve:
- Advanced Evaluation (positional heuristics, king safety, etc.)
- Move Ordering or Transposition Tables for faster AI.
- Fancy GUI Animations or a nicer 2D/3D board design.
- Additional Chess Rules like the 50-move rule or threefold repetition.

---

## License

Open-source under the MIT License. You’re free to modify and distribute, as long as the same license terms are maintained.

---

## Acknowledgments

- Pygame for enabling the GUI.
- Python community for libraries and tutorials.
- Everyone who contributed feedback, testing scenarios, and code improvements.

---

Happy coding!  
If you find any issues or have suggestions, please open an issue or PR. Enjoy your game of !
