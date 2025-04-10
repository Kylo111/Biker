# Biker - Aplikacja Flutter

Ten katalog zawiera kod źródłowy aplikacji mobilnej dla projektu Biker, napisanej we Flutterze.

## Opis

Aplikacja służy do konfiguracji, monitorowania i debugowania systemu sterowania silnikiem BLDC roweru elektrycznego opartego na ESP8266.

## Wymagania

- Flutter SDK (stabilna wersja)
- Android SDK (dla budowania na Androida)
- Xcode/iOS SDK (dla budowania na iOS)

## Uruchomienie

1.  Upewnij się, że masz zainstalowany Flutter SDK.
2.  Przejdź do katalogu `flutter_app`: `cd flutter_app`
3.  Pobierz zależności: `flutter pub get`
4.  Podłącz urządzenie lub uruchom emulator/symulator.
5.  Uruchom aplikację: `flutter run`

## Status

Projekt został właśnie zainicjowany. Wymaga implementacji logiki komunikacji z ESP8266 (np. przez WiFi/ESP-NOW) oraz interfejsu użytkownika.
