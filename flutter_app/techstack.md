# Stos technologiczny dla aplikacji Flutter (Projekt Biker)

## 1. Platforma i Język

- **Framework:** Flutter SDK (stabilna wersja)
- **Język:** Dart

## 2. Architektura Aplikacji

- **Zarządzanie stanem:** `provider` (zalecany, prosty) lub `flutter_bloc` (bardziej rozbudowany, dla złożonych stanów).
- **Struktura:** Podział na warstwy (np. UI, Business Logic/State Management, Services/Repositories, Models).

## 3. Komunikacja z ESP8266

- **Metoda:** Do ustalenia. Możliwości:
    - **WiFi (HTTP):** Aplikacja Flutter jako klient HTTP, ESP8266 jako serwer HTTP (biblioteka `ESPAsyncWebServer` lub podobna). Użycie biblioteki `http` w Flutterze.
    - **WiFi (WebSockets):** Dwukierunkowa komunikacja w czasie rzeczywistym. Biblioteka `web_socket_channel` w Flutterze, odpowiednia biblioteka WebSocket na ESP8266.
    - **WiFi (MQTT):** Komunikacja przez brokera MQTT. Biblioteka `mqtt_client` w Flutterze, biblioteka `PubSubClient` na ESP8266. Wymaga działającego brokera MQTT (lokalnie lub w chmurze).
    - **ESP-NOW:** Bezpośrednia komunikacja między urządzeniami ESP bez routera. Wymaga odpowiedniej implementacji po obu stronach (może być bardziej złożona).
- **Format danych:** JSON (dla konfiguracji), format binarny lub JSON (dla danych telemetrycznych/debug).

## 4. Interfejs Użytkownika (UI)

- **Widgety:** Flutter Material Widgets (zgodne z Material Design).
- **Responsywność:** Użycie `LayoutBuilder`, `MediaQuery`, elastycznych layoutów (Row, Column, Expanded, Flexible).
- **Wykresy:**
    - `fl_chart`: Popularna i elastyczna biblioteka do wykresów.
    - `syncfusion_flutter_charts`: Bogaty zestaw wykresów od Syncfusion.
- **Nawigacja:** `Navigator` (standardowy), `go_router` (dla bardziej złożonej nawigacji).

## 5. Przechowywanie Danych Lokalnych

- **Proste ustawienia:** `shared_preferences` (odpowiednik SharedPreferences w Androidzie).
- **Strukturalne dane (np. profile):** `sqflite` (odpowiednik Room/SQLite) lub przechowywanie jako pliki JSON.

## 6. Testowanie

- **Testy jednostkowe:** `flutter_test` (pakiet `test`).
- **Testy widgetów:** `flutter_test`.
- **Testy integracyjne:** `flutter_test` (pakiet `integration_test`).
- **Mockowanie:** `mockito` lub `mocktail`.

## 7. Narzędzia Deweloperskie

- **IDE:** VS Code z rozszerzeniami Flutter i Dart lub Android Studio z pluginem Flutter.
- **Debugowanie i Profilowanie:** Flutter DevTools.
- **Zarządzanie zależnościami:** `flutter pub`.
- **Budowanie i dystrybucja:** `flutter build`.