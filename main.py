import pygame

from fenster import GameWindow


if __name__ == "__main__":
    pygame.init()

    window_size = (800, 800)
    game_window = GameWindow(*window_size)
    game_window.run_game()