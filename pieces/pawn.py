from .piece import Piece
from move import Move

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        moves = []
        direction = -1 if self.color == "WHITE" else 1

        start_row = row
        start_col = col
        end_row = row + direction
        end_col = col

        if 0 <= end_row < 8 and board.get_piece_at(end_row, end_col) is None:
            moves.append(Move(start_row, start_col, end_row, end_col, self))

            if (self.color == "WHITE" and row == 6) or (self.color == "BLACK" and row == 1):
                # Can move 2 squares from starting position
                end_row = row + 2 * direction
                if board.get_piece_at(end_row, end_col) is None:
                    moves.append(Move(start_row, start_col, end_row, end_col, self))
        
        for capture_col in [col - 1, col + 1]:
            if 0 <= end_row < 8 and 0 <= capture_col < 8:
                target_piece = board.get_piece_at(end_row, capture_col)
                if target_piece is not None and target_piece.color != self.color:
                    moves.append(Move(start_row, start_col, end_row, capture_col, self, target_piece))

        return moves

    def __str__(self):
        return 'P' if self.color == "WHITE" else 'p'
