import pygame # Dodaj import pygame
from src.core.game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit() # Dodaj zakończenie Pygame po wyjściu z pętli gry