#include <Arduino.h>
#include <BLEDevice.h>
#include <Preferences.h>

// Placeholder for motor control library
// #include <SimpleFOC.h> or #include <ESP32MotorControl.h>

BLEServer *pServer = nullptr;

void receiveConfiguration();   // odbiór konfiguracji (JSON)
void sendTelemetry();          // wysyłanie danych telemetrycznych (binarne)
void debug();                  // debugowanie
void controlMotor();           // sterowanie silnikiem
void saveSettings();           // zapis ustawień do pamięci nieulotnej
void loadSettings();           // odczyt ustawień z pamięci nieulotnej

void setup() {
  Serial.begin(115200);
  Serial.println("Biker firmware start");

  // Inicjalizacja BLE
  BLEDevice::init("BikerESP32");
  pServer = BLEDevice::createServer();

  // Placeholder: konfiguracja GATT serwera, usług i charakterystyk
}

void loop() {
  // Placeholder: główna pętla programu
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

void controlMotor() {
  // Placeholder: sterowanie silnikiem (np. SimpleFOC)
}

void saveSettings() {
  // Placeholder: zapis ustawień do pamięci nieulotnej (Preferences)
}

void loadSettings() {
  // Placeholder: odczyt ustawień z pamięci nieulotnej (Preferences)
}