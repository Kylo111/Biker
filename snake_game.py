import pygame
import sys
import random

# Inicjalizacja pygame
pygame.init()
pygame.mixer.init()

# Załaduj dźwięki (upewnij się, że pliki są w tym samym katalogu co gra)
try:
    eat_sound = pygame.mixer.Sound("eat_sound.wav")
except:
    eat_sound = None
try:
    bonus_sound = pygame.mixer.Sound("bonus_sound.wav")
except:
    bonus_sound = None

# Ustawienia okna
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zaawansowany Wąż")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24, bold=True)
big_font = pygame.font.SysFont("Arial", 48, bold=True)

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (160, 32, 240)
BG_COLOR = (30, 30, 30)

# Funkcje pomocnicze
def draw_text(text, font, color, surface, x, y, center=True):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    if center:
        textrect.center = (x, y)
    else:
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def random_position():
    return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (WIDTH, y))

# Klasy gry
class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)

        if new_head in self.positions:
            return False  # Kolizja z samym sobą

        self.positions.insert(0, new_head)
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False
        return True

    def change_direction(self, new_dir):
        # Nie pozwól na obrót o 180 stopni
        if (new_dir[0] * -1, new_dir[1] * -1) == self.direction:
            return
        self.direction = new_dir

    def draw(self):
        for idx, pos in enumerate(self.positions):
            x = pos[0] * CELL_SIZE
            y = pos[1] * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            # Gradient imitowany przez dwa nakładające się prostokąty
            base_color = (0, 200, 0) if idx == 0 else (0, 255, 0)  # głowa ciemniejsza
            highlight_color = (100, 255, 100) if idx == 0 else (150, 255, 150)
            pygame.draw.rect(screen, base_color, rect, border_radius=6)
            inner_rect = rect.inflate(-4, -4)
            pygame.draw.rect(screen, highlight_color, inner_rect, border_radius=4)
            # Obramowanie
            pygame.draw.rect(screen, DARK_GREEN, rect, 2, border_radius=6)

class Food:
    def __init__(self, snake, obstacles):
        self.position = self.randomize(snake, obstacles)
        self.color = RED

    def randomize(self, snake, obstacles):
        while True:
            pos = random_position()
            if pos not in snake.positions and pos not in [o.position for o in obstacles]:
                return pos

    def draw(self):
        rect = pygame.Rect(self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        # Gradient imitowany
        base_color = self.color
        highlight_color = tuple(min(255, c + 80) for c in self.color)
        pygame.draw.rect(screen, base_color, rect, border_radius=6)
        inner_rect = rect.inflate(-4, -4)
        pygame.draw.rect(screen, highlight_color, inner_rect, border_radius=4)
        pygame.draw.rect(screen, WHITE, rect, 2, border_radius=6)

class Bonus:
    def __init__(self, snake, obstacles):
        self.position = self.randomize(snake, obstacles)
        self.color = YELLOW
        self.timer = 300  # czas trwania bonusu

    def randomize(self, snake, obstacles):
        while True:
            pos = random_position()
            if pos not in snake.positions and pos not in [o.position for o in obstacles]:
                return pos

    def draw(self):
        rect = pygame.Rect(self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        base_color = self.color
        highlight_color = tuple(min(255, c + 80) for c in self.color)
        pygame.draw.rect(screen, base_color, rect, border_radius=6)
        inner_rect = rect.inflate(-4, -4)
        pygame.draw.rect(screen, highlight_color, inner_rect, border_radius=4)
        pygame.draw.rect(screen, WHITE, rect, 2, border_radius=6)

class Obstacle:
    def __init__(self, snake):
        self.position = self.randomize(snake)
        self.color = BLUE

    def randomize(self, snake):
        while True:
            pos = random_position()
            if pos not in snake.positions:
                return pos

    def draw(self):
        rect = pygame.Rect(self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        base_color = self.color
        highlight_color = tuple(min(255, c + 80) for c in self.color)
        pygame.draw.rect(screen, base_color, rect, border_radius=6)
        inner_rect = rect.inflate(-4, -4)
        pygame.draw.rect(screen, highlight_color, inner_rect, border_radius=4)
        pygame.draw.rect(screen, WHITE, rect, 2, border_radius=6)

# Ekran startowy
def start_screen():
    while True:
        screen.fill(BG_COLOR)
        draw_text("WĄŻ", big_font, PURPLE, screen, WIDTH//2, HEIGHT//3)
        draw_text("Naciśnij SPACJĘ, aby rozpocząć", font, WHITE, screen, WIDTH//2, HEIGHT//2)
        draw_text("Sterowanie: Strzałki", font, WHITE, screen, WIDTH//2, HEIGHT//2 + 40)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

# Ekran końcowy
def game_over_screen(score):
    while True:
        screen.fill(BG_COLOR)
        draw_text("KONIEC GRY", big_font, PURPLE, screen, WIDTH//2, HEIGHT//3)
        draw_text(f"Wynik: {score}", font, WHITE, screen, WIDTH//2, HEIGHT//2)
        draw_text("Naciśnij SPACJĘ, aby zagrać ponownie", font, WHITE, screen, WIDTH//2, HEIGHT//2 + 40)
        draw_text("Lub ESC, aby wyjść", font, WHITE, screen, WIDTH//2, HEIGHT//2 + 80)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Główna pętla gry
def main():
    start_screen()
    while True:
        snake = Snake()
        obstacles = [Obstacle(snake) for _ in range(5)]
        food = Food(snake, obstacles)
        bonus = None
        score = 0
        speed = 10
        bonus_timer = 0
        effects = []  # lista aktywnych efektów (x, y, kolor, licznik)

        running = True
        while running:
            clock.tick(speed)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction((1, 0))

            alive = snake.move()
            if not alive:
                break

            # Sprawdzenie kolizji z przeszkodami
            for obstacle in obstacles:
                if snake.positions[0] == obstacle.position:
                    alive = False
                    break
            if not alive:
                break

            # Zjedzenie jedzenia
            if snake.positions[0] == food.position:
                snake.grow = True
                score += 10
                food = Food(snake, obstacles)
                # Dodaj efekt rozbłysku
                effects.append({"pos": snake.positions[0], "color": RED, "timer": 10})
                # Dźwięk
                if eat_sound:
                    eat_sound.play()
                # Dodaj przeszkodę co 3 punkty
                if score % 30 == 0:
                    obstacles.append(Obstacle(snake))
                # Zwiększ prędkość co 50 punktów
                if score % 50 == 0:
                    speed += 1
                # Szansa na pojawienie się bonusu
                if bonus is None and random.random() < 0.3:
                    bonus = Bonus(snake, obstacles)

            # Zjedzenie bonusu
            if bonus and snake.positions[0] == bonus.position:
                snake.grow = True
                score += 30
                # Dodaj efekt rozbłysku
                effects.append({"pos": snake.positions[0], "color": YELLOW, "timer": 15})
                # Dźwięk
                if bonus_sound:
                    bonus_sound.play()
                bonus = None

            # Aktualizacja bonusu
            if bonus:
                bonus.timer -= 1
                if bonus.timer <= 0:
                    bonus = None

            # Rysowanie
            screen.fill(BG_COLOR)
            draw_grid()
            food.draw()
            if bonus:
                bonus.draw()
            for obstacle in obstacles:
                obstacle.draw()
            snake.draw()

            # Rysuj efekty
            for effect in effects:
                x, y = effect["pos"]
                color = effect["color"]
                timer = effect["timer"]
                radius = int(CELL_SIZE * (1 + (10 - timer) / 10))
                center = (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2)
                alpha_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                pygame.draw.circle(alpha_surface, (*color, int(255 * timer / 15)), center, radius)
                screen.blit(alpha_surface, (0, 0))

            # Aktualizuj efekty
            effects[:] = [e for e in effects if e["timer"] > 0]
            for e in effects:
                e["timer"] -= 1

            draw_text(f"Wynik: {score}", font, WHITE, screen, 10, 10, center=False)
            pygame.display.flip()

        again = game_over_screen(score)
        if not again:
            break

if __name__ == "__main__":
    main()