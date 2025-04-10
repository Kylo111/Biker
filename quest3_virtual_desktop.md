# Raport: Możliwości dekodowania wideo przez Meta Quest 3 podczas korzystania z Virtual Desktop

---

## Spis treści
1. [Podsumowanie kluczowych wniosków](#podsumowanie-kluczowych-wniosków)
2. [Szczegółowe dane techniczne](#szczegółowe-dane-techniczne)
   - [Obsługiwane kodeki](#obsługiwane-kodeki)
   - [Rekomendowane ustawienia bitrate](#rekomendowane-ustawienia-bitrate)
   - [Rekomendacje ustawień Virtual Desktop](#rekomendacje-ustawień-virtual-desktop)
   - [Ograniczenia sprzętowe i programowe](#ograniczenia-sprzętowe-i-programowe)
3. [Metodologia i ograniczenia badania](#metodologia-i-ograniczenia-badania)
4. [Źródła](#źródła)

---

## Podsumowanie kluczowych wniosków

- **Meta Quest 3 obsługuje sprzętowo i programowo kodeki H.264, H.265 (HEVC) oraz AV1.**
- **AV1 oferuje najwyższą efektywność kompresji, umożliwiając wysoką jakość przy niższym bitrate, ale wymaga nowoczesnych GPU (np. NVIDIA RTX 4000, AMD 7000).**
- **Rekomendowany bitrate dla AV1 to około 150-200 Mbps, z limitem w Virtual Desktop ustawionym na 200 Mbps.**
- **Dla H.264 i H.265 optymalne bitrate to 400-500 Mbps, co zapewnia wysoką jakość, szczególnie w dynamicznych scenach.**
- **Użytkownicy zgłaszają, że AV1 przy wyższych bitrate może powodować mikroprzycięcia, dlatego zaleca się testowanie ustawień indywidualnie.**
- **Kluczowe dla płynności streamingu są: stabilne połączenie Wi-Fi 6/6E, dedykowany router oraz odpowiednia konfiguracja Virtual Desktop.**
- **Głównym ograniczeniem jest wydajność GPU po stronie PC oraz limit bitrate w Virtual Desktop dla AV1.**

---

## Szczegółowe dane techniczne

### Obsługiwane kodeki

| Kodek     | Typ wsparcia          | Charakterystyka                                                                                     | Wymagania sprzętowe                                  |
|------------|-----------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------|
| **AV1**    | Sprzętowe i programowe| Najwyższa efektywność kompresji (~50% lepsza niż H.264), niższy bitrate przy tej samej jakości    | Nowoczesne GPU (RTX 4000, AMD 7000)                  |
| **H.264**  | Sprzętowe i programowe| Szeroka kompatybilność, umiarkowana efektywność kompresji                                         | Większość współczesnych GPU                          |
| **H.265**  | Sprzętowe i programowe| Lepsza kompresja niż H.264, większe wymagania obliczeniowe                                        | Wydajne GPU, może zwiększać opóźnienia               |

---

### Rekomendowane ustawienia bitrate

| Kodek     | Rekomendowany bitrate (Mbps) | Maksymalny bitrate (Mbps) | Uwagi                                                                                   |
|------------|------------------------------|---------------------------|-----------------------------------------------------------------------------------------|
| **AV1**    | 150-200                      | 200                       | Powyżej 200 Mbps mogą wystąpić mikroprzycięcia, limit w Virtual Desktop                 |
| **H.264**  | 400-500                      | ~500                      | Lepsza płynność przy wyższych bitrate, szczególnie w dynamicznych grach                 |
| **H.265**  | 400-500                      | ~500                      | Podobnie jak H.264, ale większe obciążenie CPU/GPU                                     |

---

### Rekomendacje ustawień Virtual Desktop

- **Kodek:** Zalecane jest korzystanie z **AV1** dla najlepszej jakości przy niższym bitrate, jeśli sprzęt na to pozwala.
- **Bitrate:** Ustaw na **200 Mbps** dla AV1 lub **400-500 Mbps** dla H.264/H.265.
- **Tryb transmisji:** Używaj Wi-Fi 6/6E z dedykowanym routerem, najlepiej w trybie Access Point.
- **Testowanie:** Indywidualnie dostosuj ustawienia bitrate i kodeka, obserwując jakość i opóźnienia.
- **Inne ustawienia:** Włącz opcje redukcji opóźnień i optymalizacji dekodowania w Virtual Desktop.

---

### Ograniczenia sprzętowe i programowe

- **GPU:** Starsze karty graficzne mogą nie obsługiwać sprzętowego kodowania AV1, co ogranicza jego użycie.
- **Procesor w Quest 3:** Snapdragon XR2 Gen 2 radzi sobie z dekodowaniem AV1, ale przy bardzo wysokich bitrate mogą wystąpić mikroprzycięcia.
- **Sieć:** Niestabilne połączenie Wi-Fi lub starszy standard (np. Wi-Fi 5) może powodować spadki jakości i opóźnienia.
- **Virtual Desktop:** Limit bitrate dla AV1 wynosi 200 Mbps, co może ograniczać jakość w bardzo dynamicznych scenach.
- **Opóźnienia:** Największy wpływ na opóźnienia ma dekodowanie po stronie Questa, szczególnie przy AV1 i wysokich bitrate.

---

## Metodologia i ograniczenia badania

- **Źródła:** Analiza oparta na oficjalnych dokumentacjach (Meta, NVIDIA), forach technicznych (DCS World, Meta Community), testach użytkowników.
- **Narzędzia:** Wykorzystano Firecrawl Deep Research z iteracyjnym pogłębianiem zapytań.
- **Ograniczenia:** Brak pełnej dokumentacji technicznej od Meta dotyczącej limitów sprzętowych; część danych pochodzi z doświadczeń użytkowników, które mogą się różnić w zależności od konfiguracji sprzętowej i warunków sieciowych.

---

## Źródła

- [NVIDIA Technical Blog](https://developer.nvidia.com/blog/improving-video-quality-and-performance-with-av1-and-nvidia-ada-lovelace-architecture/)
- [DCS World Forum](https://forum.dcs.world/topic/355641-highest-bitrate-with-quest-3-in-virtual-desktop-with-vdxr-runtime-av1/)
- [Meta Community Forums](https://communityforums.atmeta.com/t5/Talk-VR/Meta-Quest-3-bitrate-and-latency-for-PCVR-over-Wi-Fi-6e-Air-Link/td-p/1086684)

---