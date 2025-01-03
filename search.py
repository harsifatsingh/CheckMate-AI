import math
import random
from evaluator import Evaluator

class Search:
    def __init__(self):
        self.evaluator = Evaluator()
        self.transposition_table = {}  # { board_fen_or_str : (depth, score) }

    def find_best_move(self, board, color, depth=4):
        """
        Main entry to the search. 
        Return best move according to minimax with alpha-beta up to 'depth'.
        """
        best_move = None
        best_score = -math.inf if color == "WHITE" else math.inf

        moves = board.generate_legal_moves(color)

        if not moves:
            return None

        # Basic move ordering: sort captures to front
        moves.sort(key=lambda m: 1 if m.piece_captured else 0, reverse=True)

        alpha, beta = -math.inf, math.inf

        for move in moves:
            board.make_move(move)
            score = self._minimax(board, self._opponent(color), depth - 1, alpha, beta)
            board.undo_move()

            if color == "WHITE":
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, best_score)
            else:
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, best_score)

            if alpha >= beta:
                break  # alpha-beta cutoff

        return best_move

    def _minimax(self, board, color, depth, alpha, beta):
        """
        Minimax with alpha-beta. 
        Return a numeric score from perspective of White (higher is better for White).
        """
        # Transposition check
        board_key = self._board_to_key(board)  
        # The key might be a FEN string or simpler approach:
        # board_key = str(board) + ... (plus castling info, etc.)

        if board_key in self.transposition_table:
            stored_depth, stored_score = self.transposition_table[board_key]
            if stored_depth >= depth:
                return stored_score

        if depth == 0:
            score = self.evaluator.evaluate(board)
            self.transposition_table[board_key] = (depth, score)
            return score

        if board.is_checkmate(color):
            # If color is checkmated, that's good for the other side
            return -99999 if color == "WHITE" else 99999
        if board.is_stalemate(color):
            return 0

        moves = board.generate_legal_moves(color)
        if not moves:
            # No moves but not in check => stalemate
            return 0

        # Basic move ordering
        moves.sort(key=lambda m: 1 if m.piece_captured else 0, reverse=True)

        if color == "WHITE":
            best_score = -math.inf
            for move in moves:
                board.make_move(move)
                score = self._minimax(board, self._opponent(color), depth - 1, alpha, beta)
                board.undo_move()
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        else:
            best_score = math.inf
            for move in moves:
                board.make_move(move)
                score = self._minimax(board, self._opponent(color), depth - 1, alpha, beta)
                board.undo_move()
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break

        # Store in transposition table
        self.transposition_table[board_key] = (depth, best_score)
        return best_score

    def _board_to_key(self, board):
        """
        Create a simple string key for the board + castling rights + en passant.
        Real engines use Zobrist hashing.
        """
        rows = []
        for row in range(8):
            cols = []
            for col in range(8):
                piece = board.get_piece_at(row, col)
                if piece:
                    cols.append(str(piece))
                else:
                    cols.append(".")
            rows.append("".join(cols))
        # add castling info & en passant
        castling = (board.white_can_castle_kingside,
                    board.white_can_castle_queenside,
                    board.black_can_castle_kingside,
                    board.black_can_castle_queenside)
        enp = board.en_passant_target
        return "|".join(rows) + f"|{castling}|{enp}"

    def _opponent(self, color):
        return "WHITE" if color == "BLACK" else "BLACK"
