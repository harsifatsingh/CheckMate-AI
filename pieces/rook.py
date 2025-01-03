from .piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        """
        Return a list of possible moves for a rook.
        Moves are any number of squares along rank/file until blocked.
        """
        pass
