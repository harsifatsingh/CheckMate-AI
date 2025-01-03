# main.py

import sys
from game_manager import GameManager
from gui import ChessGUI

def main():
    """
    Main entry point for the application.
    
    Usage examples:
      python main.py --cli           -> Play White vs AI (Black)
      python main.py --cli --2p      -> Two humans, no AI
      python main.py                -> GUI mode (drag & drop)
    """
    if "--cli" in sys.argv:
        if "--2p" in sys.argv:
            # Two-human CLI mode
            gm = GameManager(use_gui=False, two_player=True)
        else:
            # One-human (White) vs AI (Black)
            gm = GameManager(use_gui=False, two_player=False)
        gm.start_game()
    else:
        # GUI
        gm = GameManager(use_gui=True, two_player=False) 
        # If you want a two-human GUI, set two_player=True 
        # and skip AI logic in the GUI.
        gui = ChessGUI(gm)
        gui.run()

if __name__ == "__main__":
    main()
