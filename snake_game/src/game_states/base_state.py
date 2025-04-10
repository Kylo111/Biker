from abc import ABC, abstractmethod

class BaseState(ABC):
    """
    Abstrakcyjna klasa bazowa dla wszystkich stanów gry.
    """
    def __init__(self, game, asset_manager): # Dodano asset_manager
        """
        Inicjalizuje stan, przechowując referencję do głównego obiektu gry i menedżera zasobów.

        Args:
            game: Główny obiekt gry.
            asset_manager (AssetManager): Menedżer zasobów.
        """
        self.game = game
        self.asset_manager = asset_manager # Przechowaj referencję

    @abstractmethod
    def handle_input(self, event):
        """
        Obsługuje wejście użytkownika dla danego stanu.

        Args:
            event: Zdarzenie Pygame.
        """
        pass

    @abstractmethod
    def update(self, dt):
        """
        Aktualizuje logikę stanu.

        Args:
            dt: Czas, który upłynął od ostatniej klatki (delta time).
        """
        pass

    @abstractmethod
    def draw(self, surface):
        """
        Rysuje elementy stanu na podanej powierzchni.

        Args:
            surface: Powierzchnia Pygame do rysowania.
        """
        pass

    def enter_state(self):
        """
        Wywoływana, gdy stan staje się aktywny.
        """
        pass

    def exit_state(self):
        """
        Wywoływana, gdy stan przestaje być aktywny.
        """
        pass