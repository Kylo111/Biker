import pygame
from .base_state import BaseState
from .menu_state import MenuState # Import MenuState
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, TEXT_COLOR, FONT_PATH, FONT_SIZE # Dodano importy FONT_PATH i FONT_SIZE

class GameOverState(BaseState):
    """
    Reprezentuje stan końca gry.
    """
    def __init__(self, game, asset_manager, score): # Dodano asset_manager i score
        """
        Inicjalizuje stan końca gry.

        Args:
            game: Główny obiekt gry.
            asset_manager (AssetManager): Menedżer zasobów.
            score (int): Wynik gracza.
        """
        super().__init__(game, asset_manager) # Przekazanie asset_manager do konstruktora klasy bazowej
        self.score = score # Przechowaj wynik
        # Inicjalizacja czcionki - upewnij się, że pygame.font został zainicjowany
        # Usunięto inicjalizację czcionki tutaj, używamy asset_manager
        # if not pygame.font.get_init():
        #     pygame.font.init()
        # self.font = pygame.font.Font(None, 36) # Użyj domyślnej czcionki
        self.font = self.asset_manager.get_font(FONT_PATH, FONT_SIZE) # Pobranie czcionki z asset_manager
        self.text = self.font.render(f"Game Over! Score: {self.score}", True, TEXT_COLOR) # Wyświetl wynik, użyj TEXT_COLOR
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.prompt_text = self.font.render("Press Enter to return to Menu", True, TEXT_COLOR) # Dodano tekst podpowiedzi, użyj TEXT_COLOR
        self.prompt_rect = self.prompt_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)) # Dodano pozycję podpowiedzi

    def handle_input(self, event):
        """
        Obsługuje wejście użytkownika w stanie końca gry.

        Args:
            event: Zdarzenie Pygame.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Zmień stan na MenuState po naciśnięciu Enter, przekazując asset_manager
                self.game.state_manager.change_state(MenuState(self.game, self.asset_manager))

    def update(self, dt):
        """
        Aktualizuje logikę stanu końca gry (na razie puste).

        Args:
            dt: Czas, który upłynął od ostatniej klatki (delta time).
        """
        pass # Na razie brak logiki aktualizacji

    def draw(self, surface):
        """
        Rysuje elementy stanu końca gry na podanej powierzchni.

        Args:
            surface: Powierzchnia Pygame do rysowania.
        """
        # Użyj innego koloru tła, np. ciemnoczerwonego
        surface.fill((150, 0, 0))
        surface.blit(self.text, self.text_rect)
        surface.blit(self.prompt_text, self.prompt_rect) # Dodano rysowanie podpowiedzi