from .piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        """
        Return a list of possible moves for a pawn at (row, col).
        Consider forward movement, captures, en passant, and promotions.
        """
        pass
