import pygame, sys
from .base_state import BaseState
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_PATH, FONT_SIZE, TEXT_COLOR # Zmieniono importy

class PauseState(BaseState):
    """
    Reprezentuje stan pauzy w grze.
    """
    def __init__(self, game, asset_manager):
        """
        Inicjalizuje stan pauzy.

        Args:
            game: Główny obiekt gry.
            asset_manager (AssetManager): Menedżer zasobów.
        """
        super().__init__(game, asset_manager) # Przekazanie asset_manager do konstruktora klasy bazowej
        self.game = game # Przechowaj referencję do gry
        try:
            # Użycie asset_manager do pobrania czcionek
            self.font = self.asset_manager.get_font(FONT_PATH, FONT_SIZE * 2) # Używamy większej czcionki dla napisu "Pauza"
            self.small_font = self.asset_manager.get_font(FONT_PATH, FONT_SIZE)
        except Exception as e: # Zmieniono typ wyjątku na bardziej ogólny
            print(f"Nie można załadować czcionki przez asset_manager: {e}")
            # Zastępcza czcionka systemowa - na wszelki wypadek
            self.font = pygame.font.SysFont(pygame.font.get_default_font(), FONT_SIZE * 2)
            self.small_font = pygame.font.SysFont(pygame.font.get_default_font(), FONT_SIZE)

        self.pause_text = self.font.render("Pauza", True, TEXT_COLOR) # Użycie TEXT_COLOR
        self.resume_text = self.small_font.render("Naciśnij P lub Enter, aby kontynuować", True, TEXT_COLOR) # Użycie TEXT_COLOR

        self.pause_rect = self.pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20)) # Dostosowanie pozycji
        self.resume_rect = self.resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)) # Dostosowanie pozycji

        # Półprzezroczysta warstwa
        self.overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.overlay.set_alpha(150) # Zmniejszenie przezroczystości
        self.overlay.fill((0, 0, 0)) # Czarny kolor

    def handle_input(self, event):
        """
        Obsługuje wejście użytkownika w stanie pauzy.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Dodano obsługę ESC
                self.game.state_manager.pop_state() # Zdejmij stan pauzy ze stosu, wracając do poprzedniego
            elif event.key == pygame.K_p or event.key == pygame.K_RETURN:
                self.game.state_manager.pop_state() # Zdejmij stan pauzy ze stosu, wracając do poprzedniego
        elif event.type == pygame.QUIT: # Dodano obsługę zamknięcia okna
            pygame.quit()
            sys.exit() # Zakończ program

    def update(self, dt):
        """
        Aktualizuje stan pauzy (nic nie robi, bo gra jest wstrzymana).

        Args:
            dt: Czas, który upłynął od ostatniej klatki (delta time).
        """
        pass # Na razie brak logiki aktualizacji

    def draw(self, surface):
        """
        Rysuje stan pauzy na ekranie.

        Args:
            surface: Powierzchnia Pygame do rysowania.
        """
        # 1. Narysuj poprzedni stan (zamrożona klatka gry)
        # Rysuj stan pod spodem (np. grę) - StateManager zajmie się tym
        # self.game.state_manager.states[-2].draw(surface)

        # Narysuj półprzezroczystą warstwę
        surface.blit(self.overlay, (0, 0))

        # Narysuj tekst pauzy
        surface.blit(self.pause_text, self.pause_rect)
        surface.blit(self.resume_text, self.resume_rect)