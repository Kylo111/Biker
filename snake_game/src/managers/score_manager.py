import pygame
from config import SCORE_COLOR, FONT_SIZE, SCORE_POSITION

class ScoreManager:
    """
    Klasa zarządzająca wynikiem gry (punktacją) i jej wyświetlaniem.
    """
    def __init__(self):
        """
        Inicjalizuje menedżera wyników.
        """
        self.score = 0
        # Inicjalizacja czcionki Pygame. Używamy domyślnej czcionki systemowej.
        # pygame.font.init() jest zazwyczaj wywoływane przez pygame.init(),
        # więc nie musimy go tutaj wywoływać osobno.
        # Użycie None jako nazwy czcionki wybiera domyślną czcionkę systemową.
        try:
            self.font = pygame.font.Font(None, FONT_SIZE)
        except pygame.error as e:
            print(f"Nie można załadować domyślnej czcionki: {e}")
            # Alternatywnie, można spróbować użyć SysFont, jeśli Font(None, ...) zawiedzie
            # self.font = pygame.font.SysFont('arial', FONT_SIZE) # Przykład
            # Lub zakończyć grę, jeśli czcionka jest krytyczna
            raise SystemExit("Nie można zainicjalizować czcionki.") from e


    def increase_score(self, points=1):
        """
        Zwiększa wynik gracza o określoną liczbę punktów.

        Args:
            points (int): Liczba punktów do dodania (domyślnie 1).
        """
        self.score += points

    def get_score(self):
        """
        Zwraca aktualny wynik gracza.

        Returns:
            int: Aktualny wynik.
        """
        return self.score

    def draw(self, surface):
        """
        Rysuje aktualny wynik na podanej powierzchni.

        Args:
            surface (pygame.Surface): Powierzchnia, na której ma być narysowany wynik.
        """
        score_text = f"Wynik: {self.score}"
        # Renderowanie tekstu na powierzchni
        text_surface = self.font.render(score_text, True, SCORE_COLOR)
        # Rysowanie powierzchni z tekstem na głównej powierzchni gry
        surface.blit(text_surface, SCORE_POSITION)