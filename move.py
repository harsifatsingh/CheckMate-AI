class Move:
    def __init__(self, start_row, start_col, end_row, end_col, piece_moved, piece_captured=None, is_en_passant=False, is_castling=False, promotion=None):
        """
        Encapsulates a chess move.
        - start_row, start_col: coordinates of the piece before the move
        - end_row, end_col: coordinates after the move
        - piece_moved: reference to the piece being moved
        - piece_captured: reference to the piece captured (if any)
        - is_en_passant: boolean indicating if this move is an en passant capture
        - is_castling: boolean indicating if this move is a castling move
        - promotion: piece type to promote to if this move is a pawn promotion
        """
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col
        self.piece_moved = piece_moved
        self.piece_captured = piece_captured
        self.is_en_passant = is_en_passant
        self.is_castling = is_castling
        self.promotion = promotion

    def __str__(self):
        """
        String representation of the move, e.g. "e2e4" or "e7e8Q".
        """
        pass
