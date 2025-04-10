import pygame, random # Dodano import random
import math
from config import GRID_SIZE, SNAKE_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

class Snake:
    def __init__(self, start_pos_grid):
        """
        Inicjalizuje węża.

        Args:
            start_pos_grid (tuple): Pozycja startowa (x, y) w koordynatach siatki.
        """
        self.grid_size = GRID_SIZE
        start_x = start_pos_grid[0] * self.grid_size
        start_y = start_pos_grid[1] * self.grid_size
        self.segments = [pygame.Rect(start_x, start_y, self.grid_size, self.grid_size)]
        self.direction = pygame.K_RIGHT  # Początkowy kierunek
        self.color = SNAKE_COLOR # Kolor węża
        self.head_image = None # Obrazek głowy
        self.body_image = None # Obrazek ciała
        self.tail_image = None # Obrazek ogona
        self.corner_image = None # Obrazek zakrętu
        self.grow_pending = False # Reset flagi rośnięcia
        self.last_direction = self.direction # Ostatni kierunek (do rysowania)
        self.score = 0 # Wynik gracza
        self.segment_directions = [(1, 0)] # Kierunki segmentów (dla rysowania zakrętów)
        self.eat_effect = None # Efekt zjadania jedzenia
        self.eat_effect_timer = 0 # Timer dla efektu zjadania
        self.eat_sound = None # Dźwięk zjadania jedzenia
        self.move_sound = None # Dźwięk ruchu węża
        self.death_sound = None # Dźwięk śmierci węża

    def update(self):
        """Aktualizuje stan węża."""
        self.move()

    def check_collision(self):
        """
        Sprawdza, czy wąż koliduje ze ścianami lub samym sobą.

        Returns:
            bool: Zawsze False, ponieważ wąż przechodzi przez granice w metodzie move().
        """
        return False
    def grow(self):
        """Zaznacza, że wąż ma urosnąć przy następnym ruchu."""
        self.grow_pending = True
        self.score += 10  # Zwiększenie wyniku

        # Odtwarzanie dźwięku zjadania
        if self.eat_sound:
            self.eat_sound.play()

        # Aktywacja efektu zjadania
        self.eat_effect_timer = 10  # Liczba klatek, przez które efekt będzie widoczny

    def change_direction(self, new_direction):
        """
        Zmienia kierunek ruchu węża, jeśli jest to dozwolone.

        Args:
            new_direction (int): Nowy kierunek (np. pygame.K_UP).
        """
        # Zapobieganie zawracaniu
        if new_direction == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = new_direction
        elif new_direction == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = new_direction
        elif new_direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = new_direction
        elif new_direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = new_direction

    def turn(self, direction_vector):
        """
        Zmienia kierunek ruchu węża na podstawie wektora kierunku.

        Args:
            direction_vector (pygame.Vector2): Wektor kierunku (np. (0, -1) dla ruchu w górę).
        """
        # Konwersja wektora kierunku na klawisze pygame
        if direction_vector == pygame.Vector2(0, -1) and self.direction != pygame.K_DOWN:
            self.direction = pygame.K_UP
        elif direction_vector == pygame.Vector2(0, 1) and self.direction != pygame.K_UP:
            self.direction = pygame.K_DOWN
        elif direction_vector == pygame.Vector2(-1, 0) and self.direction != pygame.K_RIGHT:
            self.direction = pygame.K_LEFT
        elif direction_vector == pygame.Vector2(1, 0) and self.direction != pygame.K_LEFT:
            self.direction = pygame.K_RIGHT

    def draw(self, surface):
        """
        Rysuje węża na podanej powierzchni.

        Args:
            surface (pygame.Surface): Powierzchnia do rysowania.
        """
        if not self.head_image or not self.body_image or not self.tail_image:
            # Rysowanie prostokątów, jeśli obrazki nie są załadowane
            for segment in self.segments:
                pygame.draw.rect(surface, self.color, segment)
            return

        # Rysowanie efektu zjadania jedzenia
        if self.eat_effect_timer > 0 and self.eat_effect:
            # Rysowanie efektu wokół głowy węża
            effect_rect = self.segments[0].inflate(10, 10)  # Powiększony prostokąt głowy
            surface.blit(self.eat_effect, effect_rect)
            self.eat_effect_timer -= 1

        # Rysowanie głowy z odpowiednią rotacją
        head_angle = 0
        if self.last_direction == pygame.K_UP:
            head_angle = 0
        elif self.last_direction == pygame.K_DOWN:
            head_angle = 180
        elif self.last_direction == pygame.K_LEFT:
            head_angle = 90
        elif self.last_direction == pygame.K_RIGHT:
            head_angle = 270

        rotated_head = pygame.transform.rotate(self.head_image, head_angle)
        surface.blit(rotated_head, self.segments[0])

        # Rysowanie ciała z uwzględnieniem zakrętów
        for i in range(1, len(self.segments) - 1):
            # Sprawdzenie, czy jest to zakręt
            if i < len(self.segment_directions):
                current_dir = self.segment_directions[i]
                prev_dir = self.segment_directions[i-1]

                if current_dir != prev_dir and self.corner_image:
                    # To jest zakręt - ustal kąt rotacji
                    angle = self._get_corner_angle(prev_dir, current_dir)
                    rotated_corner = pygame.transform.rotate(self.corner_image, angle)
                    surface.blit(rotated_corner, self.segments[i])
                else:
                    # Zwykły segment ciała
                    angle = self._get_segment_angle(current_dir)
                    rotated_body = pygame.transform.rotate(self.body_image, angle)
                    surface.blit(rotated_body, self.segments[i])
            else:
                # Fallback dla segmentów bez kierunku
                surface.blit(self.body_image, self.segments[i])

        # Rysowanie ogona
        if len(self.segments) > 1:
            tail_idx = len(self.segments) - 1
            if tail_idx < len(self.segment_directions):
                tail_dir = self.segment_directions[tail_idx]
                tail_angle = self._get_segment_angle(tail_dir)
                rotated_tail = pygame.transform.rotate(self.tail_image, tail_angle)
                surface.blit(rotated_tail, self.segments[tail_idx])
            else:
                # Fallback dla ogona bez kierunku
                surface.blit(self.tail_image, self.segments[tail_idx])

    def check_collision(self):
        """
        Sprawdza, czy wąż koliduje ze ścianami lub samym sobą.

        Returns:
            bool: True jeśli wystąpiła kolizja, False w przeciwnym razie.
        """
        return self.check_collision_with_boundary() or self.check_collision_with_self()

    def move(self):
        """Przesuwa węża o jeden krok w aktualnym kierunku. Zwraca pozycję ogona przed ruchem."""
        head = self.segments[0]
        dx, dy = 0, 0

        if self.direction == pygame.K_UP:
            dy = -self.grid_size
            current_dir = (0, -1)
        elif self.direction == pygame.K_DOWN:
            dy = self.grid_size
            current_dir = (0, 1)
        elif self.direction == pygame.K_LEFT:
            dx = -self.grid_size
            current_dir = (-1, 0)
        elif self.direction == pygame.K_RIGHT:
            dx = self.grid_size
            current_dir = (1, 0)

        # Aktualizacja kierunków segmentów
        self.segment_directions.insert(0, current_dir)
        if not self.grow_pending and len(self.segment_directions) > len(self.segments):
            self.segment_directions.pop()

        new_head = head.move(dx, dy) # Nowa pozycja głowy

        # Sprawdzenie i obsługa przejścia przez granice ekranu
        if new_head.left < 0:
            new_head.x = SCREEN_WIDTH - self.grid_size
        elif new_head.right > SCREEN_WIDTH:
            new_head.x = 0
        elif new_head.top < 0:
            new_head.y = SCREEN_HEIGHT - self.grid_size
        elif new_head.bottom > SCREEN_HEIGHT:
            new_head.y = 0

        old_tail_pos = self.segments[-1].copy() if not self.grow_pending else None # Pozycja ogona przed ruchem
        self.segments.insert(0, new_head)

        if not self.grow_pending:
            self.segments.pop() # Usuń ostatni segment, jeśli wąż nie rośnie
        else:
            self.grow_pending = False # Reset flagi rośnięcia

        # Odtwarzanie dźwięku ruchu
        if self.move_sound:
            self.move_sound.play()

        self.last_direction = self.direction # Aktualizacja ostatniego kierunku
        return old_tail_pos # Zwrócenie pozycji starego ogona

    def check_collision_with_self(self):
        """
        Sprawdza, czy wąż koliduje sam ze sobą.

        Returns:
            bool: True jeśli wystąpiła kolizja, False w przeciwnym razie.
        """
        head = self.segments[0]

        # Kolizja z samym sobą
        for segment in self.segments[1:]:
            if head.colliderect(segment):
                if self.death_sound:
                    self.death_sound.play()
                return True
        return False

    def check_collision_with_obstacles(self, obstacles):
        """
        Sprawdza, czy wąż koliduje z przeszkodami.

        Args:
            obstacles (list): Lista przeszkód.

        Returns:
            bool: True jeśli wystąpiła kolizja, False w przeciwnym razie.
        """
        head = self.segments[0]
        head_pos = pygame.Vector2(head.x // self.grid_size, head.y // self.grid_size)

        for obstacle in obstacles:
            if head_pos == obstacle.position:
                if self.death_sound:
                    self.death_sound.play()
                return True
        return False

    def get_head_position(self):
        """
        Zwraca pozycję głowy węża w koordynatach siatki.

        Returns:
            pygame.Vector2: Pozycja głowy w koordynatach siatki.
        """
        head = self.segments[0]
        return pygame.Vector2(head.x // self.grid_size, head.y // self.grid_size)

    def _get_segment_angle(self, direction):
        """
        Zwraca kąt rotacji dla segmentu ciała na podstawie kierunku.

        Args:
            direction (tuple): Kierunek segmentu (dx, dy).

        Returns:
            int: Kąt rotacji w stopniach.
        """
        if direction == (0, -1):  # Góra
            return 0
        elif direction == (0, 1):  # Dół
            return 180
        elif direction == (-1, 0):  # Lewo
            return 90
        elif direction == (1, 0):  # Prawo
            return 270
        return 0  # Domyślny kąt

    def _get_corner_angle(self, prev_dir, current_dir):
        """
        Zwraca kąt rotacji dla zakrętu na podstawie poprzedniego i obecnego kierunku.

        Args:
            prev_dir (tuple): Poprzedni kierunek.
            current_dir (tuple): Obecny kierunek.

        Returns:
            int: Kąt rotacji w stopniach.
        """
        # Mapowanie kombinacji kierunków na kąty
        if prev_dir == (0, -1) and current_dir == (1, 0):  # Góra -> Prawo
            return 0
        elif prev_dir == (0, -1) and current_dir == (-1, 0):  # Góra -> Lewo
            return 90
        elif prev_dir == (0, 1) and current_dir == (1, 0):  # Dół -> Prawo
            return 270
        elif prev_dir == (0, 1) and current_dir == (-1, 0):  # Dół -> Lewo
            return 180
        elif prev_dir == (1, 0) and current_dir == (0, -1):  # Prawo -> Góra
            return 90
        elif prev_dir == (1, 0) and current_dir == (0, 1):  # Prawo -> Dół
            return 0
        elif prev_dir == (-1, 0) and current_dir == (0, -1):  # Lewo -> Góra
            return 180
        elif prev_dir == (-1, 0) and current_dir == (0, 1):  # Lewo -> Dół
            return 270
        return 0  # Domyślny kąt

    @property
    def head_rect(self):
        """Zwraca prostokąt (Rect) głowy węża."""
        return self.segments[0]

    def load_images(self, head_image, body_image):
        """Ładuje obrazki dla głowy i ciała węża."""
        self.head_image = head_image
        self.body_image = body_image

    def load_assets(self, asset_manager):
        """Ładuje zasoby graficzne i dźwiękowe węża z AssetManager."""
        try:
            # Ładowanie grafik
            self.head_image = asset_manager.load_image('snake_head.png', use_alpha=True)
            self.body_image = asset_manager.load_image('snake_body.png', use_alpha=True)
            self.tail_image = asset_manager.load_image('snake_tail.png', use_alpha=True)
            self.corner_image = asset_manager.load_image('snake_corner.png', use_alpha=True)
            self.eat_effect = asset_manager.load_image('eat_effect.png', use_alpha=True)

            # Ładowanie dźwięków
            self.eat_sound = asset_manager.load_sound('eat.wav')
            self.move_sound = asset_manager.load_sound('move.wav')
            self.death_sound = asset_manager.load_sound('death.wav')
        except Exception as e:
            print(f"Błąd ładowania zasobów węża: {e}")
            # Resetowanie zasobów w przypadku błędu
            self.head_image = None
            self.body_image = None
            self.tail_image = None
            self.corner_image = None
            self.eat_effect = None
            self.eat_sound = None
            self.move_sound = None
            self.death_sound = None
