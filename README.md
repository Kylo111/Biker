# Projekt Biker

System sterowania silnikiem BLDC roweru elektrycznego oparty na ESP8266 i aplikacji Android.

## Opis

Projekt ma na celu stworzenie kontrolera (ESP8266), który odczytuje dane z czujnika PAS (kadencji) i na tej podstawie generuje sygnał PWM symulujący działanie manetki dla oryginalnego sterownika silnika BLDC. Aplikacja na Androida służy do konfiguracji, monitorowania i debugowania systemu.

## Postęp prac

Aktualny status prac nad projektem można śledzić w pliku [progress.md](progress.md).

**Ostatnie zmiany:**
*   Zaimplementowano podstawową logikę połączenia Bluetooth Low Energy (BLE) w aplikacji Android, wykorzystując bibliotekę Nordic Semiconductor.
*   Dodano obsługę uprawnień Bluetooth i lokalizacji w aplikacji Android.
*   Dodano podstawowy test jednostkowy dla menedżera BLE.
*   Zaktualizowano zależności projektu Android.
*   Skonfigurowano podstawowy projekt firmware dla ESP8266 z PlatformIO i dodano logikę sterowania PWM.

## Struktura projektu

*   **android/**: Kod źródłowy aplikacji Android (Kotlin, MVVM, Nordic BLE Lib).
*   **firmware/**: Kod źródłowy dla ESP8266 (PlatformIO, C++).
*   **docs/**: Dokumentacja projektu (np. PRD - na razie w `android/`).
*   **design/**: Pliki projektowe (np. schematy, PCB - na razie puste).
*   **IMPLEMENTATION_PLAN.md**: Szczegółowy plan implementacji.
*   **progress.md**: Raport postępu prac.
*   **.gitignore**: Plik ignorowanych plików dla Git.
*   **README.md**: Ten plik.

## Wymagania

*   **Firmware:** PlatformIO, ESP8266 (NodeMCU ESP-12E).
*   **Aplikacja:** Android Studio, Kotlin, Min SDK 24.

## Uruchomienie

Instrukcje dotyczące budowania i uruchamiania poszczególnych komponentów znajdują się w plikach README w odpowiednich podkatalogach (`firmware/README.md`, `android/README.md`).