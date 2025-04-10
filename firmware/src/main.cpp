#include <Arduino.h>
// #include <BLEDevice.h> // ESP8266 nie ma BLE
// #include <Preferences.h> // ESP8266 używa EEPROM
#include <EEPROM.h> // Do zapisu ustawień na ESP8266

// PWM Configuration
#define PWM_PIN D1 // Pin for PWM output (np. D1 na NodeMCU) - zmień wg potrzeb
// ESP8266 używa analogWrite, które ma domyślną częstotliwość ok. 1kHz i rozdzielczość 10 bitów (0-1023)
// Można zmienić zakres na 0-255 za pomocą analogWriteRange(255);
// BLEServer *pServer = nullptr; // Usunięto BLE

void receiveConfiguration();   // odbiór konfiguracji (JSON)
void sendTelemetry();          // wysyłanie danych telemetrycznych (binarne)
void debug();                  // debugowanie
void updatePWM(int dutyCycle); // Aktualizacja wypełnienia PWM
void saveSettings();           // zapis ustawień do EEPROM
void loadSettings();           // odczyt ustawień z EEPROM

void setup() {
  Serial.begin(115200);
  Serial.println("Biker firmware start");
// // Inicjalizacja BLE - Usunięto
// BLEDevice::init("BikerESP8266"); // Zmieniono nazwę dla jasności
// pServer = BLEDevice::createServer();
// // Placeholder: konfiguracja GATT serwera, usług i charakterystyk

// Inicjalizacja PWM dla ESP8266
pinMode(PWM_PIN, OUTPUT);
analogWriteRange(255); // Ustaw zakres PWM na 0-255 (zamiast domyślnego 0-1023)
// analogWriteFreq(1000); // Ustaw częstotliwość PWM na 1kHz (domyślnie jest ok. 1kHz)
Serial.println("PWM Initialized");

EEPROM.begin(512); // Zainicjuj EEPROM (rozmiar w bajtach, np. 512)
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
  dutyCycle = constrain(dutyCycle, 0, 255); // Upewnij się, że wartość jest w zakresie 0-255
  analogWrite(PWM_PIN, dutyCycle); // Użyj analogWrite dla ESP8266
  // Serial.print("PWM Duty Cycle: "); Serial.println(dutyCycle); // Opcjonalny debug
}

void saveSettings() {
  // Placeholder: zapis ustawień do EEPROM
  // Przykład: EEPROM.put(adres, wartosc); EEPROM.commit();
}

void loadSettings() {
  // Placeholder: odczyt ustawień z EEPROM
  // Przykład: EEPROM.get(adres, zmienna);
}