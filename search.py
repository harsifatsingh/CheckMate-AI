import random
from evaluator import Evaluator

class Search:
    def __init__(self):
        """
        Create an evaluator instance and set up any search-related parameters (like depth).
        """
        self.evaluator = Evaluator()

    def find_best_move(self, board, color, depth):
        """
        In this basic example, we'll just pick a random legal move for the AI.
        """
        moves = board.generate_legal_moves(color)
        if not moves:
            return None
        return random.choice(moves)
