from board import Board
from search import Search

class GameManager:
    def __init__(self, use_gui=False):
        """
        Initialize the GameManager:
        - Create a Board object.
        - Create a Search (AI) object.
        - Setup any required game state variables.
        - use_gui indicates if we are in a Pygame loop or CLI.
        """
        self.use_gui = use_gui
        self.board = Board()
        self.board.setup_initial_position()
        self.search_algorithm = Search()
        self.current_player = "WHITE"
        self.running = True

    def start_game(self):
        """
        Start the game loop in a simple console-based manner (CLI).
        If we're using a GUI, we won't call this method; 
        the GUI event loop is in gui.py instead.
        """
        while self.running and not self.use_gui:
            self.display_board()

            if self.board.is_checkmate(self.current_player):
                print(f"Checkmate! {self.current_player} has lost.")
                break

            if self.board.is_stalemate(self.current_player):
                print("Stalemate!")
                break

            if self.current_player == "WHITE":
                move_str = input(f"{self.current_player}'s move (e.g., 'e2e4', or 'quit'): ")
                self.handle_player_move(move_str)
            else:
                print(f"{self.current_player} (AI) is thinking...")
                self.handle_ai_move()

            self.current_player = "BLACK" if self.current_player == "WHITE" else "WHITE"

    def handle_player_move(self, move_str):
        """
        Handle the player's move input (e.g., 'e2e4').
        - If 'quit', set running = False.
        - Else parse and attempt the move.
        """
        if move_str.lower() == 'quit':
            self.running = False
            return

        move = self.board.parse_move_string(move_str, self.current_player)
        if move and self.board.is_legal_move(move, self.current_player):
            self.board.make_move(move)
        else:
            if not self.use_gui:
                print("Illegal move or invalid input. Try again.")

    def handle_ai_move(self):
        """
        Use the Search object to determine the best move for the AI.
        Then execute the move on the board.
        """
        move = self.search_algorithm.find_best_move(self.board, self.current_player, depth=4)
        if move:
            self.board.make_move(move)
            print(f"AI played: {move}")
        else:
            print(f"No legal moves found for {self.current_player}.")

    def display_board(self):
        print(self.board)
