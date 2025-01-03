import pygame
import sys

TILE_SIZE = 80
BOARD_SIZE = 8
WINDOW_SIZE = TILE_SIZE * BOARD_SIZE

WHITE_COLOR = (232, 235, 239)  # Light square color
BLACK_COLOR = (125, 135, 150)  # Dark square color

PIECE_IMAGES = {}  # We'll load images lazily

class GUI:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Chess Engine")
        self.selected_square = None  # (row, col)
        self.running = True
        self.load_piece_images()

    def load_piece_images(self):
        """
        Load piece images from some folder or resources.
        For demonstration, you must provide your own images
        named like 'wP.png', 'wR.png', 'wN.png', etc.
        If you don’t have images, this part can be omitted or replaced.
        """
        piece_types = ['P','R','N','B','Q','K']
        colors = ['w','b']
        for color in colors:
            for piece in piece_types:
                filename = f"assets/{color}{piece}.svg.png"
                try:
                    image = pygame.image.load(filename)
                    image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
                    PIECE_IMAGES[color+piece] = image
                except:
                    pass  # If missing images, skip

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(60)
            self.handle_events()
            self.draw_board()
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                row, col = self.get_clicked_square(pygame.mouse.get_pos())
                self.handle_click(row, col)

    def handle_click(self, row, col):
        if self.selected_square is None:
            # Select piece if it's the current player's piece
            piece = self.game_manager.board.get_piece_at(row, col)
            if piece and piece.color == self.game_manager.current_player:
                self.selected_square = (row, col)
        else:
            # Attempt move from selected_square to (row, col)
            start_row, start_col = self.selected_square
            algebraic = self.coords_to_algebraic(start_row, start_col, row, col)
            # Use the same handle logic as CLI
            self.game_manager.handle_player_move(algebraic)
            self.selected_square = None

    def coords_to_algebraic(self, start_row, start_col, end_row, end_col):
        """
        Convert from matrix coords to e.g. 'e2e4'.
        """
        start_file = chr(ord('a') + start_col)
        start_rank = str(8 - start_row)
        end_file = chr(ord('a') + end_col)
        end_rank = str(8 - end_row)
        return f"{start_file}{start_rank}{end_file}{end_rank}"

    def get_clicked_square(self, pos):
        x, y = pos
        col = x // TILE_SIZE
        row = y // TILE_SIZE
        return (row, col)

    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = WHITE_COLOR if (row + col) % 2 == 0 else BLACK_COLOR
                rect = pygame.Rect(col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, color, rect)
                piece = self.game_manager.board.get_piece_at(row, col)
                if piece:
                    symbol = str(piece)  # e.g. 'P' or 'p'
                    # Determine color prefix
                    color_prefix = 'w' if symbol.isupper() else 'b'
                    piece_key = color_prefix + symbol.upper()
                    if piece_key in PIECE_IMAGES:
                        self.screen.blit(PIECE_IMAGES[piece_key], (col*TILE_SIZE, row*TILE_SIZE))
