from move import Move
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King

class Board:
    def __init__(self):
        """
        Initialize an 8x8 board as a 2D list.
        None means no piece on that square.
        """
        self.squares = self._create_empty_board()

    def _create_empty_board(self):
        """
        Helper to create an 8x8 grid of None.
        """
        return [[None for _ in range(8)] for _ in range(8)]

    def setup_initial_position(self):
        """
        Place all pieces in their initial positions.
        """
        # Pawns
        for col in range(8):
            self.squares[1][col] = Pawn("WHITE")
            self.squares[6][col] = Pawn("BLACK")

        # Rooks
        self.squares[0][0] = Rook("WHITE")
        self.squares[0][7] = Rook("WHITE")
        self.squares[7][0] = Rook("BLACK")
        self.squares[7][7] = Rook("BLACK")

        # Knights
        self.squares[0][1] = Knight("WHITE")
        self.squares[0][6] = Knight("WHITE")
        self.squares[7][1] = Knight("BLACK")
        self.squares[7][6] = Knight("BLACK")

        # Bishops
        self.squares[0][2] = Bishop("WHITE")
        self.squares[0][5] = Bishop("WHITE")
        self.squares[7][2] = Bishop("BLACK")
        self.squares[7][5] = Bishop("BLACK")

        # Queens
        self.squares[0][3] = Queen("WHITE")
        self.squares[7][3] = Queen("BLACK")

        # Kings
        self.squares[0][4] = King("WHITE")
        self.squares[7][4] = King("BLACK")

    def parse_move_string(self, move_str, color):
        """
        Given a string like 'e2e4', convert to a Move object.
        If invalid format, return None.
        """
        if len(move_str) < 4:
            return None

        # Convert algebraic notation: 'a' -> col=0, 'b'->1... 'h'->7
        start_col = ord(move_str[0]) - ord('a')
        start_row = 8 - int(move_str[1])  # '1' -> row=7, '2'->6, etc.
        end_col = ord(move_str[2]) - ord('a')
        end_row = 8 - int(move_str[3])

        # Basic validation
        if not (0 <= start_row < 8 and 0 <= start_col < 8):
            return None
        if not (0 <= end_row < 8 and 0 <= end_col < 8):
            return None

        piece_moved = self.squares[start_row][start_col]
        if piece_moved is None or piece_moved.color != color:
            # No piece of the correct color at start square
            return None

        piece_captured = self.squares[end_row][end_col]
        return Move(start_row, start_col, end_row, end_col, piece_moved, piece_captured)

    def get_piece_at(self, row, col):
        return self.squares[row][col]

    def set_piece_at(self, row, col, piece):
        self.squares[row][col] = piece

    def make_move(self, move):
        """
        Update the board for the given move:
        - Move the piece on start -> end.
        - Replace (capture) or set None on start.
        """
        self.squares[move.end_row][move.end_col] = move.piece_moved
        self.squares[move.start_row][move.start_col] = None

    def generate_legal_moves(self, color):
        """
        Generate all pseudo-legal moves for the given color 
        (NOT checking for check or checkmate for this example).
        """
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self.squares[row][col]
                if piece and piece.color == color:
                    piece_moves = piece.get_legal_moves(self, row, col)
                    moves.extend(piece_moves)
        return moves

    def __str__(self):
        """
        Return a string representation of the board.
        Top row is row=0 in our matrix, but visually it's rank 8 in chess.
        """
        board_str = ""
        for row in range(8):
            rank_str = f"{8 - row} "
            for col in range(8):
                piece = self.squares[row][col]
                rank_str += f"{str(piece) if piece else '.'} "
            board_str += rank_str + "\n"
        board_str += "  a b c d e f g h\n"
        return board_str
