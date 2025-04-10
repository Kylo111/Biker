// Obsługa wejścia (klawiatura)
const InputHandler = {
    // Mapa klawiszy i odpowiadających im kierunków
    keyMap: {
        ArrowUp: DIRECTIONS.UP,
        ArrowDown: DIRECTIONS.DOWN,
        ArrowLeft: DIRECTIONS.LEFT,
        ArrowRight: DIRECTIONS.RIGHT,
        // Alternatywne klawisze (np. WASD)
        KeyW: DIRECTIONS.UP,
        KeyS: DIRECTIONS.DOWN,
        KeyA: DIRECTIONS.LEFT,
        KeyD: DIRECTIONS.RIGHT,
    },

    // Inicjalizacja nasłuchiwania na zdarzenia klawiatury
    initialize() {
        document.addEventListener('keydown', this.handleKeyDown.bind(this));
    },

    // Obsługa zdarzenia naciśnięcia klawisza
    handleKeyDown(event) {
        // Sprawdź, czy gra jest w stanie PAUSED, jeśli tak, nie reaguj na ruch
        if (GameState.currentState === GameState.PAUSED && event.code !== 'KeyP') {
             return;
        }

        // Obsługa pauzy (klawisz P)
        if (event.code === 'KeyP') {
            if (GameState.currentState === GameState.RUNNING) {
                GameState.setState(GameState.PAUSED);
                // Tutaj można dodać logikę wyświetlania komunikatu "Paused"
                UIManager.showMessage("Paused", "info"); // Przykładowe użycie UIManager
            } else if (GameState.currentState === GameState.PAUSED) {
                GameState.setState(GameState.RUNNING);
                 // Tutaj można usunąć komunikat "Paused"
                 UIManager.hideMessage(); // Przykładowe użycie UIManager
                 // Wznowienie pętli gry, jeśli była wstrzymana
                 // (to będzie obsługiwane w głównym pliku game.js)
                 GameLoop.run();
            }
            return; // Zakończ obsługę dla klawisza P
        }


        // Sprawdź, czy naciśnięty klawisz odpowiada któremuś kierunkowi
        const newDirection = this.keyMap[event.code];

        if (newDirection) {
            // Sprawdź, czy nowy kierunek nie jest przeciwny do aktualnego
            // (zapobiega "zawracaniu" węża na siebie)
            const currentDirection = Snake.direction;
            if (
                (newDirection === DIRECTIONS.UP && currentDirection !== DIRECTIONS.DOWN) ||
                (newDirection === DIRECTIONS.DOWN && currentDirection !== DIRECTIONS.UP) ||
                (newDirection === DIRECTIONS.LEFT && currentDirection !== DIRECTIONS.RIGHT) ||
                (newDirection === DIRECTIONS.RIGHT && currentDirection !== DIRECTIONS.LEFT)
            ) {
                // Ustaw nowy kierunek w obiekcie Snake (zostanie zastosowany w następnym kroku gry)
                Snake.nextDirection = newDirection;
            }
        }
    }
};

// Inicjalizacja obsługi wejścia przy załadowaniu skryptu
InputHandler.initialize();