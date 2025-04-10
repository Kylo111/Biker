import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE, FPS, BACKGROUND_COLOR, GRID_WIDTH, GRID_HEIGHT
# Poprawione importy, używając ścieżek względnych z katalogu 'core'
# Usunięto importy Snake, Food, ScoreManager - logika przeniesiona do PlayingState
from src.game_states.state_manager import GameStateManager
from src.game_states.menu_state import MenuState # Stan początkowy
from .asset_manager import AssetManager # Dodano import AssetManager
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.easy_mode = False # Domyślnie tryb normalny
        self.paused = False # Dodano flagę pauzy
        # Usunięto self.running - pętla gry działa, dopóki okno nie zostanie zamknięte

        # Inicjalizacja menedżera zasobów
        self.asset_manager = AssetManager()
        # Inicjalizacja menedżera stanów z przekazaniem asset_manager
        self.state_manager = GameStateManager(self, self.asset_manager)
        # Ustawienie początkowego stanu na MenuState (przekazanie asset_manager)
        # Zakładamy, że konstruktor MenuState i innych stanów zostanie zaktualizowany,
        # aby przyjmować asset_manager. W tym pliku zmieniamy tylko wywołanie.
        self.state_manager.push_state(MenuState(self, self.asset_manager))


    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Zamiast ustawiać flagę, kończymy pętlę bezpośrednio
                # To będzie obsłużone w main.py po wyjściu z game.run()
                return False # Sygnalizuje potrzebę zakończenia pętli w run()
            # Przekaż zdarzenie do bieżącego stanu
            self.state_manager.handle_input(event)
        return True # Sygnalizuje kontynuację pętli

    def _update(self):
        # Oblicz delta time (czas od ostatniej klatki w sekundach)
        dt = self.clock.tick(FPS) / 1000.0
        # Zaktualizuj bieżący stan
        self.state_manager.update(dt)

    def _draw(self):
        # Rysowanie jest teraz obsługiwane przez bieżący stan
        self.state_manager.draw(self.screen)
        # Odświeżenie ekranu pozostaje tutaj, aby było wykonane po narysowaniu stanu
        pygame.display.flip()

    def run(self):
        # Główna pętla gry - działa "nieskończenie", dopóki _handle_events nie zwróci False
        while True:
            if not self._handle_events(): # Obsługa zdarzeń (sprawdza też QUIT)
                break # Zakończ pętlę, jeśli zażądano wyjścia
            self._update()       # Aktualizacja stanu gry
            self._draw()         # Rysowanie
            # self.clock.tick(FPS) jest teraz w _update() do obliczenia dt
        # pygame.quit() zostanie wywołane w main.py po zakończeniu run()