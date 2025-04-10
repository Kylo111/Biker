import pygame
import random
from config import GRID_SIZE, FOOD_COLOR, GRID_WIDTH, GRID_HEIGHT

class Food:
    def __init__(self, asset_manager, occupied_positions): # Dodano asset_manager
        """
        Inicjalizuje obiekt jedzenia.

        Args:
            asset_manager (AssetManager): Menedżer zasobów.
            occupied_positions (list): Lista obiektów pygame.Rect zajętych przez węża.
        """
        self.asset_manager = asset_manager # Przechowaj referencję
        self.grid_size = GRID_SIZE
        self.color = FOOD_COLOR
        self.rect = None  # Zostanie ustawione w randomize_position
        self.position = None  # Pozycja w koordynatach siatki
        self.image = None # Obrazek jedzenia
        self.randomize_position(occupied_positions)

    def randomize_position(self, occupied_positions):
        """
        Umieszcza jedzenie w losowej, wolnej pozycji na siatce.

        Args:
            occupied_positions (list): Lista obiektów pygame.Rect zajętych przez węża.
        """
        while True:
            grid_x = random.randint(0, GRID_WIDTH - 1)
            grid_y = random.randint(0, GRID_HEIGHT - 1)
            x = grid_x * self.grid_size
            y = grid_y * self.grid_size
            potential_rect = pygame.Rect(x, y, self.grid_size, self.grid_size)

            # Sprawdź, czy pozycja nie koliduje z wężem
            collision = False
            for segment in occupied_positions:
                if potential_rect.colliderect(segment):
                    collision = True
                    break

            if not collision:
                self.rect = potential_rect
                self.position = pygame.Vector2(grid_x, grid_y)  # Dodajemy pozycję w koordynatach siatki
                break

    def draw(self, surface):
        """
        Rysuje jedzenie na podanej powierzchni.

        Args:
            surface (pygame.Surface): Powierzchnia do rysowania.
        """
        if self.rect:
            if self.image:
                surface.blit(self.image, self.rect)
            else:
                # Rysowanie prostokąta, jeśli obrazek nie jest załadowany
                pygame.draw.rect(surface, self.color, self.rect)

    def load_image(self, image):
        """Ładuje obrazek dla jedzenia."""
        self.image = image

    def load_assets(self, asset_manager):
        """Ładuje zasoby graficzne jedzenia z AssetManager."""
        try:
            self.image = asset_manager.load_image('food.png', use_alpha=True)
        except Exception:
            self.image = None

    def spawn(self, occupied_positions):
        """Umieszcza jedzenie w nowej losowej pozycji."""
        self.randomize_position(occupied_positions)