from .piece import Piece
from move import Move

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        """
        Return a list of possible moves for a knight (L-shaped moves).
        Knight can jump over other pieces.
        """
        moves = []
        knight_moves = [
            (row+2, col+1),
            (row+2, col-1),
            (row-2, col+1),
            (row-2, col-1),
            (row+1, col+2),
            (row+1, col-2),
            (row-1, col+2),
            (row-1, col-2)
        ]

        for r, c in knight_moves:
            if 0 <= r < 8 and 0 <= c < 8:
                target_piece = board.get_piece_at(r, c)
                if target_piece is None:
                    moves.append(Move(row, col, r, c, board.get_piece_at(row, col)))
                else:
                    if target_piece.color != self.color:
                        moves.append(Move(row, col, r, c, board.get_piece_at(row, col), target_piece))
        return moves
    
    def __str__(self):
        return "N" if self.color == "white" else "n"