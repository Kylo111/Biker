# Postęp projektu Biker

---

## Faza 0 - Inicjalizacja i Migracja

### Firmware ESP8266
- Utworzono projekt PlatformIO dla NodeMCU ESP-12E.
- Usunięto zbędną bibliotekę SimpleFOC.
- Dodano podstawową inicjalizację i sterowanie PWM (`analogWrite`).
- Status: **Zainicjowano, podstawowa logika PWM działa, kompilacja OK.**

### Aplikacja Mobilna (Migracja do Fluttera)
- **Rozpoczęto migrację z natywnego Androida do Fluttera.**
- Utworzono nowy katalog `flutter_app` i zainicjowano w nim projekt Flutter (`biker_app`).
- Istniejący kod natywny Androida pozostaje w katalogu `android/` jako archiwum.
- Status: **Projekt Flutter zainicjowany.**
- Następne kroki:
    - Aktualizacja dokumentacji (`IMPLEMENTATION_PLAN.md`, `README.md`).
    - Dodanie zależności Fluttera dla komunikacji (np. WiFi, MQTT lub BLE jeśli używany jest zewnętrzny moduł).
    - Implementacja logiki komunikacji we Flutterze.
    - Implementacja UI we Flutterze.

---

## Podsumowanie

- Firmware dla ESP8266 jest gotowy do dalszego rozwoju (odczyt czujników, komunikacja).
- Rozpoczęto migrację aplikacji mobilnej do Fluttera.
- Do wykonania:
    - Aktualizacja dokumentacji pod kątem Fluttera.
    - Implementacja logiki komunikacji i UI w aplikacji Flutter.
    - Implementacja komunikacji między firmware a aplikacją Flutter (np. przez WiFi/ESP-NOW).

---

## Data raportu: 2025-04-11, godz. 00:13