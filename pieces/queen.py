# pieces/queen.py
from .piece import Piece
from move import Move

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        moves = []

        # Rook-like directions
        rook_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for drow, dcol in rook_directions:
            r, c = row, col
            while True:
                r += drow
                c += dcol
                if 0 <= r < 8 and 0 <= c < 8:
                    target_piece = board.get_piece_at(r, c)
                    if target_piece is None:
                        # Empty square
                        moves.append(
                            Move(row, col, r, c, board.get_piece_at(row, col))
                        )
                    else:
                        # Capture if enemy
                        if target_piece.color != self.color:
                            moves.append(
                                Move(row, col, r, c, board.get_piece_at(row, col), target_piece)
                            )
                        break
                else:
                    break

        # Bishop-like directions
        bishop_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for drow, dcol in bishop_directions:
            r, c = row, col
            while True:
                r += drow
                c += dcol
                if 0 <= r < 8 and 0 <= c < 8:
                    target_piece = board.get_piece_at(r, c)
                    if target_piece is None:
                        moves.append(
                            Move(row, col, r, c, board.get_piece_at(row, col))
                        )
                    else:
                        if target_piece.color != self.color:
                            moves.append(
                                Move(row, col, r, c, board.get_piece_at(row, col), target_piece)
                            )
                        break
                else:
                    break

        return moves

    def __str__(self):
        return 'Q' if self.color == "WHITE" else 'q'
