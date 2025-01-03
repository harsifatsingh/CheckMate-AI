class Piece:
    def __init__(self, color):
        self.color = color

    def get_legal_moves(self, board, row, col):
        """
        Return a list of moves (Move objects) this piece can make from (row, col).
        This method is overridden by derived classes.
        """
        return []

    def __str__(self):
        """
        Base class returns '?' for unknown piece type. 
        Children should override with appropriate letter.
        """
        return '?'
