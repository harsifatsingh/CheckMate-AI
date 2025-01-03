# pieces/pawn.py
from .piece import Piece
from move import Move

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        moves = []
        piece_at_start = board.get_piece_at(row, col)
        if piece_at_start != self:
            return moves  # just a sanity check

        # Determine direction
        if self.color == "WHITE":
            direction = -1   # White moves "up" the board (row decreases)
            start_row = 6    # typical start row for White if row=0 is top
        else:
            direction = +1   # Black moves "down" the board (row increases)
            start_row = 1    # typical start row for Black if row=0 is top

        # 1) One-square forward (only if empty)
        forward_row = row + direction
        forward_col = col
        if 0 <= forward_row < 8:
            if board.get_piece_at(forward_row, forward_col) is None:
                # not blocked
                moves.append(Move(row, col, forward_row, forward_col, self))
                
                # 2) Two-square forward if on starting rank, and empty
                if row == start_row:
                    two_forward_row = row + 2*direction
                    if board.get_piece_at(two_forward_row, forward_col) is None:
                        moves.append(Move(row, col, two_forward_row, forward_col, self))

        # 3) Captures: diagonally left & right
        for dc in [-1, +1]:
            capture_col = col + dc
            capture_row = row + direction
            if 0 <= capture_row < 8 and 0 <= capture_col < 8:
                target_piece = board.get_piece_at(capture_row, capture_col)
                if target_piece and target_piece.color != self.color:
                    # normal capture
                    moves.append(Move(row, col, capture_row, capture_col, self, target_piece))

                # If you have en passant logic, check it here. E.g.:
                # if (capture_row, capture_col) == board.en_passant_target:
                #    # create en-passant move
                #    moves.append(...)

        return moves

    def __str__(self):
        return 'P' if self.color == "WHITE" else 'p'
