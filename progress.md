# Postęp projektu Biker

---

## Faza 0 - Inicjalizacja projektu

### Firmware ESP32
- Utworzono projekt PlatformIO z BLE GATT Server i placeholderami funkcji
- Usunięto zbędną bibliotekę SimpleFOC
- Dodano podstawową inicjalizację i sterowanie PWM (symulacja manetki)
- Status: **zainicjowano, logika PWM dodana**
- Testy kompilacji: **do wykonania**
### Aplikacja Android
- Utworzono projekt Android Studio z architekturą MVVM i bibliotekami
- Status: **Etap 3.2.1 (Połączenie BLE) - częściowo zaimplementowano**
- Zaimplementowano:
  - Podstawową logikę połączenia i stanu w `BleManager` (Nordic BLE Lib)
  - Obsługę uprawnień i stanu połączenia w `MainActivity`
  - Dodano zależności BLE i testowe do `build.gradle`
  - Dodano uprawnienia do `AndroidManifest.xml`
  - Dodano zasoby stringów
- Testy bazowe:
  - Dodano podstawowy test jednostkowy dla `BleManager` (`BleManagerTest.kt`)
  - Kompilacja projektu: do wykonania w Android Studio / Gradle
  - Test połączenia: do wykonania na urządzeniu/emulatorze po ustawieniu adresu MAC

---

## Podsumowanie

- Faza 0, punkt 1 została rozpoczęta: projekty firmware i app są zainicjowane
- Do wykonania:
  - Kompilacja firmware z logiką PWM (zakończona sukcesem)
  - Kompilacja i uruchomienie aplikacji Android (wymaga synchronizacji Gradle)
  - Implementacja skanowania BLE w aplikacji
  - Implementacja pozostałych etapów zgodnie z planem

---

## Data raportu: 2025-04-10, godz. 23:11