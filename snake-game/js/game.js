// Główny silnik gry (pętla gry, zarządzanie)
const GameEngine = {
    lastTimestamp: 0,
    gameInterval: null, // Bazowy interwał dla danego poziomu trudności
    currentInterval: null, // Aktualny interwał (może być zmieniony przez bonus)
    score: 0,
    animationFrameId: null, // ID dla requestAnimationFrame

    // Inicjalizacja silnika gry (wywoływana raz na początku)
    initialize() {
        console.log("Initializing game engine...");
        GameState.initialize(); // Ustawia stan na SELECT_DIFFICULTY
        UIManager.initialize(
            'score',
            'message',
            'difficulty-selection',
            'easyBtn',
            'mediumBtn',
            'hardBtn',
            this.startGame.bind(this) // Przekazanie metody startGame jako callback
        );
        UIManager.reset(); // Resetuje UI do stanu początkowego (pokazuje wybór poziomu)
        this.render(); // Wstępne renderowanie UI

        // Usunięcie nasłuchiwania na Enter do restartu
        document.removeEventListener('keydown', this.handleRestart);
    },

    // Rozpoczęcie nowej gry po wybraniu poziomu trudności
    startGame(difficulty) {
        console.log(`Starting game with difficulty: ${difficulty}`);
        GameState.setDifficulty(difficulty);
        this.gameInterval = DIFFICULTY_SPEEDS[difficulty]; // Ustawienie bazowego interwału
        this.currentInterval = this.gameInterval; // Początkowo aktualny interwał = bazowy

        // Resetowanie stanu gry przed startem
        this.score = 0;
        this.lastTimestamp = 0;
        UIManager.updateScore(this.score);
        GameState.reset(); // Resetuje też stan bonusów
        GameState.setDifficulty(difficulty); // Ustawiamy ponownie po resecie

        // Inicjalizacja komponentów gry
        Board.reset(); // Wyczyść stare przeszkody
        Board.initializeObstacles(difficulty); // Generuj nowe przeszkody
        Snake.initialize();
        Food.initialize(); // Upewnij się, że jedzenie nie pojawia się na wężu ani przeszkodach

        // Ustawienie stanu gry na RUNNING
        GameState.setState(GameState.RUNNING);

        // Anuluj poprzednią pętlę, jeśli istnieje
        if (this.animationFrameId) {
            cancelAnimationFrame(this.animationFrameId);
        }

        // Rozpocznij pętlę gry
        this.run(0); // Przekaż 0 jako początkowy timestamp
        console.log("Game started and running.");
    },

    // Główna pętla gry
    run(timestamp) {
        // Sprawdź, czy bonus prędkości wygasł
        if (GameState.isSpeedBoostActive && timestamp >= GameState.speedBoostEndTime) {
            GameState.isSpeedBoostActive = false;
            this.currentInterval = this.gameInterval; // Przywróć normalną prędkość
            console.log("Speed boost expired.");
            // Można dodać aktualizację UI, jeśli jest potrzebna
            UIManager.hideBonusMessage();
        }

        // Oblicz czas od ostatniej aktualizacji logiki
        const timeSinceLastUpdate = timestamp - this.lastTimestamp;

        // Główna logika pętli w zależności od stanu
        switch (GameState.currentState) {
            case GameState.RUNNING:
                // Sprawdź, czy minął wystarczający czas na kolejny krok (używamy currentInterval)
                if (timeSinceLastUpdate >= this.currentInterval) {
                    // Zapisz dokładny czas tej aktualizacji, aby uniknąć dryfu
                    // this.lastTimestamp = timestamp;
                    // Lub lepiej, aby zachować stały rytm:
                    this.lastTimestamp = this.lastTimestamp + this.currentInterval;
                    // Jeśli gra mocno laguje, można wrócić do this.lastTimestamp = timestamp;
                    // ale to może powodować nierównomierne tempo gry.

                    this.update(timestamp); // Przekaż timestamp do update
                }
                this.render(); // Rysuj stan gry
                break;
            case GameState.GAME_OVER:
            case GameState.PAUSED:
            case GameState.SELECT_DIFFICULTY:
                // W tych stanach tylko renderujemy UI i czekamy na akcję użytkownika
                this.render();
                // Nie planujemy kolejnej klatki, pętla jest wstrzymana
                console.log(`Game loop paused in state: ${GameState.currentState}`);
                return; // Zakończ funkcję run dla tych stanów
            default:
                // Nieznany stan, zatrzymaj pętlę
                console.error(`Unknown game state: ${GameState.currentState}`);
                return;
        }


        // Zaplanuj następną klatkę
        this.animationFrameId = requestAnimationFrame(this.run.bind(this));
    },

    // Aktualizacja stanu gry (wywoływana co określony interwał)
    update(timestamp) { // Odbierz timestamp
        // Przesuń węża
        Snake.move();

        // Sprawdź kolizje
        if (Snake.checkCollision()) {
            GameState.setState(GameState.GAME_OVER);
            console.log("Collision detected - Game Over!");
            return; // Zakończ update w tej klatce
        }

        let ateFood = false; // Flaga, czy zjedzono jedzenie w tej klatce
        let shouldGrow = true; // Czy wąż powinien rosnąć (domyślnie tak po zjedzeniu)

        // Sprawdź, czy wąż zjadł jedzenie
        if (Snake.checkEatFood(Food.position)) {
            ateFood = true;
            this.score++; // Zawsze +1 punkt za zjedzenie czegokolwiek

            // Sprawdź typ jedzenia i zastosuj efekt
            switch (Food.type) {
                case FOOD_TYPE.NORMAL:
                    console.log("Ate NORMAL food.");
                    // shouldGrow = true; (już jest true)
                    break;
                case FOOD_TYPE.BONUS_SCORE:
                    this.score += BONUS_SCORE_POINTS;
                    console.log(`Ate BONUS_SCORE! +${BONUS_SCORE_POINTS} points.`);
                    // shouldGrow = true;
                    break;
                case FOOD_TYPE.BONUS_SPEED_UP:
                    console.log("Ate BONUS_SPEED_UP!");
                    if (!GameState.isSpeedBoostActive) { // Aktywuj tylko, jeśli nie jest już aktywny
                        GameState.isSpeedBoostActive = true;
                        this.currentInterval = this.gameInterval * BONUS_SPEED_FACTOR; // Zmniejsz interwał (przyspiesz)
                        console.log(`Speed boost activated! New interval: ${this.currentInterval}ms`);
                        UIManager.showBonusMessage(`Speed Boost! (${BONUS_SPEED_DURATION / 1000}s)`);
                    }
                    // Zawsze odnawiaj czas trwania, nawet jeśli już był aktywny
                    GameState.speedBoostEndTime = timestamp + BONUS_SPEED_DURATION;
                    console.log(`Speed boost ends at: ${GameState.speedBoostEndTime}`);
                    // shouldGrow = true;
                    break;
                case FOOD_TYPE.BONUS_SHRINK:
                    console.log("Ate BONUS_SHRINK!");
                    Snake.shrink(BONUS_SHRINK_AMOUNT);
                    shouldGrow = false; // Nie rośnij po zjedzeniu tego bonusa
                    break;
            }

            UIManager.updateScore(this.score);
            Food.generatePosition(); // Wygeneruj nowe jedzenie po zjedzeniu
        }

        // Usuń ogon, jeśli nie zjedzono jedzenia LUB zjedzono bonus skracający
        if (!ateFood || !shouldGrow) {
            Snake.body.pop();
        }
    },

    // Rysowanie stanu gry
    render() {
        const gameData = {
            snake: Snake,
            food: Food,
            obstacles: Board.obstacles, // Dodajemy przeszkody do danych renderowania
            state: GameState.currentState, // Przekazujemy aktualny stan
            score: this.score,
            difficulty: GameState.difficultyLevel, // Przekazujemy poziom trudności
            isSpeedBoostActive: GameState.isSpeedBoostActive, // Przekazujemy stan bonusu prędkości
            speedBoostEndTime: GameState.speedBoostEndTime // Przekazujemy czas końca bonusu
        };
        Renderer.render(gameData);

        // Rysowanie komunikatów na canvas jest teraz obsługiwane przez UIManager
        // Można usunąć Renderer.drawGameOverMessage() i Renderer.drawPausedMessage()
        // jeśli UIManager.updateGameState() odpowiednio zarządza elementem #message
    },

    // Usunięto handleRestart, ponieważ restart jest inicjowany przez wybór poziomu
};

// Inicjalizacja gry może być wywołana w main.js po załadowaniu DOM
// GameEngine.initialize();