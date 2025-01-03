from game_manager import GameManager

def main():
    """
    Main entry point for the chess application.
    Initializes the GameManager and starts the game.
    """
    game_manager = GameManager()
    game_manager.start_game()

if __name__ == "__main__":
    main()
