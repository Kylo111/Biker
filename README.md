# Projekt Biker

System sterowania silnikiem BLDC roweru elektrycznego oparty na ESP8266 i aplikacji Android.

## Opis

Projekt ma na celu stworzenie kontrolera (ESP8266), który odczytuje dane z czujnika PAS (kadencji) i na tej podstawie generuje sygnał PWM symulujący działanie manetki dla oryginalnego sterownika silnika BLDC. Aplikacja na Androida służy do konfiguracji, monitorowania i debugowania systemu.

## Postęp prac

Aktualny status prac nad projektem można śledzić w pliku [progress.md](progress.md).

**Ostatnie zmiany:**
*   Rozpoczęto migrację aplikacji mobilnej z natywnego Androida do Fluttera.
*   Utworzono nowy projekt Flutter w katalogu `flutter_app`.
*   Zaktualizowano dokumentację (`IMPLEMENTATION_PLAN.md`, `README.md`, `progress.md`) pod kątem Fluttera.
*   Utworzono plik `flutter_app/techstack.md` opisujący stos technologiczny Fluttera.
*   Skonfigurowano podstawowy projekt firmware dla ESP8266 z PlatformIO i dodano logikę sterowania PWM.

## Struktura projektu

*   **flutter_app/**: Kod źródłowy aplikacji mobilnej (Flutter).
*   **android/**: (Archiwalny) Kod źródłowy aplikacji Android (Kotlin, MVVM).
*   **firmware/**: Kod źródłowy dla ESP8266 (PlatformIO, C++).
*   **docs/**: Dokumentacja projektu (np. PRD - na razie w `android/`).
*   **design/**: Pliki projektowe (np. schematy, PCB - na razie puste).
*   **IMPLEMENTATION_PLAN.md**: Szczegółowy plan implementacji (wymaga aktualizacji dla Fluttera).
*   **progress.md**: Raport postępu prac.
*   **.gitignore**: Plik ignorowanych plików dla Git.
*   **README.md**: Ten plik.

## Wymagania

*   **Firmware:** PlatformIO, ESP8266 (NodeMCU ESP-12E).
*   **Aplikacja:** Flutter SDK, Android SDK/iOS SDK.

## Uruchomienie

Instrukcje dotyczące budowania i uruchamiania poszczególnych komponentów znajdują się w plikach README w odpowiednich podkatalogach (`firmware/README.md`, `flutter_app/README.md`).