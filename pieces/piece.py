class Piece:
    def __init__(self, color):
        """
        Base class for all chess pieces.
        color: "WHITE" or "BLACK"
        """
        self.color = color

    def get_legal_moves(self, board, row, col):
        """
        Return a list of legal moves this piece can make from the given position (row, col).
        This is a base method to be overridden by each specific piece type.
        """
        pass

    def __str__(self):
        """
        Return a string representation of the piece (e.g., 'P', 'N', 'B', 'R', 'Q', 'K').
        """
        pass
