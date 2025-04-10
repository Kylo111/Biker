# Dokument Wymagań Produktu (PRD)

## 1. Informacje ogólne

### 1.1 Cel dokumentu

Niniejszy dokument definiuje wymagania dla systemu sterowania silnikiem BLDC roweru elektrycznego, składającego się z dwóch głównych komponentów: kontrolera ESP32 mini oraz aplikacji na urządzenia z systemem Android.

### 1.2 Zakres produktu

System umożliwi sterowanie silnikiem BLDC roweru elektrycznego poprzez kontroler ESP32, który będzie odczytywał dane z czujnika PAS (kadencji) i na tej podstawie generował odpowiedni sygnał dla oryginalnego sterownika silnika.

### 1.3 Definicje i skróty

- **BLDC** - Bezszczotkowy silnik prądu stałego (Brushless Direct Current motor)
- **PAS** - Czujnik asysty pedałowania (Pedal Assist Sensor)
- **ESP32** - Mikrokontroler z wbudowanym modułem Wi-Fi i Bluetooth
- **PWM** - Modulacja szerokości impulsu (Pulse Width Modulation)
- **BLE** - Bluetooth Low Energy

---

## 2. Opis produktu

### 2.1 Przegląd produktu

System składa się z dwóch aplikacji:

1. Kontrolera opartego na ESP32, który odczytuje sygnały z czujnika PAS i generuje odpowiedni sygnał PWM do sterowania silnikiem BLDC.
2. Aplikacji mobilnej na Androida, służącej do konfiguracji, monitorowania i debugowania systemu.

### 2.2 Grupy użytkowników

- Użytkownicy rowerów elektrycznych szukający możliwości dostosowania działania silnika do własnych preferencji
- Hobbyści i entuzjaści majsterkowania przy rowerach elektrycznych
- Inżynierowie i technicy wykonujący modyfikacje w systemach napędowych rowerów elektrycznych


### 2.3 Założenia i ograniczenia

- System będzie współpracował z oryginalnymi sterownikami silników BLDC
- System wykorzystuje istniejący czujnik manetki oraz czujnik PAS
- Kontroler ESP32 wymaga zasilania 5V DC
- Kompatybilność z Android 8.0 i nowszymi wersjami

---

## 3. Wymagania funkcjonalne

### 3.1 Kontroler ESP32 Mini

#### 3.1.1 Odczyt danych z czujnika PAS

- Kontroler musi odczytywać impulsy z czujnika kadencji PAS
- Na podstawie impulsów i zdefiniowanej liczby magnesów kontroler oblicza aktualną kadencję pedałowania
- System musi obsługiwać różne ilości magnesów w czujniku PAS (konfigurowane przez użytkownika)


#### 3.1.2 Generowanie sygnału sterującego

- Kontroler generuje sygnał PWM o częstotliwości 1 kHz symulujący napięcie od 0 do 5V
- Sygnał PWM jest generowany na podstawie aktualnej kadencji i krzywej przypisanej do aktywnego trybu pracy
- W razie potrzeby sygnał PWM może być wygładzony za pomocą filtra RC w celu uzyskania sygnału analogowego


#### 3.1.3 Komunikacja Bluetooth

- Kontroler używa Bluetooth Low Energy (BLE) do komunikacji z aplikacją Android
- Po włączeniu kontroler automatycznie przechodzi w tryb parowania BLE
- Kontroler implementuje BLE GATT Server z charakterystykami do:
    - Wysyłania danych debugowych (kadencja, napięcia)
    - Odbierania konfiguracji trybów pracy
    - Wymiany danych kalibracyjnych


#### 3.1.4 Obsługa trybów pracy

- Kontroler obsługuje wiele trybów pracy (liczba konfigurowana przez użytkownika)
- Każdy tryb ma przypisaną własną krzywą zależności między kadencją a generowanym napięciem
- Przełączanie trybów odbywa się poprzez dwukrotne naciśnięcie hamulca w ciągu 0,5 sekundy
- Aktualny tryb jest sygnalizowany krótkim sygnałem dźwiękowym (liczba beep = numer trybu)


#### 3.1.5 Debugowanie

- W trybie debug kontroler wysyła w czasie rzeczywistym do aplikacji:
    - Napięcie z czujnika PAS
    - Informację o wykryciu impulsu z czujnika PAS
    - Wartość napięcia na wyjściu (kierowanego do manetki)
- Częstotliwość wysyłania danych debugowych jest konfigurowalna (domyślnie 100 ms)


#### 3.1.6 Zarządzanie ustawieniami

- Kontroler zapisuje wszystkie ustawienia w pamięci nieulotnej
- Po ponownym uruchomieniu kontroler przywraca zapisane ustawienia
- Kontroler przechowuje informacje o:
    - Liczbie magnesów w czujniku PAS
    - Maksymalnej kadencji
    - Liczbie trybów
    - Krzywych dla poszczególnych trybów

---

### 3.2 Aplikacja Android

#### 3.2.1 Połączenie Bluetooth

- Aplikacja łączy się z kontrolerem ESP32 poprzez Bluetooth Low Energy (BLE)
- Wskaźnik stanu połączenia (zielona lampka gdy połączenie jest aktywne)
- Możliwość zmiany nazwy podłączonego kontrolera BT


#### 3.2.2 Konfiguracja podstawowa

- Ustawienie liczby magnesów czujnika PAS
- Ustawienie maksymalnej kadencji
- Ustawienie liczby trybów pracy


#### 3.2.3 Edycja krzywych dla trybów pracy

- Interaktywny edytor krzywych zależności między kadencją a napięciem
- Oś X reprezentuje kadencję (od 0 do maksymalnej kadencji)
- Oś Y reprezentuje napięcie (od 0 do 5V)
- Możliwość dodawania, usuwania i przesuwania punktów na krzywej
- Domyślny kształt to linia prosta od lewego dolnego rogu do prawego górnego rogu


#### 3.2.4 Wizualizacja danych w czasie rzeczywistym

- Wyświetlanie wykresów w trybie debug:
    - Napięcie z czujnika PAS
    - Napięcie generowane na wyjściu
    - Kadencja w czasie rzeczywistym
- Możliwość konfiguracji częstotliwości odświeżania danych (domyślnie 100 ms)
- Konfigurowalne zakresy czasowe wykresu (np. 5 sekund, 10 sekund)


#### 3.2.5 Automatyczna kalibracja

- Procedura kalibracji czujnika PAS
- Po uruchomieniu kalibracji ESP32 odczytuje impulsy przy różnych kadencjach
- Wyniki są prezentowane jako tabela i wykres
- Możliwość automatycznego dostosowania parametrów systemu na podstawie wyników kalibracji


#### 3.2.6 Profile użytkownika

- Możliwość zapisywania i ładowania profili zawierających:
    - Liczbę magnesów
    - Maksymalną kadencję
    - Krzywe dla poszczególnych trybów
- Zarządzanie profilami (zapisywanie, ładowanie, usuwanie)


#### 3.2.7 Responsywność i tryb ciemny

- Optymalizacja interfejsu dla różnych rozdzielczości ekranów
- Automatyczne przełączanie między trybem jasnym a ciemnym zgodnie z ustawieniami systemowymi
- Opcja ręcznego wyboru trybu jasnego/ciemnego

---

## 4. Techniczne wymagania

### 4.1 Sprzęt

#### 4.1.1 Kontroler ESP32 Mini

- Mikrokontroler: ESP32-S3 lub ESP32-WROOM
- Wejścia:
    - Czujnik PAS (impulsowy)
    - Czujnik hamulca (kontaktron)
- Wyjścia:
    - PWM (symulujące 0-5V) z opcją filtra RC
    - Buzzer do sygnalizacji dźwiękowej
- Zasilanie: 5V DC


#### 4.1.2 Urządzenia mobilne

- System operacyjny: Android 8.0 lub nowszy
- Obsługa Bluetooth Low Energy
- Minimalne wymagania sprzętowe: 2 GB RAM, procesor ARM64


### 4.2 Oprogramowanie

#### 4.2.1 Kontroler ESP32

- Platforma programistyczna: Arduino IDE z dodatkiem ESP32 lub PlatformIO
- Biblioteki:
    - ESP32 BLE Arduino Library
    - ESP32MotorControl
    - EEPROM lub Preferences do przechowywania ustawień


#### 4.2.2 Aplikacja Android

- Język programowania: Kotlin
- Architektura: MVVM
- Biblioteki:
    - Nordic Android BLE Library lub RxAndroidBLE
    - AnyChart Android Charts do wizualizacji danych
    - Material Design Components
    - ConstraintLayout

---

## 5. Scenariusze użycia

### 5.1 Scenariusz: Pierwsze uruchomienie i konfiguracja

1. Użytkownik podłącza kontroler ESP32 do zasilania
2. Kontroler automatycznie przechodzi w tryb parowania BLE
3. Użytkownik uruchamia aplikację Android i łączy się z kontrolerem
4. Użytkownik wprowadza podstawowe parametry:
    - Liczbę magnesów w czujniku PAS
    - Maksymalną kadencję
    - Liczbę trybów pracy
5. Aplikacja przesyła konfigurację do kontrolera
6. Kontroler zapisuje ustawienia w pamięci nieulotnej

### 5.2 Scenariusz: Edycja krzywej dla trybu pracy

1. Użytkownik wybiera tryb pracy do edycji
2. Aplikacja wyświetla edytor krzywych z aktualną krzywą dla wybranego trybu
3. Użytkownik modyfikuje krzywą, dodając/usuwając/przesuwając punkty
4. Po zakończeniu edycji użytkownik zapisuje krzywą
5. Aplikacja przesyła krzywą do kontrolera
6. Kontroler przypisuje krzywą do wybranego trybu i zapisuje w pamięci

### 5.3 Scenariusz: Kalibracja PAS

1. Użytkownik uruchamia procedurę kalibracji w aplikacji
2. Aplikacja informuje użytkownika o konieczności pedałowania z różnymi prędkościami
3. Kontroler ESP32 zbiera dane z czujnika PAS przez określony czas
4. Po zakończeniu zbierania danych, kontroler przesyła wyniki do aplikacji
5. Aplikacja prezentuje wyniki jako tabelę i wykres
6. Użytkownik może zaakceptować automatyczne dostosowanie parametrów na podstawie wyników kalibracji

### 5.4 Scenariusz: Jazda z użyciem systemu

1. Użytkownik włącza rower i kontroler ESP32
2. Kontroler ładuje zapisane ustawienia i aktywuje ostatnio używany tryb
3. Użytkownik zaczyna pedałować, generując impulsy z czujnika PAS
4. Kontroler ESP32 oblicza aktualną kadencję i na jej podstawie generuje odpowiedni sygnał PWM
5. Sterownik silnika BLDC odbiera sygnał i dostosowuje moc silnika
6. Użytkownik może zmieniać tryby pracy przez dwukrotne naciśnięcie hamulca w ciągu 0,5 sekundy

---

## 6. Interfejs użytkownika

### 6.1 Aplikacja Android - makiety interfejsu

1. Ekran główny:
    - Status połączenia Bluetooth
    - Przyciski wyboru sekcji (Ustawienia, Tryby, Kalibracja, Debug)
    - Informacje o aktualnym trybie pracy
2. Ekran ustawień:
    - Pola do wprowadzenia liczby magnesów, maksymalnej kadencji, liczby trybów
    - Zarządzanie profilami użytkownika (zapisz/załaduj/usuń)
    - Zmiana nazwy kontrolera BT
3. Ekran edycji trybów:
    - Interaktywny edytor krzywych
    - Lista dostępnych trybów
    - Możliwość kopiowania ustawień między trybami
4. Ekran kalibracji:
    - Przycisk rozpoczęcia kalibracji
    - Instrukcje dla użytkownika
    - Wyniki kalibracji (tabela, wykres)
5. Ekran debugowania:
    - Wykresy w czasie rzeczywistym (napięcie PAS, napięcie wyjściowe, kadencja)
    - Suwak do ustawienia częstotliwości odświeżania
    - Wskaźniki stanu (wykrycie impulsu PAS)

---

## 7. Ryzyka i ograniczenia

### 7.1 Ryzyka techniczne

1. Zakłócenia sygnału BLE w środowiskach o dużym natężeniu ruchu radiowego
2. Kompatybilność sygnału PWM z różnymi typami sterowników silników BLDC
3. Dokładność odczytu impulsów z czujników PAS różnych producentów
4. Opóźnienia w komunikacji między kontrolerem a aplikacją przy dużej ilości danych debugowych

### 7.2 Ograniczenia

1. System działa tylko z rowerami wyposażonymi w czujnik PAS i manetkę
2. Wymagane jest zasilanie 5V DC dla kontrolera ESP32
3. Konieczność montażu kontrolera w miejscu dostępnym dla sygnału Bluetooth

---

## 8. Harmonogram realizacji

| Etap | Czas trwania | Termin zakończenia |
| :-- | :-- | :-- |
| Projektowanie systemu | 4 tygodnie | Kwiecień 2025 |
| Implementacja kontrolera ESP32 | 4 tygodnie | Maj 2025 |
| Implementacja aplikacji Android | 6 tygodni | Czerwiec 2025 |
| Testy integracyjne | 2 tygodnie | Lipiec 2025 |
| Optymalizacja i poprawki | 2 tygodnie | Lipiec 2025 |
| Wdrożenie i dokumentacja końcowa | 2 tygodnie | Sierpień 2025 |

---

## 9. Metryki sukcesu

- Czas reakcji systemu na zmiany kadencji: poniżej 100 ms
- Stabilność komunikacji BLE: ponad 99% skutecznych połączeń
- Kompatybilność z co najmniej 90% popularnych sterowników BLDC
- Poprawne działanie aplikacji na 95% urządzeń z systemem Android 8.0 i nowszym
- Pozytywne opinie użytkowników (ponad 90% satysfakcji w testach)

---

## 10. Kryteria akceptacji

Projekt zostanie uznany za zakończony, gdy:

1. Wszystkie wymagania funkcjonalne zostaną zaimplementowane i przetestowane
2. System będzie spełniał wszystkie metryki sukcesu
3. Dokumentacja techniczna i użytkownika zostanie ukończona
4. Stabilność systemu zostanie potwierdzona w testach trwających minimum 100 godzin

---

## 11. Dokumentacja

- Instrukcja użytkownika dla aplikacji Android
- Schemat montażowy kontrolera ESP32
- Dokumentacja techniczna API BLE
- Instrukcja kalibracji i rozwiązywania problemów

