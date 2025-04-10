import pygame, sys
from .base_state import BaseState
# from .playing_state import PlayingState # Import przeniesiony do funkcji, aby uniknąć cyklicznego importu
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, TEXT_COLOR, FONT_PATH, FONT_SIZE # Dodano FONT_PATH, FONT_SIZE

class MenuState(BaseState):
    """
    Reprezentuje stan menu głównego gry.
    """
    def __init__(self, game, asset_manager): # Dodano asset_manager
        """
        Inicjalizuje stan menu.

        Args:
            game: Główny obiekt gry.
            asset_manager (AssetManager): Menedżer zasobów.
        """
        super().__init__(game, asset_manager) # Przekazanie asset_manager do konstruktora klasy bazowej
        # Inicjalizacja czcionki - upewnij się, że pygame.font został zainicjowany
        # Usunięto inicjalizację czcionki tutaj, używamy asset_manager
        # if not pygame.font.get_init():
        #     pygame.font.init()
        # self.font = pygame.font.Font(None, 36) # Użyj domyślnej czcionki
        self.font = self.asset_manager.get_font(FONT_PATH, FONT_SIZE) # Pobranie czcionki z asset_manager
        self.title_font = self.asset_manager.get_font(FONT_PATH, FONT_SIZE * 2) # Większa czcionka dla tytułu
        self.option_font = self.asset_manager.get_font(FONT_PATH, FONT_SIZE) # Czcionka dla opcji

        self.title_text = self.title_font.render("Snake Game", True, TEXT_COLOR)
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

        self.play_text = self.option_font.render("Naciśnij Enter, aby zagrać", True, TEXT_COLOR)
        self.play_rect = self.play_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))

        self.quit_text = self.option_font.render("Naciśnij ESC, aby wyjść", True, TEXT_COLOR)
        self.quit_rect = self.quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))

    def handle_input(self, event):
        """
        Obsługuje wejście użytkownika w stanie menu.

        Args:
            event: Zdarzenie Pygame.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Import lokalny, aby uniknąć cyklicznego importu
                from .playing_state import PlayingState
                # Zmień stan na PlayingState po naciśnięciu Enter, przekazując asset_manager
                self.game.state_manager.change_state(PlayingState(self.game, self.asset_manager))
            elif event.key == pygame.K_ESCAPE: # Dodano obsługę ESC
                pygame.quit()
                sys.exit() # Zakończ program

    def update(self, dt):
        """
        Aktualizuje logikę stanu menu (na razie puste).

        Args:
            dt: Czas, który upłynął od ostatniej klatki (delta time).
        """
        pass # Na razie brak logiki aktualizacji w menu

    def draw(self, surface):
        """
        Rysuje elementy stanu menu na podanej powierzchni.

        Args:
            surface: Powierzchnia Pygame do rysowania.
        """
        surface.fill(BACKGROUND_COLOR) # Użyj koloru tła z config
        surface.blit(self.title_text, self.title_rect)
        surface.blit(self.play_text, self.play_rect)
        surface.blit(self.quit_text, self.quit_rect) # Dodano rysowanie tekstu wyjścia