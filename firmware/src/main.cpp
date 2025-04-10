#include <Arduino.h>
#include <BLEDevice.h>
#include <Preferences.h>

// PWM Configuration
#define PWM_PIN 25       // Pin for PWM output (change as needed)
#define PWM_CHANNEL 0    // LEDC channel (0-15)
#define PWM_FREQ 1000    // PWM frequency in Hz (1 kHz)
#define PWM_RESOLUTION 8 // PWM resolution in bits (8 bits = 0-255)
BLEServer *pServer = nullptr;

void receiveConfiguration();   // odbiór konfiguracji (JSON)
void sendTelemetry();          // wysyłanie danych telemetrycznych (binarne)
void debug();                  // debugowanie
void updatePWM(int dutyCycle); // Aktualizacja wypełnienia PWM
void saveSettings();           // zapis ustawień do pamięci nieulotnej
void loadSettings();           // odczyt ustawień z pamięci nieulotnej

void setup() {
  Serial.begin(115200);
  Serial.println("Biker firmware start");
// Inicjalizacja BLE
BLEDevice::init("BikerESP32");
pServer = BLEDevice::createServer();
// Placeholder: konfiguracja GATT serwera, usług i charakterystyk

// Inicjalizacja PWM
ledcSetup(PWM_CHANNEL, PWM_FREQ, PWM_RESOLUTION);
ledcAttachPin(PWM_PIN, PWM_CHANNEL);
Serial.println("PWM Initialized");

loadSettings(); // Załaduj ustawienia przy starcie
}

void loop() {
  // Placeholder: główna pętla programu
  // Na razie ustawiamy stałe wypełnienie PWM dla testu
  updatePWM(128); // Ustaw wypełnienie na 50% (128/255)
  delay(100); // Małe opóźnienie
}

void receiveConfiguration() {
  // Placeholder: odbiór konfiguracji JSON przez BLE
}

void sendTelemetry() {
  // Placeholder: wysyłanie danych telemetrycznych binarnie przez BLE
}

void debug() {
  // Placeholder: funkcje debugujące
}

void updatePWM(int dutyCycle) {
  // Ogranicz wartość dutyCycle do zakresu 0-255
  dutyCycle = constrain(dutyCycle, 0, 255);
  ledcWrite(PWM_CHANNEL, (uint32_t)dutyCycle); // Użyj rzutowania na uint32_t
  // Serial.print("PWM Duty Cycle: "); Serial.println(dutyCycle); // Opcjonalny debug
}

void saveSettings() {
  // Placeholder: zapis ustawień do pamięci nieulotnej (Preferences)
}

void loadSettings() {
  // Placeholder: odczyt ustawień z pamięci nieulotnej (Preferences)
}