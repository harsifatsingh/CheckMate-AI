from .piece import Piece
from move import Move

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_legal_moves(self, board, row, col):
        """
        Return a list of possible moves for a bishop.
        Moves are any number of squares diagonally until blocked.
        """
        moves = []
        directions = [(1,1), (-1,1), (1,-1), (-1,-1)]

        for drow, dcol in directions:
            r, c = row, col
            while True:
                r += drow
                c += dcol
                if 0 <= r < 8 and 0 <= c < 8:
                    target_piece = board.get_piece_at(r, c)
                    if target_piece is None:
                        moves.append(Move(row, col, r, c, board.get_piece_at(row, col)))  
                    else:
                        if target_piece.color != self.color:
                            moves.append(Move(row, col, r, c, board.get_piece_at(row, col), target_piece))
                        break
                else:
                    break
        return moves
    
    def __str__(self):
        return "B" if self.color == "white" else "b"