import pygame

class GameStateManager:
    """
    Zarządza stanami gry (np. menu, gra, koniec gry).
    """
    def __init__(self, game, asset_manager): # Dodano asset_manager
        """
        Inicjalizuje menedżera stanów.

        Args:
            game: Główny obiekt gry.
            asset_manager (AssetManager): Menedżer zasobów.
        """
        self.game = game
        self.asset_manager = asset_manager # Przechowaj referencję
        self.states = []

    def push_state(self, state):
        """
        Dodaje nowy stan na wierzch stosu i wywołuje jego metodę enter_state.

        Args:
            state: Stan do dodania.
        """
        if self.states:
            self.states[-1].exit_state()  # Wywołaj exit_state dla poprzedniego stanu
        self.states.append(state)
        state.enter_state()

    def pop_state(self):
        """
        Usuwa stan z wierzchołka stosu i wywołuje metodę enter_state dla nowego stanu na wierzchołku.
        """
        if self.states:
            self.states[-1].exit_state()
            self.states.pop()
            if self.states:
                self.states[-1].enter_state()

    def change_state(self, state):
        """
        Usuwa wszystkie stany ze stosu i dodaje nowy stan.

        Args:
            state: Nowy stan do ustawienia.
        """
        while self.states:
            self.states[-1].exit_state()
            self.states.pop()
        self.push_state(state)

    def handle_input(self, event):
        """
        Przekazuje obsługę zdarzeń do bieżącego stanu.

        Args:
            event: Zdarzenie Pygame.
        """
        if self.states:
            self.states[-1].handle_input(event)

    def update(self, dt):
        """
        Aktualizuje bieżący stan.

        Args:
            dt: Czas, który upłynął od ostatniej klatki (delta time).
        """
        if self.states:
            self.states[-1].update(dt)

    def draw(self, surface):
        """
        Rysuje bieżący stan.

        Args:
            surface: Powierzchnia Pygame do rysowania.
        """
        if self.states:
            self.states[-1].draw(surface)