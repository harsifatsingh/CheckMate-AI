import sys
from game_manager import GameManager
from gui import GUI

def main():
    """
    Simple CLI usage:
    > python main.py --cli
    or
    > python main.py (without args) for GUI-based usage.
    """
    if "--cli" in sys.argv:
        # Run a CLI-based version
        game_manager = GameManager(use_gui=False)
        game_manager.start_game()
    else:
        # Run a GUI-based version (Pygame)
        game_manager = GameManager(use_gui=True)
        gui = GUI(game_manager)
        gui.run()

if __name__ == "__main__":
    main()
