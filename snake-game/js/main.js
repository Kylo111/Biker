// Główny plik aplikacji Snake

// Funkcja inicjalizująca grę (teraz tylko inicjalizuje silnik i UI)
function initializeGame() {
    console.log("Initializing game...");
    GameEngine.initialize(); // Inicjalizuje stan gry i UI
    // Nie inicjujemy już tutaj Snake'a i Food, bo to się dzieje po wyborze poziomu
}

// Funkcja obsługująca zdarzenia klawiatury
function handleKeyDown(event) {
    const key = event.key;

    // Obsługa pauzy (P) - tylko gdy gra jest uruchomiona
    if (key === 'p' || key === 'P') {
        if (GameState.is(GameState.RUNNING)) {
            GameState.setState(GameState.PAUSED);
            // Pętla gry zatrzyma się sama, bo sprawdzamy stan RUNNING
        } else if (GameState.is(GameState.PAUSED)) {
            GameState.setState(GameState.RUNNING);
            // Ponownie uruchamiamy pętlę gry
            GameEngine.run(performance.now());
        }
        return; // Pauza/wznowienie obsłużone
    }

    // Obsługa ruchu węża (klawisze strzałek) - tylko gdy gra jest uruchomiona
    if (GameState.is(GameState.RUNNING)) {
        switch (key) {
            case 'ArrowUp':
                Snake.setDirection(DIRECTIONS.UP);
                break;
            case 'ArrowDown':
                Snake.setDirection(DIRECTIONS.DOWN);
                break;
            case 'ArrowLeft':
                Snake.setDirection(DIRECTIONS.LEFT);
                break;
            case 'ArrowRight':
                Snake.setDirection(DIRECTIONS.RIGHT);
                break;
        }
        // Zapobiegaj domyślnej akcji przewijania strony dla klawiszy strzałek
        if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(key)) {
            event.preventDefault();
        }
    }

    // Obsługa restartu gry po GAME_OVER (np. klawiszem Enter)
    // Zmieniamy to - restart będzie inicjowany przez kliknięcie przycisku poziomu trudności
    // if (GameState.is(GameState.GAME_OVER) && key === 'Enter') {
    //     GameEngine.initialize(); // Restart gry
    // }
}

// Dodaj nasłuchiwanie na zdarzenia klawiatury po załadowaniu DOM
document.addEventListener('DOMContentLoaded', () => {
    initializeGame(); // Inicjalizacja gry

    // Dodaj nasłuchiwanie na zdarzenia klawiatury dla całego dokumentu
    document.addEventListener('keydown', handleKeyDown);
});