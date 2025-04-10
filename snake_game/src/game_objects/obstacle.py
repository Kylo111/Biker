import pygame
import random
from config import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT

class Obstacle:
    def __init__(self, asset_manager, snake_segments):
        """
        Inicjalizuje przeszkodę w losowej pozycji, która nie koliduje z wężem.

        Args:
            asset_manager (AssetManager): Menedżer zasobów.
            snake_segments (list): Lista segmentów węża (pygame.Rect).
        """
        self.asset_manager = asset_manager
        self.grid_size = GRID_SIZE
        self.color = (128, 128, 128)  # Szary kolor przeszkody
        self.image = None  # Możemy dodać obraz przeszkody w przyszłości
        self.position = self._find_valid_position(snake_segments)

    def _find_valid_position(self, snake_segments):
        """
        Znajduje losową pozycję dla przeszkody, która nie koliduje z wężem.

        Args:
            snake_segments (list): Lista segmentów węża (pygame.Rect).

        Returns:
            pygame.Vector2: Pozycja przeszkody w koordynatach siatki.
        """
        snake_positions = [pygame.Vector2(segment.x // self.grid_size, segment.y // self.grid_size) for segment in snake_segments]

        # Próbujemy znaleźć wolną pozycję (maksymalnie 100 prób)
        for _ in range(100):
            # Losowa pozycja
            pos = pygame.Vector2(
                random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1)
            )

            # Sprawdzamy, czy pozycja nie koliduje z wężem
            if pos not in snake_positions:
                return pos

        # Jeśli nie znaleziono wolnej pozycji, zwróć pozycję domyślną
        # (to rzadki przypadek, ale warto mieć fallback)
        return pygame.Vector2(0, 0)

    def draw(self, surface):
        """
        Rysuje przeszkodę na podanej powierzchni.

        Args:
            surface (pygame.Surface): Powierzchnia do rysowania.
        """
        rect = pygame.Rect(self.position.x * self.grid_size, self.position.y * self.grid_size, self.grid_size, self.grid_size)

        if self.image:
            surface.blit(self.image, rect)
        else:
            pygame.draw.rect(surface, self.color, rect)