// Odpowiedzialny za rysowanie na <canvas>
const Renderer = {
    canvas: null,
    ctx: null,

    // Inicjalizacja - pobranie elementu canvas i kontekstu 2D
    initialize(canvasId) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) {
            console.error(`Canvas element with id "${canvasId}" not found.`);
            return false;
        }
        this.ctx = this.canvas.getContext('2d');

        // Ustawienie rozmiaru canvas na podstawie stałych
        this.canvas.width = Board.width * CELL_SIZE;
        this.canvas.height = Board.height * CELL_SIZE;

        return true; // Inicjalizacja pomyślna
    },

    // Czyszczenie całego canvas
    clear() {
        if (!this.ctx) return;
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },

    // Rysowanie tła planszy
    drawBoard() {
        if (!this.ctx) return;
        this.ctx.fillStyle = BOARD_COLOR;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    },

    // Rysowanie węża
    drawSnake(snakeBody, isSpeedBoostActive) { // Dodano isSpeedBoostActive
        if (!this.ctx) return;
        this.ctx.fillStyle = isSpeedBoostActive ? 'orange' : SNAKE_COLOR; // Zmień kolor węża, jeśli bonus prędkości jest aktywny
        snakeBody.forEach(segment => {
            this.ctx.fillRect(segment.x * CELL_SIZE, segment.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
        });
    },

    // Rysowanie jedzenia
    drawFood(food) { // Zmieniono argument na obiekt food
        if (!this.ctx || !food || food.position.x < 0) return; // Nie rysuj, jeśli jedzenie nie istnieje

        // Ustaw kolor w zależności od typu jedzenia
        switch (food.type) {
            case FOOD_TYPE.NORMAL:
                this.ctx.fillStyle = FOOD_COLOR;
                break;
            case FOOD_TYPE.BONUS_SCORE:
                this.ctx.fillStyle = BONUS_SCORE_COLOR; // Kolor dla bonusu punktowego
                break;
            case FOOD_TYPE.BONUS_SPEED_UP:
                this.ctx.fillStyle = BONUS_SPEED_UP_COLOR; // Kolor dla bonusu prędkości
                break;
            case FOOD_TYPE.BONUS_SHRINK:
                this.ctx.fillStyle = BONUS_SHRINK_COLOR; // Kolor dla bonusu skracającego
                break;
            default:
                this.ctx.fillStyle = 'black'; // Domyślny kolor (np. dla błędów)
        }
        this.ctx.fillRect(food.position.x * CELL_SIZE, food.position.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
    },

    // Rysowanie przeszkód
    drawObstacles(obstacles) {
        if (!this.ctx || !obstacles) return;
        this.ctx.fillStyle = OBSTACLE_COLOR; // Użyj koloru przeszkód
        obstacles.forEach(obstacle => {
            this.ctx.fillRect(obstacle.x * CELL_SIZE, obstacle.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
        });
    },

    // Główna metoda renderująca - wywoływana w każdej klatce pętli gry
    render(gameData) {
        if (!this.ctx) return;

        // Wyczyść canvas
        this.clear();

        // Rysuj tło
        this.drawBoard();

        // Rysuj przeszkody
        this.drawObstacles(gameData.obstacles);

        // Rysuj jedzenie
        this.drawFood(gameData.food); // Przekaż cały obiekt food

        // Rysuj węża
        this.drawSnake(gameData.snake.body, gameData.isSpeedBoostActive); // Przekaż stan bonusu prędkości

        // Rysuj komunikaty o stanie gry (np. GAME_OVER, PAUSED)
        // Te komunikaty są teraz obsługiwane przez UIManager, ale zostawiam je na razie
        // jako alternatywę lub do rysowania bezpośrednio na canvasie, jeśli UIManager zawiedzie.
        if (gameData.state === GameState.GAME_OVER) {
            this.drawGameOverMessage(gameData.score); // Przekaż wynik
        } else if (gameData.state === GameState.PAUSED) {
            this.drawPausedMessage();
        }
    },

    // Rysowanie komunikatu Game Over
    drawGameOverMessage(score) { // Dodano argument score
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.7)'; // Półprzezroczyste tło
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.ctx.fillStyle = 'red';
        this.ctx.font = 'bold 40px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('Game Over!', this.canvas.width / 2, this.canvas.height / 2 - 30);

        this.ctx.fillStyle = 'white';
        this.ctx.font = '20px Arial';
        this.ctx.fillText(`Score: ${score}`, this.canvas.width / 2, this.canvas.height / 2 + 10);
        // Usunięto "Press R to play again", bo jest to obsługiwane przez UIManager
    },

    // Rysowanie komunikatu Pauza
    drawPausedMessage() {
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.5)'; // Półprzezroczyste tło
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.ctx.fillStyle = 'white';
        this.ctx.font = '30px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('Paused', this.canvas.width / 2, this.canvas.height / 2);
    }
};