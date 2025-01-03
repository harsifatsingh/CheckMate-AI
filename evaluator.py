class Evaluator:
    def __init__(self):
        # Basic piece values
        self.values = {
            'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 1000
        }

    def evaluate(self, board):
        score = 0
        for row in range(8):
            for col in range(8):
                piece = board.get_piece_at(row, col)
                if piece:
                    symbol = piece.symbol()
                    base_val = self.values.get(symbol.upper(), 0)
                    if symbol.isupper():
                        score += base_val
                    else:
                        score -= base_val
        return score
