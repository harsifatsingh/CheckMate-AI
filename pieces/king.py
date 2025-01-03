from .piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        """
        Return a list of possible moves for a king.
        Moves one square in any direction if it’s not in check.
        Also handle castling if allowed.
        """
        pass
