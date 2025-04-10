// Rozmiar planszy (liczba komórek w poziomie i pionie)
const GRID_SIZE = 20;
// Rozmiar pojedynczej komórki w pikselach
const CELL_SIZE = 20;

// Początkowa prędkość gry (klatek na sekundę)
const INITIAL_SPEED = 5;
// O ile zwiększać prędkość po zjedzeniu jedzenia (opcjonalne w tej wersji)
const SPEED_INCREMENT = 0.1;

// Poziomy trudności
const DifficultyLevel = {
    EASY: 'easy',
    MEDIUM: 'medium',
    HARD: 'hard'
};

// Prędkości dla poziomów trudności (interwał w ms)
const DIFFICULTY_SPEEDS = {
    [DifficultyLevel.EASY]: 200,   // 5 FPS
    [DifficultyLevel.MEDIUM]: 125, // 8 FPS
    [DifficultyLevel.HARD]: 80     // 12.5 FPS
};

// Kolory
const BOARD_COLOR = '#fff';
const SNAKE_COLOR = '#333';
const FOOD_COLOR = 'red';
const OBSTACLE_COLOR = 'blue'; // Kolor dla przeszkód

// Kolory bonusów
const BONUS_SCORE_COLOR = 'gold';
const BONUS_SPEED_UP_COLOR = 'cyan';
const BONUS_SHRINK_COLOR = 'purple';

const TEXT_COLOR = '#333';
const MESSAGE_COLOR = 'red';
// Kierunki ruchu (używane w logice węża i obsłudze wejścia)
const DIRECTIONS = {
    UP: { x: 0, y: -1 },
    DOWN: { x: 0, y: 1 },
    LEFT: { x: -1, y: 0 },
    RIGHT: { x: 1, y: 0 }
};

// Typy jedzenia
const FOOD_TYPE = {
    NORMAL: 'normal',
    BONUS_SCORE: 'bonus_score',
    BONUS_SPEED_UP: 'bonus_speed_up',
    BONUS_SHRINK: 'bonus_shrink'
};

// Wartości bonusów
const BONUS_SCORE_POINTS = 5; // Dodatkowe punkty za bonus punktowy (oprócz 1 za zjedzenie)
const BONUS_SPEED_FACTOR = 0.6; // Mnożnik interwału (mniejszy = szybszy)
const BONUS_SPEED_DURATION = 5000; // Czas trwania bonusu prędkości w ms (5 sekund)
const BONUS_SHRINK_AMOUNT = 3; // O ile segmentów skrócić węża

// Prawdopodobieństwa (0 do 1)
const BONUS_APPEARANCE_PROBABILITY = 0.2; // 20% szans na pojawienie się bonusu zamiast normalnego jedzenia