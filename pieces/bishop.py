from .piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        """
        Return a list of possible moves for a bishop.
        Moves are any number of squares diagonally until blocked.
        """
        pass
