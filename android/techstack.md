# Stos technologiczny dla projektu sterowania silnikiem BLDC roweru

## 1. Kontroler ESP32

### Sprzęt

1. **Mikrokontroler**: ESP32-S3 lub ESP32-WROOM
    - Dwurdzeniowy procesor Xtensa LX7 (ESP32-S3) lub LX6 (ESP32-WROOM) z taktowaniem do 240 MHz[^1][^2]
    - Wbudowana obsługa Wi-Fi i Bluetooth 5 (LE)[^2]
    - Wystarczająca liczba wyprowadzeń GPIO do obsługi czujników i wyjść
2. **Peryferia**:
    - Buzzer (sygnalizacja dźwiękowa zmiany trybu)
    - Wejście dla sygnału z czujnika PAS
    - Wejście dla sygnału z czujnika hamulca (kontaktron)
    - Wyjście PWM do sterowania manetką
3. **Generowanie sygnału PWM**:
    - Wykorzystanie modułu LEDC Driver z ESP32 do generowania sygnału PWM[^8]
    - Opcjonalnie: filtr RC do wygładzenia sygnału PWM na napięcie analogowe
    - Częstotliwość PWM: 1 kHz

### Oprogramowanie

1. **Platforma programistyczna**:
    - Arduino IDE z dodatkiem ESP32[^1]
    - Alternatywnie: PlatformIO dla bardziej zaawansowanego zarządzania projektem
2. **Biblioteki**:
    - ESP32 BLE Arduino Library do komunikacji Bluetooth[^3][^9]
    - ESP32MotorControl lub SimpleFOC do zaawansowanego sterowania silnikiem[^2][^8]
    - Preferences do przechowywania ustawień w pamięci nieulotnej
3. **Protokół komunikacji**:
    - BLE GATT Server do komunikacji z aplikacją Android[^5][^9]
    - Wykorzystanie charakterystyk GATT do przesyłania danych i odbierania konfiguracji

## 2. Aplikacja Android

### Sprzęt

1. **Wymagania minimalne**:
    - System operacyjny: Android 8.0 lub nowszy
    - Obsługa Bluetooth Low Energy
    - RAM: minimum 2 GB

### Oprogramowanie

1. **Język programowania**:
    - Kotlin (zalecany jako standard dla nowych aplikacji Android)[^9]
2. **Architektura aplikacji**:
    - MVVM (Model-View-ViewModel) dla łatwiejszego testowania i separacji logiki
3. **Biblioteki**:
    - **Bluetooth Low Energy**:
        - Nordic Android BLE Library: zaawansowana biblioteka do obsługi BLE[^5][^9]
        - Alternatywnie: RxAndroidBLE do reaktywnej komunikacji Bluetooth[^9]
    - **Wizualizacja danych**:
        - Vico: biblioteka wykresów zoptymalizowana pod kątem aktualizacji w czasie rzeczywistym, aktywnie utrzymywana[^10]
        - Alternatywnie: MPAndroidChart: dojrzała biblioteka do wizualizacji danych z wysoką wydajnością[^6][^10]
    - **UI/UX**:
        - Material Design Components do tworzenia interfejsu zgodnego z wytycznymi Google
        - ConstraintLayout do tworzenia responsywnych układów
4. **Komunikacja z kontrolerem ESP32**:
    - BLE GATT Client do odbierania i wysyłania danych[^9]
    - Obsługa powiadomień BLE do odbierania danych debugowych w czasie rzeczywistym
5. **Przechowywanie danych**:
    - Room Database do przechowywania profili użytkownika i ustawień
    - SharedPreferences do przechowywania prostych ustawień

## 3. Protokół komunikacji między ESP32 a aplikacją Android

1. **Format danych**:
    - JSON do serializacji/deserializacji danych konfiguracyjnych
    - Proste struktury binarne dla danych czasu rzeczywistego (aby zminimalizować obciążenie)
2. **Charakterystyki GATT**:
    - Charakterystyka do odbierania konfiguracji trybów pracy
    - Charakterystyka do przesyłania danych debugowych
    - Charakterystyka do sterowania kalibracją

## 4. Narzędzia deweloperskie

1. **Monitorowanie i testowanie BLE**:
    - nRF Connect do testowania komunikacji BLE[^5]
    - Wireshark z analizatorem Bluetooth do zaawansowanego debugowania
2. **Testowanie aplikacji Android**:
    - JUnit i Espresso do testów jednostkowych i UI
    - Android Studio Profiler do monitorowania wydajności

Powyższy stos technologiczny zapewni solidną podstawę do realizacji projektu, oferując wydajność, niezawodność oraz możliwości rozwoju systemu w przyszłości.

<div>⁂</div>

[^1]: https://www.instructables.com/Wireless-BLDC-Motor-Driver-Using-TMC6200-and-ESP32/

[^2]: https://www.electronics-lab.com/focn-bldc-motor-driver-a-esp32-s3-based-module-that-supports-simplefoc/

[^3]: https://github.com/konsaibakudan/ESP32LEDBluetooth

[^4]: https://bldc-motor.allbestapps.net

[^5]: https://github.com/NordicSemiconductor/Android-BLE-Library

[^6]: https://stackoverflow.com/questions/26467376/android-charting-libraries

[^7]: https://www.electronicsforu.com/electronics-projects/wireless-bldc-motor-control-esp32

[^8]: https://github.com/uLipe/espFoC

[^9]: https://github.com/dotintent/awesome-ble

[^10]: https://www.reddit.com/r/androiddev/comments/189mlv8/as_of_now_what_is_the_best_performed_android/

[^11]: https://www.perplexity.ai/page/2024-ai-showdown-gpt-4o-perple-OU.CI7U_RxKW9NaE3WmEhQ

[^12]: https://www.techrm.com/how-to-control-a-dc-motor-via-esp32-and-bluetooth-with-l298n-on-platformio/

[^13]: https://www.reddit.com/r/esp32/comments/gzabny/whats_your_favorite_motor_control_system_for/

[^14]: https://github.com/usefullcodenet/UcnBrushlessDCMotorPWM

[^15]: https://randomnerdtutorials.com/esp32-ble-server-client/

[^16]: https://kamami.pl/en/brushless-motor-controllers-bldc/1188139-rob-22132-sparkfun-iot-brushless-motor-driver-esp32-wroom-tmc6300-5906623418787.html

[^17]: https://community.simplefoc.com/t/simplefoclibrary-support-for-esp32-boards/61

[^18]: https://randomnerdtutorials.com/esp32-bluetooth-low-energy-ble-arduino-ide/

[^19]: https://community.simplefoc.com/t/controlling-bldc-motor-using-6-mosfets-arduino-esp32/4327

[^20]: https://www.esp32.com/viewtopic.php?t=1200

[^21]: https://forum.arduino.cc/t/esp32-control-bldc/1266716

[^22]: https://www.youtube.com/watch?v=0Yvd_k0hbVs

[^23]: https://www.youtube.com/watch?v=IgbAx9IfV7Q

[^24]: https://github.com/AnyChart/AnyChart-Android

[^25]: https://www.st.com/content/st_com/en/ecosystems/stm32-motor-control-ecosystem.html

[^26]: https://source.android.com/docs/core/connect/bluetooth/ble

[^27]: https://www.scichart.com/android-chart-features/

[^28]: https://www.nxp.com/applications/BRUSHLESS-DC-MOTORS

[^29]: https://developer.android.com/develop/connectivity/bluetooth/ble/ble-overview

[^30]: https://github.com/PhilJay/MPAndroidChart

[^31]: https://www.ti.com/technologies/motor-control.html

[^32]: https://android-arsenal.com/tag/134?sort=name

[^33]: https://www.metabase.com/blog/best-open-source-chart-library

[^34]: https://www.infineon.com/cms/en/product/evaluation-boards/bldc-shield_ifx007t/

[^35]: https://punchthrough.com/android-ble-guide/

[^36]: https://forum.arduino.cc/t/ble-controlling-a-dc-motor-with-esp32-board-and-l293d/559830

[^37]: https://docs.espressif.com/projects/esp-iot-solution/en/latest/motor/bldc/esp_sensorless_bldc_control.html

[^38]: https://components.espressif.com/components/espressif/esp_sensorless_bldc_control

[^39]: https://promwad.com/news/open-source-motor-control

[^40]: https://toshiba.semicon-storage.com/eu/semiconductor/design-development/innovationcentre/articles/tcm0661_MotorStudio.html

[^41]: https://www.reddit.com/r/androiddev/comments/13vxks2/android_ble/

