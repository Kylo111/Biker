import pygame, sys
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, FONT_PATH, FONT_SIZE, TEXT_COLOR, SNAKE_SPEED
from .base_state import BaseState
from ..game_objects.snake import Snake
from ..game_objects.food import Food
from ..game_objects.obstacle import Obstacle
from .game_over_state import GameOverState
from .pause_state import PauseState # Dodaj import stanu pauzy

class PlayingState(BaseState):
    """
    Reprezentuje stan gry podczas rozgrywki.
    """
    def __init__(self, game, asset_manager):
        super().__init__(game, asset_manager) # Przekazanie asset_manager do konstruktora klasy bazowej
        self.game = game
        self.asset_manager = asset_manager # Przechowaj referencję do asset_manager
        # Usunięto duplikat self.game = game
        from config import GRID_WIDTH, GRID_HEIGHT
        self.snake = Snake((GRID_WIDTH // 2, GRID_HEIGHT // 2))
        self.snake.load_assets(self.asset_manager)
        self.food = Food(self.asset_manager, self.snake.segments) # Przekazanie asset_manager do Food
        self.food.load_assets(self.asset_manager)
        # Dodaj przeszkody tylko jeśli nie jest to tryb łatwy
        self.obstacles = []
        if not self.game.easy_mode:
            for _ in range(3): # Dodaj 3 przeszkody na start
                self.obstacles.append(Obstacle(self.asset_manager, self.snake.segments)) # Przekazanie asset_manager do Obstacle
        self.score = 0 # Inicjalizacja wyniku
        self.score_text = self.asset_manager.get_font(FONT_PATH, FONT_SIZE).render(f"Score: {self.score}", True, TEXT_COLOR) # Inicjalizacja tekstu wyniku
        self.move_timer = 0 # Timer do kontrolowania prędkości węża
        self.obstacle_threshold = 30 # Próg punktowy do dodawania nowych przeszkód
        self.last_obstacle_score = 0 # Ostatni wynik, przy którym dodano przeszkodę


    def handle_input(self, event):
        """
        Obsługuje wejście użytkownika w stanie gry.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.state_manager.push_state(PauseState(self.game, self.asset_manager)) # Przekazanie asset_manager do PauseState
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                self.snake.turn(pygame.Vector2(0, -1)) # Poprawiono kierunek ruchu w górę
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                 self.snake.turn(pygame.Vector2(0, 1)) # Poprawiono kierunek ruchu w dół
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                 self.snake.turn(pygame.Vector2(-1, 0)) # Poprawiono kierunek ruchu w lewo
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                 self.snake.turn(pygame.Vector2(1, 0)) # Poprawiono kierunek ruchu w prawo


    def update(self, dt):
        """
        Aktualizuje stan gry.

        Args:
            dt (float): Czas od ostatniej klatki.
        """
        if not self.game.paused: # Sprawdź czy gra nie jest spauzowana
            # Zwiększamy timer
            self.move_timer += 1

            # Aktualizujemy węża tylko gdy timer osiągnie odpowiednią wartość
            if self.move_timer >= SNAKE_SPEED:
                self.snake.update()
                self.move_timer = 0  # Resetujemy timer

            self.check_collisions()
            if self.snake.check_collision_with_obstacles(self.obstacles) or self.snake.check_collision_with_self():
                self.game.state_manager.push_state(GameOverState(self.game, self.asset_manager, self.snake.score)) # Przekazanie asset_manager do GameOverState


    def draw(self, surface):
        """
        Rysuje stan gry na ekranie.

        Args:
            surface (pygame.Surface): Powierzchnia do rysowania.
        """
        surface.fill((0, 0, 0)) # Czarne tło
        self.snake.draw(surface)
        self.food.draw(surface)
        for obstacle in self.obstacles:
            obstacle.draw(surface)

        # Rysowanie wyniku
        score_text = self.asset_manager.get_font(FONT_PATH, FONT_SIZE).render(f"Score: {self.snake.score}", True, TEXT_COLOR) # Użycie asset_manager do pobrania czcionki i TEXT_COLOR
        surface.blit(score_text, (10, 10))

    def check_collisions(self):
        """
        Sprawdza kolizje węża z jedzeniem i przeszkodami.
        """
        # Kolizja z jedzeniem
        if self.snake.get_head_position() == self.food.position:
            self.snake.grow()
            self.food.spawn(self.snake.segments)

            # Dodawanie przeszkód w zależności od wyniku
            if not self.game.easy_mode:
                # Sprawdzamy, czy przekroczyliśmy próg punktowy od ostatniego dodania przeszkody
                if self.snake.score >= self.last_obstacle_score + self.obstacle_threshold:
                    # Dodaj nową przeszkodę
                    self.obstacles.append(Obstacle(self.asset_manager, self.snake.segments))
                    # Aktualizacja ostatniego wyniku, przy którym dodano przeszkodę
                    self.last_obstacle_score = self.snake.score
                    # Zmniejszamy próg, aby przeszkody pojawiały się częściej w miarę postępu gry
                    if self.obstacle_threshold > 10:  # Minimalny próg to 10 punktów
                        self.obstacle_threshold -= 2

        # Kolizja z przeszkodami
        for obstacle in self.obstacles:
            if self.snake.get_head_position() == obstacle.position:
                self.game.state_manager.push_state(GameOverState(self.game, self.asset_manager, self.snake.score)) # Przekazanie asset_manager do GameOverState
                break # Wyjście z pętli po kolizji