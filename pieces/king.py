from .piece import Piece
from move import Move

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        moves = []
        king_moves = [
            (row+1, col),   (row-1, col),
            (row, col+1),   (row, col-1),
            (row+1, col+1), (row+1, col-1),
            (row-1, col+1), (row-1, col-1)
        ]
        for (r, c) in king_moves:
            if 0 <= r < 8 and 0 <= c < 8:
                target_piece = board.get_piece_at(r, c)
                if target_piece is None:
                    moves.append(Move(row, col, r, c, board.get_piece_at(row, col)))
                else:
                    # capture if enemy
                    if target_piece.color != self.color:
                        moves.append(Move(row, col, r, c, board.get_piece_at(row, col), target_piece))

        # In a full implementation, you'd handle castling here.
        return moves

    def __str__(self):
        return 'K' if self.color == "WHITE" else 'k'
