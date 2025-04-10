# Biker Firmware

Firmware dla ESP32 do projektu **Biker**.

## Wymagania

- PlatformIO (https://platformio.org/)

## Budowanie

W katalogu `firmware/` uruchom:

```
pio run
```

## Flashowanie na ESP32

Podłącz ESP32 przez USB i uruchom:

```
pio run --target upload
```

## Monitor portu szeregowego

```
pio device monitor