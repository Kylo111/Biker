# Plan implementacji projektu **Biker**

---

## 1. Podział projektu na komponenty

### 1.1 Firmware ESP32
- Odczyt sygnałów z czujnika PAS i hamulca
- Obliczanie kadencji
- Generowanie sygnału PWM (symulacja manetki)
- BLE GATT Server z charakterystykami:
  - konfiguracja trybów (JSON)
  - dane debug (binarne)
  - kalibracja
- Obsługa wielu trybów pracy i przełączanie
- Zapisywanie ustawień w pamięci nieulotnej (Preferences)
- Debugowanie i wysyłanie danych telemetrycznych

### 1.2 Aplikacja Android
- BLE GATT Client
- Konfiguracja parametrów (magnesy, kadencja, tryby)
- Edycja krzywych dla trybów
- Wizualizacja danych w czasie rzeczywistym
- Kalibracja PAS
- Profile użytkownika (Room)
- UI/UX (Material Design, tryb ciemny/jasny)
- Zarządzanie połączeniem BLE i powiadomieniami

---

## 2. Technologie i biblioteki

### Firmware ESP32
- PlatformIO + Arduino framework
- ESP32 BLE Arduino Library
- SimpleFOC lub ESP32MotorControl
- Preferences
- LEDC Driver (PWM)

### Aplikacja Mobilna (Flutter)
- Flutter SDK + Dart
- Komunikacja: **WiFi** (HTTP REST API + ewentualnie WebSockets dla danych czasu rzeczywistego). Biblioteki: `http`, `web_socket_channel`.
- Zarządzanie stanem: `provider` lub `flutter_bloc`
- UI: Flutter Material Widgets
- Wykresy: `fl_chart` lub `syncfusion_flutter_charts`
- Przechowywanie danych: `shared_preferences`, `sqflite` (odpowiednik Room)

---

## 3. Szczegółowy plan implementacji

### 3.1 Firmware ESP8266

#### Etap 1: Infrastruktura
- Utworzenie projektu PlatformIO
- Konfiguracja BLE GATT Server z charakterystykami
- Placeholdery funkcji

#### Etap 2: Odczyt czujników
- Implementacja odczytu impulsów PAS
- Obsługa czujnika hamulca
- Obliczanie kadencji

#### Etap 3: Generowanie PWM
- Konfiguracja LEDC Driver
- Mapowanie kadencji na PWM wg krzywej
- Filtr RC (opcjonalnie)

#### Etap 4: Tryby pracy
- Struktura danych dla trybów i krzywych
- Przełączanie trybów (podwójne naciśnięcie hamulca)
- Sygnalizacja buzzerem

#### Etap 5: Komunikacja BLE
- Odbiór konfiguracji (JSON)
- Wysyłanie danych debug (binarne)
- Kalibracja

#### Etap 6: Pamięć nieulotna
- Preferences: zapis/odczyt ustawień i krzywych

#### Etap 7: Testy i optymalizacja
- Testy z nRF Connect
- Debugowanie przez BLE
- Optymalizacja czasów reakcji

---

### 3.2 Aplikacja Mobilna (Flutter)

#### Etap 1: Infrastruktura i Komunikacja WiFi
- Utworzenie projektu Flutter (zrobione)
- Dodanie zależności (`http`, `web_socket_channel`, `provider`, `fl_chart`, `shared_preferences`)
- Implementacja podstawowej komunikacji WiFi z ESP8266:
    - Połączenie z siecią WiFi w firmware.
    - Uruchomienie serwera HTTP na ESP8266 (np. `ESPAsyncWebServer`).
    - Implementacja punktów końcowych REST API na ESP8266 (np. `/config` [GET/POST]).
    - Implementacja klienta HTTP w Flutterze (`http`) do wysyłania/odbierania konfiguracji.
    - (Opcjonalnie) Implementacja serwera WebSocket na ESP8266 i klienta w Flutterze (`web_socket_channel`) do danych czasu rzeczywistego.
- Zarządzanie stanem połączenia WiFi w Flutterze.

#### Etap 2: Konfiguracja systemu
- UI do ustawień (magnesy, kadencja, tryby)
- Logika wysyłania konfiguracji do ESP8266
- Zapis/odczyt ustawień lokalnych (`shared_preferences`)

#### Etap 3: Edycja krzywych
- UI do interaktywnej edycji krzywych (np. za pomocą `fl_chart` lub gestów)
- Logika wysyłania definicji krzywych do ESP8266

#### Etap 4: Wizualizacja danych
- UI do wyświetlania wykresów w czasie rzeczywistym (`fl_chart`)
- Odbiór i parsowanie danych telemetrycznych/debug z ESP8266
- Konfiguracja odświeżania i zakresów wykresów

#### Etap 5: Kalibracja PAS
- UI do przeprowadzania procedury kalibracji
- Komunikacja z ESP8266 w celu sterowania kalibracją i odbioru wyników
- Prezentacja wyników (tabela, wykres)

#### Etap 6: Profile użytkownika
- UI do zarządzania profilami (zapisz/załaduj/usuń)
- Logika zapisu/odczytu profili (np. do plików JSON lub bazy `sqflite`)

#### Etap 7: UI/UX
- Dopracowanie interfejsu (Material Design)
- Obsługa trybu ciemnego/jasnego
- Responsywność

#### Etap 8: Testy i optymalizacja
- Testy jednostkowe i widgetów (`flutter_test`)
- Testy integracyjne
- Profilowanie wydajności (DevTools)

---

## 4. Protokół komunikacji (ESP8266 <-> Flutter przez WiFi)

- **Metoda:** HTTP REST API (dla konfiguracji, profili) + WebSockets (dla danych czasu rzeczywistego - debug, telemetria).
- **Format danych:**
    - Konfiguracja/Profile: JSON
    - Dane telemetryczne/debug: JSON (łatwiejsze parsowanie) lub format binarny (bardziej wydajny).
- **Punkty końcowe HTTP REST API (przykładowe):**
    - `GET /config`: Pobranie aktualnej konfiguracji.
    - `POST /config`: Ustawienie nowej konfiguracji (JSON w body).
    - `GET /profiles`: Lista profili.
    - `POST /profiles`: Zapis nowego profilu.
    - `POST /calibrate/start`: Rozpoczęcie kalibracji.
- **Komunikaty WebSocket (przykładowe):**
    - Serwer -> Klient: `{ "type": "telemetry", "cadence": 60, "pwm": 128 }`
    - Serwer -> Klient: `{ "type": "debug", "pas_voltage": 1.5, "pulse": true }`
    - Serwer -> Klient: `{ "type": "calibration_result", ... }`

---

## 5. Narzędzia i testowanie

- **Firmware:**
  - PlatformIO, Monitor portu szeregowego, Narzędzia do testowania HTTP/WebSocket (np. Postman, przeglądarka, klient WebSocket)
- **Flutter:**
  - Flutter SDK, VS Code/Android Studio, `flutter_test`, Flutter DevTools
- **Inne:**  
  - GitHub, README, dokumentacja API BLE, instrukcje użytkownika

---

## 6. Kamienie milowe

| Kamień milowy | Termin | Opis |
| --- | --- | --- |
| Architektura i plan | kwiecień 2025 | Dokumentacja, podział modułów |
| Firmware MVP | maj 2025 | BLE, odczyt PAS, PWM, tryby |
| App MVP | czerwiec 2025 | BLE, konfiguracja, wizualizacja |
| Testy integracyjne | lipiec 2025 | Połączenie firmware + app |
| Optymalizacja | lipiec 2025 | Poprawki, stabilność |
| Wdrożenie | sierpień 2025 | Dokumentacja, release |

---

## 7. Uwagi końcowe

- Priorytet: stabilna i szybka komunikacja WiFi oraz szybka reakcja na zmiany kadencji
- Minimalizacja opóźnień w przesyle danych telemetrycznych/debug przez WebSockets.
- Intuicyjna konfiguracja i edycja krzywych  
- Możliwość rozbudowy o kolejne funkcje (np. OTA, logowanie danych)

---

# Koniec planu