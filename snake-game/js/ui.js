// Zarządzanie interfejsem użytkownika (wynik, menu, komunikaty)
const UIManager = {
    scoreElement: null,
    messageElement: null,
    difficultySelectionElement: null,
    easyBtn: null,
    mediumBtn: null,
    hardBtn: null,
    onDifficultySelect: null, // Callback function
    bonusMessageElement: null, // Element do wyświetlania komunikatów o bonusach

    // Inicjalizacja - pobranie referencji do elementów DOM
    initialize(scoreId, messageId, difficultyContainerId, easyBtnId, mediumBtnId, hardBtnId, onDifficultySelectCallback) {
        this.scoreElement = document.getElementById(scoreId);
        this.messageElement = document.getElementById(messageId);
        this.difficultySelectionElement = document.getElementById(difficultyContainerId);
        this.easyBtn = document.getElementById(easyBtnId);
        this.mediumBtn = document.getElementById(mediumBtnId);
        this.hardBtn = document.getElementById(hardBtnId);
        this.bonusMessageElement = document.getElementById('bonus-message'); // Dodaj ID dla elementu bonusu
        this.onDifficultySelect = onDifficultySelectCallback;

        if (!this.scoreElement) {
            console.error(`Score element with id "${scoreId}" not found.`);
        }
        if (!this.messageElement) {
            console.error(`Message element with id "${messageId}" not found.`);
        }
        if (!this.difficultySelectionElement || !this.easyBtn || !this.mediumBtn || !this.hardBtn) {
            console.error("Difficulty selection elements not found.");
        } else {
            this._setupDifficultyButtons();
        }
        if (!this.bonusMessageElement) {
            console.error("Bonus message element not found.");
        }
        this.hideMessage(); // Ukryj komunikaty na starcie
        this.hideBonusMessage(); // Ukryj komunikaty o bonusach na starcie
        this.showDifficultySelection(); // Pokaż wybór poziomu na starcie
    },

    // Prywatna metoda do ustawienia nasłuchiwaczy dla przycisków poziomu trudności
    _setupDifficultyButtons() {
        this.easyBtn.onclick = () => this.onDifficultySelect(DifficultyLevel.EASY);
        this.mediumBtn.onclick = () => this.onDifficultySelect(DifficultyLevel.MEDIUM);
        this.hardBtn.onclick = () => this.onDifficultySelect(DifficultyLevel.HARD);
    },

    // Aktualizacja wyświetlanego wyniku
    updateScore(score) {
        if (this.scoreElement) {
            this.scoreElement.textContent = score;
        }
    },

    // Wyświetlanie komunikatu
    showMessage(text, type = 'error') { // type może być 'error', 'info', etc.
        if (this.messageElement) {
            this.messageElement.textContent = text;
            this.messageElement.style.color = (type === 'error') ? MESSAGE_COLOR : TEXT_COLOR; // Użyj stałych kolorów
            this.messageElement.style.display = 'block';
        }
    },

    // Ukrywanie komunikatu
    hideMessage() {
        if (this.messageElement) {
            this.messageElement.textContent = '';
            this.messageElement.style.display = 'none';
        }
    },

    // Wyświetlanie komunikatu o bonusie
    showBonusMessage(text) {
        if (this.bonusMessageElement) {
            this.bonusMessageElement.textContent = text;
            this.bonusMessageElement.style.display = 'block';
            this.bonusMessageElement.style.color = 'blue'; // Można dostosować kolor
        }
    },

    // Ukrywanie komunikatu o bonusie
    hideBonusMessage() {
        if (this.bonusMessageElement) {
            this.bonusMessageElement.textContent = '';
            this.bonusMessageElement.style.display = 'none';
        }
    }, // <--- Usuń zbędne nawiasy, dodaj przecinek

    // Wyświetlanie sekcji wyboru poziomu trudności
    showDifficultySelection() {
        if (this.difficultySelectionElement) {
            this.difficultySelectionElement.style.display = 'block';
        }
    },

    // Ukrywanie sekcji wyboru poziomu trudności
    hideDifficultySelection() {
        if (this.difficultySelectionElement) {
            this.difficultySelectionElement.style.display = 'none';
        }
    },

    // Aktualizacja UI w zależności od stanu gry
    updateGameState(state) {
        switch (state) {
            case GameState.SELECT_DIFFICULTY:
                this.hideMessage();
                this.showDifficultySelection();
                break;
            case GameState.RUNNING:
                this.hideMessage();
                this.hideDifficultySelection(); // Ukryj wybór poziomu podczas gry
                break;
            case GameState.PAUSED:
                this.showMessage("Paused", "info");
                break;
            case GameState.GAME_OVER:
                this.showMessage("Game Over! Wybierz poziom, aby zagrać ponownie.");
                this.showDifficultySelection(); // Pokaż wybór poziomu po przegranej
                break;
            default:
                this.hideMessage();
                this.showDifficultySelection(); // Pokaż wybór poziomu w innych stanach (np. początkowym)
                break;
        }
    },

    // Resetowanie UI (np. przy nowej grze)
    reset() {
        this.updateScore(0);
        this.hideMessage();
        this.hideBonusMessage(); // Ukryj komunikaty o bonusach przy resecie
        this.showDifficultySelection(); // Pokaż wybór poziomu przy resecie
    }
};

// Inicjalizacja UIManager po załadowaniu DOM (można przenieść do main.js)
// document.addEventListener('DOMContentLoaded', () => {
//     UIManager.initialize('score', 'message');
// });
// Lepiej zainicjalizować w main.js, aby mieć pewność, że DOM jest gotowy