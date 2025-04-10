// Zarządzanie stanem gry
const GameState = {
    // Możliwe stany gry
    SELECT_DIFFICULTY: 'SELECT_DIFFICULTY', // Nowy stan wyboru poziomu
    RUNNING: 'RUNNING',
    PAUSED: 'PAUSED',
    GAME_OVER: 'GAME_OVER',

    // Aktualny stan gry
    currentState: null,
    difficultyLevel: null, // Dodana właściwość do przechowywania poziomu trudności
    isSpeedBoostActive: false, // Czy bonus prędkości jest aktywny?
    speedBoostEndTime: 0, // Kiedy bonus prędkości wygasa (timestamp)

    // Metoda do ustawiania stanu gry
    setState(newState) {
        this.currentState = newState;
        // Tutaj można dodać logikę do aktualizacji UI w zależności od stanu
        // np. wyświetlanie komunikatu "Game Over" lub "Paused"
        UIManager.updateGameState(this.currentState);
    },

    // Metoda do sprawdzania, czy gra jest w danym stanie
    is(state) {
        return this.currentState === state;
    },

    // Metoda inicjalizująca stan gry
    initialize() {
        this.setState(GameState.SELECT_DIFFICULTY); // Zaczynamy od wyboru poziomu
        this.difficultyLevel = null;
        this.isSpeedBoostActive = false;
        this.speedBoostEndTime = 0;
    },

    // Metoda do ustawiania poziomu trudności
    setDifficulty(level) {
        if (Object.values(DifficultyLevel).includes(level)) {
            this.difficultyLevel = level;
            console.log(`Difficulty set to: ${level}`);
            // Po wybraniu poziomu, można przejść do stanu RUNNING (zostanie to zrobione w game.js)
        } else {
            console.error(`Invalid difficulty level: ${level}`);
        }
    },

    // Metoda resetująca stan gry (np. po zakończeniu gry)
    reset() {
        // Resetuje również poziom trudności i bonusy
        this.difficultyLevel = null;
        this.isSpeedBoostActive = false;
        this.speedBoostEndTime = 0;
        this.setState(GameState.SELECT_DIFFICULTY); // Wracamy do wyboru poziomu
    }
};

// Inicjalizacja stanu gry przy załadowaniu skryptu (można dostosować)
// GameState.initialize(); // Można wywołać np. po kliknięciu przycisku "Start"