class Move:
    def __init__(self, start_row, start_col, end_row, end_col, piece_moved, piece_captured=None):
        """
        A basic Move object.
        """
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col
        self.piece_moved = piece_moved
        self.piece_captured = piece_captured

    def __eq__(self, other):
        if not isinstance(other, Move):
            return False
        return (self.start_row == other.start_row and
                self.start_col == other.start_col and
                self.end_row == other.end_row and
                self.end_col == other.end_col and
                self.piece_moved == other.piece_moved and
                self.piece_captured == other.piece_captured)

    def __str__(self):
        """
        Human-readable format: e.g. 'e2e4'.
        """
        start_file = chr(ord('a') + self.start_col)
        start_rank = str(8 - self.start_row)
        end_file = chr(ord('a') + self.end_col)
        end_rank = str(8 - self.end_row)

        return f"{start_file}{start_rank}{end_file}{end_rank}"
