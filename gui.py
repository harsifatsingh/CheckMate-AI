import pygame
import sys

TILE_SIZE = 80
BOARD_SIZE = 8
WINDOW_WIDTH = TILE_SIZE * BOARD_SIZE
WINDOW_HEIGHT = TILE_SIZE * BOARD_SIZE

LIGHT_SQUARE = (240, 217, 181)  # Light beige
DARK_SQUARE  = (181, 136, 99)   # Brown
HIGHLIGHT_SQUARE = (186, 202, 68)  # Light green highlight

PIECE_IMAGES = {}

class ChessGUI:
    def __init__(self, game_manager):
        """
        :param game_manager: An instance of your existing GameManager,
                             which has 'board', 'current_player', etc.
        """
        self.game_manager = game_manager
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Chess Engine - Drag & Drop")

        # Dragging logic
        self.dragging_piece = None
        self.drag_start_row = None
        self.drag_start_col = None
        self.drag_offset_x = 0
        self.drag_offset_y = 0

        # We'll store the set of squares (row,col) where the dragged piece can legally move.
        self.dragging_legal_moves = []

        self.load_piece_images()
        self.running = True
        self.clock = pygame.time.Clock()

    def load_piece_images(self):
        piece_types = ['P', 'N', 'B', 'R', 'Q', 'K']
        colors = ['w','b']
        for color in colors:
            for pt in piece_types:
                filename = f"assets/{color}{pt}.svg.png"
                try:
                    img = pygame.image.load(filename)
                    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                    PIECE_IMAGES[color + pt] = img
                except:
                    print(f"Could not load image: {filename}")

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()

            # If AI's turn (say black is AI) and not dragging
            if (self.game_manager.current_player == "BLACK"
                and not self.dragging_piece):
                self.ai_move()

            self.draw_board()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click
                    self.handle_mouse_down(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.handle_mouse_up(event.pos)

    def handle_mouse_down(self, pos):
        """
        Start dragging if we clicked on our own piece.
        Then gather the squares to which it can move
        so we can highlight them.
        """
        row, col = self.coords_to_rowcol(pos)
        board = self.game_manager.board
        piece = board.get_piece_at(row, col)

        # Check if it's the current player's piece
        if piece and piece.color == self.game_manager.current_player:
            self.dragging_piece = piece
            self.drag_start_row = row
            self.drag_start_col = col
            self.drag_offset_x = pos[0] - col * TILE_SIZE
            self.drag_offset_y = pos[1] - row * TILE_SIZE

            # 1) Get all legal moves for the current player
            all_legal_moves = board.generate_legal_moves(self.game_manager.current_player)

            # 2) Filter only those that start from (row,col)
            #    and store their end positions
            self.dragging_legal_moves = []
            for mv in all_legal_moves:
                if (mv.start_row == row and mv.start_col == col):
                    self.dragging_legal_moves.append((mv.end_row, mv.end_col))
        else:
            self.dragging_piece = None
            self.dragging_legal_moves = []

    def handle_mouse_up(self, pos):
        if not self.dragging_piece:
            return

        row, col = self.coords_to_rowcol(pos)
        # Check if (row,col) is in our dragging_legal_moves
        if (row, col) in self.dragging_legal_moves:
            # Convert to algebraic
            start_alg = self.rowcol_to_algebraic(self.drag_start_row, self.drag_start_col)
            end_alg = self.rowcol_to_algebraic(row, col)
            move_str = start_alg + end_alg

            # Attempt the move
            self.game_manager.handle_player_move(move_str)

            # If it was white, switch to black
            if self.game_manager.current_player == "WHITE":
                self.game_manager.current_player = "BLACK"
            else:
                self.game_manager.current_player = "WHITE"
        else:
            # Not a legal square, so do nothing; piece reverts
            pass

        # Reset drag
        self.dragging_piece = None
        self.drag_start_row = None
        self.drag_start_col = None
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        self.dragging_legal_moves = []

    def ai_move(self):
        """
        If black is AI, pick the best move from generate_legal_moves().
        """
        move = self.game_manager.search_algorithm.find_best_move(
            self.game_manager.board,
            self.game_manager.current_player,
            depth=3
        )
        if move:
            self.game_manager.board.make_move(move)
        else:
            print(f"No legal moves for {self.game_manager.current_player}.")
        # Switch to white
        self.game_manager.current_player = "WHITE"

    def draw_board(self):
        # 1) Draw squares
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = LIGHT_SQUARE if (row+col)%2 == 0 else DARK_SQUARE
                rect = pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, color, rect)

        # 2) Highlight squares if dragging
        #    We'll highlight squares that are in self.dragging_legal_moves
        if self.dragging_piece:
            for (r,c) in self.dragging_legal_moves:
                highlight_rect = pygame.Rect(c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, HIGHLIGHT_SQUARE, highlight_rect)

        # 3) Draw pieces (except the one being dragged)
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = self.game_manager.board.get_piece_at(row, col)
                if piece:
                    # If it's the currently dragged piece at the start square, skip
                    if (piece == self.dragging_piece 
                        and row == self.drag_start_row 
                        and col == self.drag_start_col):
                        continue
                    self.draw_piece(piece, row, col)

        # 4) If dragging, draw the piece under the mouse
        if self.dragging_piece:
            mx, my = pygame.mouse.get_pos()
            x = mx - self.drag_offset_x
            y = my - self.drag_offset_y
            self.draw_piece_at_pixel(self.dragging_piece, x, y)

    def draw_piece(self, piece, row, col):
        symbol = str(piece)
        color_prefix = 'w' if symbol.isupper() else 'b'
        piece_type = symbol.upper()
        image = PIECE_IMAGES.get(color_prefix + piece_type)
        if image:
            self.screen.blit(image, (col*TILE_SIZE, row*TILE_SIZE))

    def draw_piece_at_pixel(self, piece, x, y):
        symbol = str(piece)
        color_prefix = 'w' if symbol.isupper() else 'b'
        piece_type = symbol.upper()
        image = PIECE_IMAGES.get(color_prefix + piece_type)
        if image:
            self.screen.blit(image, (x,y))

    def coords_to_rowcol(self, pos):
        x,y = pos
        col = x // TILE_SIZE
        row = y // TILE_SIZE
        return (row, col)

    def rowcol_to_algebraic(self, row, col):
        file_letter = chr(ord('a') + col)
        rank_number = 8 - row
        return f"{file_letter}{rank_number}"
