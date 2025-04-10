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

### Aplikacja Android
- Kotlin + MVVM
- Nordic Android BLE Library
- Vico (lub MPAndroidChart)
- Room Database
- Material Design Components
- ConstraintLayout
- SharedPreferences

---

## 3. Szczegółowy plan implementacji

### 3.1 Firmware ESP32

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

### 3.2 Aplikacja Android

#### Etap 1: Infrastruktura
- Utworzenie projektu Android Studio
- Konfiguracja bibliotek (BLE, Vico, Room)
- Architektura MVVM, pakiety

#### Etap 2: Komunikacja BLE
- Skanowanie i łączenie z ESP32
- Obsługa powiadomień i charakterystyk
- Status połączenia

#### Etap 3: Konfiguracja systemu
- Formularze ustawień (magnesy, kadencja, tryby)
- Wysyłanie konfiguracji do ESP32 (JSON)
- Zarządzanie profilami (Room)

#### Etap 4: Edycja krzywych
- Interaktywny edytor krzywych (Vico)
- Wysyłanie krzywych do ESP32
- Zarządzanie trybami

#### Etap 5: Wizualizacja danych
- Odbiór danych debug (binarne)
- Wykresy w czasie rzeczywistym
- Konfiguracja częstotliwości odświeżania

#### Etap 6: Kalibracja PAS
- Procedura kalibracji
- Wizualizacja wyników
- Automatyczne dostosowanie parametrów

#### Etap 7: UI/UX
- Material Design, tryb ciemny/jasny
- Responsywność
- Profile użytkownika

#### Etap 8: Testy i optymalizacja
- Testy jednostkowe (JUnit)
- Testy UI (Espresso)
- Profilowanie wydajności

---

## 4. Protokół komunikacji BLE

- BLE GATT Server (ESP32) i Client (Android)
- Charakterystyki:
  - `config` (JSON, write/read)
  - `debug` (binarne, notify)
  - `calibration` (write/read)
- JSON do konfiguracji i kalibracji
- Binarne dane telemetryczne dla szybkości przesyłu
- Powiadomienia BLE dla danych debug

---

## 5. Narzędzia i testowanie

- **Firmware:**  
  - PlatformIO, nRF Connect, Wireshark  
- **Android:**  
  - Android Studio, JUnit, Espresso, Profiler  
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

- Priorytet: stabilna komunikacja BLE i szybka reakcja na zmiany kadencji  
- Minimalizacja opóźnień w przesyle danych debug  
- Intuicyjna konfiguracja i edycja krzywych  
- Możliwość rozbudowy o kolejne funkcje (np. OTA, logowanie danych)

---

# Koniec planu