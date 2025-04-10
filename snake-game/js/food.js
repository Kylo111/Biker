// Logika i stan jedzenia
const Food = {
    position: { x: -1, y: -1 }, // Początkowa pozycja poza planszą
    type: FOOD_TYPE.NORMAL, // Typ aktualnego jedzenia

    // Generowanie nowej, losowej pozycji dla jedzenia
    generatePosition() {
        let newPosition, newType;
        let collisionWithSnake, collisionWithObstacle;

        // Losowanie typu jedzenia
        if (Math.random() < BONUS_APPEARANCE_PROBABILITY) {
            // Losuj typ bonusu (na razie równomiernie)
            const bonusTypes = [FOOD_TYPE.BONUS_SCORE, FOOD_TYPE.BONUS_SPEED_UP, FOOD_TYPE.BONUS_SHRINK];
            newType = bonusTypes[Math.floor(Math.random() * bonusTypes.length)];
        } else {
            newType = FOOD_TYPE.NORMAL;
        }

        do {
            // Losowanie współrzędnych w granicach planszy
            newPosition = {
                x: Math.floor(Math.random() * Board.width),
                y: Math.floor(Math.random() * Board.height)
            };

            // Sprawdź, czy nowa pozycja nie koliduje z ciałem węża
            collisionWithSnake = Snake.body.some(segment =>
                segment.x === newPosition.x && segment.y === newPosition.y
            );

            // Sprawdź, czy nowa pozycja nie koliduje z przeszkodą
            collisionWithObstacle = Board.obstacles.some(obstacle =>
                obstacle.x === newPosition.x && obstacle.y === newPosition.y
            );

        } while (collisionWithSnake || collisionWithObstacle); // Powtarzaj, jeśli jest kolizja z wężem lub przeszkodą

        this.position = newPosition;
        this.type = newType; // Ustaw wylosowany typ
        console.log(`Generated food of type: ${this.type} at (${this.position.x}, ${this.position.y})`);
    },

    // Inicjalizacja (wygenerowanie pierwszej pozycji jedzenia)
    initialize() {
        this.generatePosition();
    },

    // Rysowanie jedzenia (przeniesione do Renderer)
    // Rysowanie jedzenia zostało przeniesione do Renderer.js
    // Ta metoda nie jest już potrzebna tutaj.
    // draw(ctx) { ... }
};