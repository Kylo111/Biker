import pygame
import os

# Inicjalizacja pygame
pygame.init()

# Rozmiar segmentu węża
GRID_SIZE = 20

# Kolory
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
APPLE_RED = (220, 0, 0)

# Ścieżka do katalogu z grafikami
graphics_path = os.path.dirname(os.path.abspath(__file__))

# Funkcja do tworzenia i zapisywania obrazu
def create_and_save_image(filename, draw_function):
    surface = pygame.Surface((GRID_SIZE, GRID_SIZE), pygame.SRCALPHA)
    draw_function(surface)
    pygame.image.save(surface, os.path.join(graphics_path, filename))
    print(f"Zapisano {filename}")

# Głowa węża
def draw_snake_head(surface):
    # Podstawowy kształt głowy (zielony kwadrat)
    pygame.draw.rect(surface, GREEN, (0, 0, GRID_SIZE, GRID_SIZE))
    # Oczy (czerwone kropki)
    pygame.draw.circle(surface, RED, (GRID_SIZE * 0.7, GRID_SIZE * 0.3), GRID_SIZE * 0.15)
    pygame.draw.circle(surface, RED, (GRID_SIZE * 0.7, GRID_SIZE * 0.7), GRID_SIZE * 0.15)
    # Język (czerwona linia)
    pygame.draw.line(surface, RED, (GRID_SIZE, GRID_SIZE/2), (GRID_SIZE * 1.3, GRID_SIZE/2), 2)

# Ciało węża
def draw_snake_body(surface):
    # Zielony kwadrat z ciemniejszym środkiem
    pygame.draw.rect(surface, GREEN, (0, 0, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(surface, DARK_GREEN, (GRID_SIZE * 0.25, GRID_SIZE * 0.25,
                                         GRID_SIZE * 0.5, GRID_SIZE * 0.5))

# Ogon węża
def draw_snake_tail(surface):
    # Zielony trójkąt
    pygame.draw.rect(surface, GREEN, (0, 0, GRID_SIZE, GRID_SIZE))
    pygame.draw.polygon(surface, DARK_GREEN, [
        (0, 0),
        (0, GRID_SIZE),
        (GRID_SIZE * 0.7, GRID_SIZE/2)
    ])

# Zakręt węża
def draw_snake_corner(surface):
    # Zielony kwadrat z zaokrąglonym rogiem
    pygame.draw.rect(surface, GREEN, (0, 0, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(surface, DARK_GREEN, (GRID_SIZE * 0.25, GRID_SIZE * 0.25,
                                         GRID_SIZE * 0.5, GRID_SIZE * 0.5))
    # Zaokrąglony róg
    pygame.draw.circle(surface, GREEN, (GRID_SIZE * 0.25, GRID_SIZE * 0.25),
                      GRID_SIZE * 0.25)

# Efekt zjadania
def draw_eat_effect(surface):
    # Żółty okrąg z przezroczystością
    surface.fill((0, 0, 0, 0))  # Przezroczyste tło
    pygame.draw.circle(surface, (255, 255, 0, 150),
                      (GRID_SIZE/2, GRID_SIZE/2), GRID_SIZE * 0.7)

# Jedzenie (jabłko)
def draw_food(surface):
    # Czerwone jabłko
    pygame.draw.circle(surface, APPLE_RED, (GRID_SIZE/2, GRID_SIZE/2), GRID_SIZE/2 - 2)
    # Ogonek
    pygame.draw.line(surface, (139, 69, 19), (GRID_SIZE/2, 2), (GRID_SIZE/2, GRID_SIZE/4), 2)
    # Liść
    pygame.draw.ellipse(surface, GREEN, (GRID_SIZE/2 - 3, 1, 6, 4))

# Tworzenie i zapisywanie obrazów
create_and_save_image("snake_head.png", draw_snake_head)
create_and_save_image("snake_body.png", draw_snake_body)
create_and_save_image("snake_tail.png", draw_snake_tail)
create_and_save_image("snake_corner.png", draw_snake_corner)
create_and_save_image("eat_effect.png", draw_eat_effect)
create_and_save_image("food.png", draw_food)

print("Wszystkie grafiki zostały wygenerowane!")
