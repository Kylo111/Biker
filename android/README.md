# Biker - Android App Skeleton

## Wymagania
- Android Studio (Arctic Fox lub nowszy)
- Android SDK 24+
- Kotlin 1.9+
- Gradle 8.1+

## Budowanie projektu
1. Otwórz katalog `android/` w Android Studio
2. Poczekaj na synchronizację Gradle
3. Zbuduj projekt (`Build > Make Project` lub `Ctrl+F9`)

## Uruchomienie
- Podłącz urządzenie z Androidem lub uruchom emulator
- Kliknij `Run` lub użyj `Shift+F10`

## Architektura
- MVVM (Model-View-ViewModel)
- Room Database
- BLE (Bluetooth Low Energy) z Nordic Android BLE Library
- Wykresy z Vico (możesz zamienić na MPAndroidChart)

## Struktura pakietów
- `ui` - Aktywności i fragmenty
- `viewmodel` - ViewModel
- `repository` - Repozytorium danych i BLE
- `ble` - Logika BLE
- `model` - Modele danych (Room)

## Status
To jest szkielet projektu z placeholderami. Wymaga implementacji logiki BLE, bazy danych i UI.