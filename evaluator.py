class Evaluator:
    def __init__(self):
        """
        Initialize anything needed for evaluation, e.g., piece values.
        """
        # Very simplistic piece values
        self.values = {
            'P': 1,   'N': 3,   'B': 3,
            'R': 5,   'Q': 9,   'K': 1000,
            # For black, we can just use the lowercase letter's uppercase equivalent
        }

    def evaluate(self, board):
        """
        Evaluate a board state and return a numeric score.
        Positive -> good for WHITE, negative -> good for BLACK.
        """
        score = 0
        for row in range(8):
            for col in range(8):
                piece = board.get_piece_at(row, col)
                if piece is not None:
                    symbol = str(piece)
                    if symbol.isupper():
                        score += self.values.get(symbol.upper(), 0)
                    else:
                        score -= self.values.get(symbol.upper(), 0)
        return score
