from .piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        """
        Return a list of possible moves for a knight (L-shaped moves).
        Knight can jump over other pieces.
        """
        pass
