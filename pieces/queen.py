from .piece import Piece
from move import Move
from .rook import Rook
from .bishop import Bishop

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        """
        Return a list of possible moves for a queen.
        moves = Rook.get_legal_moves(self, board, row, col)
        moves.extend(Bishop.get_legal_moves(self, board, row, col))
        """
        moves = Rook.get_legal_moves(board, row, col)
        moves.extend(Bishop.get_legal_moves(board, row, col))
        return moves
    
    def __str__(self):
        return "Q" if self.color == "white" else "q"
