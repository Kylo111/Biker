// Logika i stan węża
const Snake = {
    body: [], // Tablica segmentów węża, każdy segment to obiekt {x, y}
    direction: null, // Aktualny kierunek ruchu (obiekt z DIRECTIONS)
    nextDirection: null, // Kierunek, który zostanie ustawiony w następnym kroku
    initialLength: 3, // Początkowa długość węża

    // Inicjalizacja węża na środku planszy
    initialize() {
        this.body = [];
        const startX = Math.floor(Board.width / 2);
        const startY = Math.floor(Board.height / 2);

        for (let i = 0; i < this.initialLength; i++) {
            // Początkowe segmenty węża, np. poziomo w lewo od środka
            this.body.push({ x: startX - i, y: startY });
        }

        // Początkowy kierunek ruchu (np. w prawo)
        this.direction = DIRECTIONS.RIGHT;
        this.nextDirection = DIRECTIONS.RIGHT;
    },

    // Zmiana kierunku ruchu (ustawia nextDirection)
    setDirection(newDirection) {
        // Zapobiega ruchowi w przeciwnym kierunku
        if (
            (newDirection === DIRECTIONS.UP && this.direction !== DIRECTIONS.DOWN) ||
            (newDirection === DIRECTIONS.DOWN && this.direction !== DIRECTIONS.UP) ||
            (newDirection === DIRECTIONS.LEFT && this.direction !== DIRECTIONS.RIGHT) ||
            (newDirection === DIRECTIONS.RIGHT && this.direction !== DIRECTIONS.LEFT)
        ) {
            this.nextDirection = newDirection;
        }
    },

    // Aktualizacja pozycji węża
    move() {
        // Ustawienie nowego kierunku, jeśli został zmieniony
        this.direction = this.nextDirection;

        // Obliczenie nowej pozycji głowy
        const head = { ...this.body[0] }; // Kopia głowy
        head.x += this.direction.x;
        head.y += this.direction.y;

        // Dodanie nowej głowy na początek ciała
        this.body.unshift(head);

        // Usunięcie ostatniego segmentu (ogon), chyba że wąż właśnie zjadł jedzenie
        // Logika wzrostu będzie obsługiwana w game.js po sprawdzeniu kolizji z jedzeniem
        // Na razie zawsze usuwamy ogon
        // this.body.pop(); // Zostanie dodane w game.js
    },

    // Wzrost węża (dodanie segmentu w miejscu, gdzie był ogon przed ruchem)
    // Ta metoda jest wywoływana z game.js, gdy wąż zje jedzenie
    grow() {
        // W praktyce, po prostu nie usuwamy ogona w metodzie move(),
        // więc ta metoda może być pusta lub służyć do innych celów związanych ze wzrostem.
        // Alternatywnie, można tu dodać logikę dodawania segmentu, jeśli move() zawsze usuwa ogon.
        // Dla uproszczenia, game.js będzie decydować, czy wywołać pop() w move().
    },

    // Sprawdzenie kolizji
    checkCollision() {
        const head = this.body[0];

        // Kolizja ze ścianami
        if (!Board.isWithinBounds(head)) {
            console.log("Collision detected: Wall", head); // Log
            return true; // Kolizja ze ścianą
        }

        // Kolizja z samym sobą (sprawdzamy od drugiego segmentu)
        for (let i = 1; i < this.body.length; i++) {
            if (head.x === this.body[i].x && head.y === this.body[i].y) {
                console.log("Collision detected: Self", head, "collided with body segment", i, this.body[i]); // Log
                return true; // Kolizja z ciałem
            }
        }

        // Kolizja z przeszkodami
        if (Board.isObstacle(head)) {
            // Loguj pozycję głowy i listę przeszkód dla diagnostyki
            console.log("Collision detected: Obstacle", head); // Log
            console.log("Obstacles list:", Board.obstacles); // Log
            return true; // Kolizja z przeszkodą
        }

        return false; // Brak kolizji
    },

    // Sprawdzenie, czy głowa węża jest na pozycji jedzenia
    checkEatFood(foodPosition) {
        const head = this.body[0];
        return head.x === foodPosition.x && head.y === foodPosition.y;
    },

    // Skrócenie węża
    shrink(amount) {
        if (this.body.length > amount + 1) { // Zostaw co najmniej głowę i jeden segment
            this.body.splice(-amount); // Usuń 'amount' segmentów z końca
            console.log(`Snake shrunk by ${amount} segments.`);
        } else if (this.body.length > 1) { // Jeśli można skrócić, ale nie o pełną kwotę
             const actualAmount = this.body.length - 1; // Skróć do długości 1
             this.body.splice(-actualAmount);
             console.log(`Snake too short to shrink by ${amount}. Shrunk by ${actualAmount}.`);
        } else {
            console.log(`Snake too short to shrink (length 1).`);
        }
    },

    // Rysowanie węża (przeniesione do Renderer)
    draw(ctx) {
        ctx.fillStyle = SNAKE_COLOR;
        this.body.forEach(segment => {
            ctx.fillRect(segment.x * CELL_SIZE, segment.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
            // Opcjonalnie: obramowanie segmentów dla lepszej widoczności
            // ctx.strokeStyle = '#eee';
            // ctx.strokeRect(segment.x * CELL_SIZE, segment.y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
        });
    }
};