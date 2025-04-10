// Logika i stan planszy
const Board = {
    // Rozmiar planszy pobierany ze stałych
    width: GRID_SIZE,
    height: GRID_SIZE,
    obstacles: [], // Tablica przechowująca pozycje przeszkód {x, y}

    // Metoda sprawdzająca, czy dana pozycja (x, y) jest w granicach planszy
    isWithinBounds(position) {
        return (
            position.x >= 0 &&
            position.x < this.width &&
            position.y >= 0 &&
            position.y < this.height
        );
    },

    // Inicjalizacja przeszkód w zależności od poziomu trudności
    initializeObstacles(difficulty) {
        this.obstacles = []; // Wyczyść poprzednie przeszkody
        let obstacleCount = 0;

        switch (difficulty) {
            case DifficultyLevel.EASY:
                obstacleCount = 0; // Brak przeszkód na łatwym
                break;
            case DifficultyLevel.MEDIUM:
                obstacleCount = 5; // 5 przeszkód na średnim
                break;
            case DifficultyLevel.HARD:
                obstacleCount = 10; // 10 przeszkód na trudnym
                break;
        }

        // Generuj przeszkody w losowych miejscach, unikając środka planszy (start węża)
        const centerBuffer = 3; // Obszar wokół środka, gdzie nie ma przeszkód
        const startX = Math.floor(this.width / 2);
        const startY = Math.floor(this.height / 2);

        for (let i = 0; i < obstacleCount; i++) {
            let newObstacle;
            let validPosition = false;
            while (!validPosition) {
                newObstacle = {
                    x: Math.floor(Math.random() * this.width),
                    y: Math.floor(Math.random() * this.height)
                };
                // Sprawdź, czy nie jest w obszarze startowym węża
                const isNearCenter = Math.abs(newObstacle.x - startX) < centerBuffer && Math.abs(newObstacle.y - startY) < centerBuffer;
                // Sprawdź, czy nie koliduje z już istniejącymi przeszkodami
                const collidesWithOtherObstacle = this.obstacles.some(obs => obs.x === newObstacle.x && obs.y === newObstacle.y);

                if (!isNearCenter && !collidesWithOtherObstacle) {
                    validPosition = true;
                }
            }
            this.obstacles.push(newObstacle);
        }
        console.log(`Generated ${this.obstacles.length} obstacles for ${difficulty} level.`);
    },

    // Metoda sprawdzająca, czy dana pozycja jest zajęta przez przeszkodę
    isObstacle(position) {
        return this.obstacles.some(obstacle => obstacle.x === position.x && obstacle.y === position.y);
    },

    // Resetowanie planszy (czyszczenie przeszkód)
    reset() {
        this.obstacles = [];
    }

    // Usunięto metodę draw, ponieważ rysowanie odbywa się w Renderer
};