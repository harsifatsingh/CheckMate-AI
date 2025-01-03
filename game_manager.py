# game_manager.py

from board import Board
from search import Search

class GameManager:
    def __init__(self, use_gui=False, two_player=False):
        """
        Manages overall game flow & state.
        :param use_gui: bool -> are we in GUI mode or CLI?
        :param two_player: bool -> if True, two humans; else White vs AI
        """
        self.use_gui = use_gui
        self.two_player = two_player  # new param

        self.board = Board()
        self.board.setup_initial_position()

        self.search_algorithm = Search()  # for AI

        # White always starts
        self.current_player = "WHITE"
        self.running = True

    def start_game(self):
        """
        If we're not in GUI mode, we do a CLI loop.
        In two_player mode, both players input moves.
        Otherwise, White inputs, and Black is AI.
        """
        while self.running and not self.use_gui:
            self.display_board()

            # Check for checkmate/stalemate before the move
            if self.board.is_checkmate(self.current_player):
                print(f"Checkmate! {self.current_player} loses.")
                break
            if self.board.is_stalemate(self.current_player):
                print("Stalemate!")
                break

            # If two humans, always prompt for current player's move:
            if self.two_player:
                move_str = input(f"{self.current_player}'s move (e.g. 'e2e4' or 'quit'): ")
                self.handle_player_move(move_str)
            else:
                # Otherwise, White is the human, Black is AI
                if self.current_player == "WHITE":
                    move_str = input(f"{self.current_player}'s move (e.g. 'e2e4' or 'quit'): ")
                    self.handle_player_move(move_str)
                else:
                    print(f"{self.current_player} (AI) is thinking...")
                    self.handle_ai_move()

            # Switch
            self.current_player = "BLACK" if self.current_player == "WHITE" else "WHITE"

        print("Game over.")

    def handle_player_move(self, move_str):
        """
        For a CLI player's typed move.
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
        AI picks a move. 
        """
        move = self.search_algorithm.find_best_move(self.board, self.current_player, depth=3)
        if move:
            self.board.make_move(move)
        else:
            print(f"No legal moves for {self.current_player}!")

    def display_board(self):
        """
        Print ASCII board in CLI mode.
        """
        print(self.board)
