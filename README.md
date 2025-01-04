# Chess Engine

This Python-based Chess Engine supports both command-line and graphical (Pygame) interfaces. You can play:

- **Human vs. AI** (in CLI or GUI)
- **Two-human mode** (in CLI or GUI)
- Drag-and-drop piece movement in the GUI, including move highlighting.

The AI is powered by a Minimax search with Alpha-Beta pruning. All standard chess rules, including check/checkmate detection, are implemented. Special rules like castling, en passant, and promotions are also supported.

## Features

### Multiple Modes
- **CLI**: Command-line interface with text-based board display.
- **GUI**: Pygame-based board with drag-and-drop pieces, similar to chess.com style.
- Human vs. AI or Two humans (both in CLI or GUI mode).

### Minimax AI (Alpha-Beta)
- Evaluates positions with a material-based heuristic.
- Configurable search depth.

### Legal Move Generation
- Distinguishes pseudo-legal from fully legal moves (no illegal captures, no pinned-piece moves).
- Automatic check/checkmate/stalemate detection.

### Move Highlighting (GUI)
- Highlights squares to which a dragged piece can move.
- Prevents dropping a piece on illegal squares.

### Piece Images
- Choose your own set of PNG images (e.g., `wP.png`, `bQ.png`) in the `assets/` folder for the GUI.

## Installation & Requirements

- **Python 3.7+** (or any recent version of Python 3).
- **Pygame** (for GUI mode). Install via:

```bash
pip install pygame
```

1. Clone or download this repository.
2. Ensure your terminal/command prompt is in the project directory.

## Directory Structure

```plaintext
chess_engine/
├── main.py
├── game_manager.py
├── gui.py
├── board.py
├── search.py
├── move.py
├── evaluator.py
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
│   ├── wP.png
│   ├── wR.png
│   ├── ...
│   ├── bP.png
│   ├── bR.png
│   └── ...
└── README.md
```

- `assets/`: Place your piece images here (e.g., `wP.png` for White Pawn, `bK.png` for Black King, etc.).
- `pieces/`: All piece-specific classes.
- `board.py`: Contains the Board class (setup, move application, legality checking).
- `game_manager.py`: The main driver for game flow (turns, inputs, calls AI).
- `gui.py`: The Pygame-based interface for drag-and-drop.
- `search.py`: AI logic (Minimax + Alpha-Beta).
- `main.py`: Entry point for launching the game (CLI or GUI).

## Usage

After installing dependencies, open a terminal in the `chess_engine/` directory.

### GUI Mode

```bash
python main.py
```

- Launches a Pygame window with a drag-and-drop interface.
- By default, it’s set to Human (White) vs. AI (Black) or whichever mode you configured.

### CLI Mode (Human vs. AI)

```bash
python main.py --cli
```

- Displays an ASCII board in your terminal.
- White types moves like `e2e4`, and Black is controlled by the AI.

### CLI Mode (Two Humans)

```bash
python main.py --cli --2p
```

- Both players type moves. No AI involved.

### Move Notation
- Type moves in algebraic format, e.g., `e2e4`.
- Type `quit` to end the game.

### Drag-and-drop (GUI mode)
- Click and hold on a piece to drag it.
- Legal moves highlight.
- Release on a valid square to finalize the move.

## Contributing

1. Fork the repository and clone locally.
2. Create a new branch for your feature or fix.
3. Commit and push your work.
4. Open a Pull Request describing your changes.

We welcome improvements such as:
- Better evaluation heuristics.
- Enhanced GUI visuals or animations.
- Additional chess rules (3-fold repetition, 50-move rule, etc.).
- Move ordering optimizations or transposition tables for the AI.

## License

This project is open-source under the [MIT License](LICENSE), which allows commercial and private use, modification, and distribution.

### Happy Coding!

If you find any issues or have improvements, feel free to submit a pull request or open an issue. Thank you for checking out **Chess-engine**!