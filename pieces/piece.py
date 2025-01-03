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

    def symbol(self):
        """
        By default, the symbol is str(self), e.g. 'p' or 'Q'.
        But we keep a separate method if we need direct logic in Board.
        """
        return str(self)