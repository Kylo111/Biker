# config.py
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINDOW_TITLE = "Zaawansowany Wąż"
FPS = 60

# Prędkość węża (ilość klatek pomiędzy ruchami)
# Im wyższa wartość, tym wolniejszy wąż
SNAKE_SPEED = 10

# Rozmiar siatki i kolory
GRID_SIZE = 20  # Rozmiar pojedynczego kwadratu siatki w pikselach
SNAKE_COLOR = (0, 255, 0)  # Zielony
FOOD_COLOR = (255, 0, 0)  # Czerwony
BACKGROUND_COLOR = (0, 0, 0)  # Czarny

# Obliczone wymiary siatki
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Stałe dla systemu punktacji
SCORE_COLOR = (255, 255, 255) # Biały
FONT_SIZE = 30
SCORE_POSITION = (10, 10) # Pozycja w lewym górnym rogu

# Ścieżka do czcionki systemowej lub None dla domyślnej pygame
FONT_PATH = None

# Kolor tekstu (biały)
TEXT_COLOR = (255, 255, 255)