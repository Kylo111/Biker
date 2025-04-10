import pygame
import os

class AssetManager:
    """
    Zarządza ładowaniem i przechowywaniem zasobów gry (obrazy, dźwięki, czcionki).
    """
    def __init__(self):
        """
        Inicjalizuje menedżera zasobów, tworząc puste słowniki na zasoby.
        """
        self.images = {}
        self.sounds = {}
        self.fonts = {}
        # Upewnij się, że ścieżka bazowa jest poprawna względem głównego skryptu
        self.base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) # Przejdź 3 poziomy w górę (src/core -> src -> snake_game)
        self.graphics_path = os.path.join(self.base_path, 'assets', 'graphics')
        self.sounds_path = os.path.join(self.base_path, 'assets', 'sounds')

    def load_image(self, filename, use_alpha=False):
        """
        Ładuje obraz z pliku, przechowuje go w pamięci podręcznej i zwraca.

        Args:
            filename (str): Nazwa pliku obrazu w katalogu 'assets/graphics'.
            use_alpha (bool): Czy obraz powinien obsługiwać przezroczystość.

        Returns:
            pygame.Surface or None: Załadowany obraz lub None w przypadku błędu.
        """
        if filename in self.images:
            return self.images[filename]

        path = os.path.join(self.graphics_path, filename)
        try:
            image = pygame.image.load(path)
            if use_alpha:
                image = image.convert_alpha() # Konwersja z kanałem alfa
            else:
                image = image.convert() # Konwersja bez kanału alfa (szybsza)
            self.images[filename] = image
            print(f"Obraz '{filename}' załadowany pomyślnie z '{path}'.") # Debug print
            return image
        except pygame.error as e:
            print(f"Błąd ładowania obrazu '{filename}' z '{path}': {e}")
            return None
        except FileNotFoundError:
            print(f"Błąd: Nie znaleziono pliku obrazu '{filename}' w '{path}'")
            return None


    def get_image(self, filename):
        """
        Zwraca wcześniej załadowany obraz.

        Args:
            filename (str): Nazwa pliku obrazu.

        Returns:
            pygame.Surface or None: Obraz lub None, jeśli nie został załadowany.
        """
        image = self.images.get(filename)
        if image is None:
             print(f"Ostrzeżenie: Próba pobrania niezaładowanego obrazu '{filename}'.")
        return image

    # --- Metody do zaimplementowania w przyszłości ---

    def load_sound(self, filename):
        """
        Ładuje dźwięk z pliku, przechowuje go w pamięci podręcznej i zwraca.

        Args:
            filename (str): Nazwa pliku dźwiękowego w katalogu 'assets/sounds'.

        Returns:
            pygame.mixer.Sound or None: Załadowany dźwięk lub None w przypadku błędu.
        """
        if filename in self.sounds:
            return self.sounds[filename]

        path = os.path.join(self.sounds_path, filename)
        try:
            sound = pygame.mixer.Sound(path)
            self.sounds[filename] = sound
            print(f"Dźwięk '{filename}' załadowany pomyślnie z '{path}'.")
            return sound
        except pygame.error as e:
            print(f"Błąd ładowania dźwięku '{filename}' z '{path}': {e}")
            return None
        except FileNotFoundError:
            print(f"Błąd: Nie znaleziono pliku dźwiękowego '{filename}' w '{path}'")
            return None

    def get_sound(self, filename):
        """
        Zwraca wcześniej załadowany dźwięk.

        Args:
            filename (str): Nazwa pliku dźwiękowego.

        Returns:
            pygame.mixer.Sound or None: Dźwięk lub None, jeśli nie został załadowany.
        """
        sound = self.sounds.get(filename)
        if sound is None:
            print(f"Ostrzeżenie: Próba pobrania niezaładowanego dźwięku '{filename}'.")
        return sound

    def load_font(self, filename, size):
        """
        Ładuje czcionkę (do implementacji).
        """
        # TODO: Implement font loading
        print(f"Funkcja load_font dla '{filename}' (rozmiar {size}) nie jest jeszcze zaimplementowana.")
        return None

    def get_font(self, filename, size):
        """
        Zwraca załadowaną czcionkę lub ładuje nową, jeśli nie istnieje.

        Args:
            filename (str or None): Ścieżka do pliku czcionki lub None dla domyślnej.
            size (int): Rozmiar czcionki.

        Returns:
            pygame.font.Font: Obiekt czcionki.
        """
        key = (filename, size)
        if key in self.fonts:
            return self.fonts[key]
        try:
            font = pygame.font.Font(filename, size)
            self.fonts[key] = font
            return font
        except Exception as e:
            print(f"Błąd ładowania czcionki '{filename}': {e}")
            # Fallback do domyślnej czcionki pygame
            font = pygame.font.Font(None, size)
            self.fonts[key] = font
            return font