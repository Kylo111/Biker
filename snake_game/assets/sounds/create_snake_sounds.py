import pygame
import numpy as np
import os
import wave
import struct

# Inicjalizacja pygame
pygame.init()
pygame.mixer.init()

# Ścieżka do katalogu z dźwiękami
sounds_path = os.path.dirname(os.path.abspath(__file__))

# Częstotliwość próbkowania
SAMPLE_RATE = 44100

# Funkcja do generowania dźwięku i zapisywania go jako plik WAV
def create_sound(filename, frequency, duration, volume=0.5, fade_out=0.1):
    # Generowanie tablicy czasu
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)

    # Generowanie fali sinusoidalnej
    note = np.sin(frequency * 2 * np.pi * t) * volume

    # Zastosowanie fade-out na końcu dźwięku
    fade_samples = int(SAMPLE_RATE * fade_out)
    if fade_samples > 0:
        fade_curve = np.linspace(1.0, 0.0, fade_samples)
        note[-fade_samples:] *= fade_curve

    # Konwersja do formatu 16-bitowego
    audio = (note * 32767).astype(np.int16)

    # Konwersja do stereo (2 kanały)
    stereo = np.column_stack((audio, audio))  # Duplikacja mono do stereo

    # Zapisanie jako plik WAV
    file_path = os.path.join(sounds_path, filename)

    # Zapisanie jako plik WAV ręcznie
    with wave.open(file_path, 'w') as wav_file:
        # Ustawienie parametrów pliku WAV
        wav_file.setnchannels(2)  # Stereo
        wav_file.setsampwidth(2)  # 2 bajty na próbkę (16-bit)
        wav_file.setframerate(SAMPLE_RATE)

        # Konwersja tablicy NumPy do bajtów
        for sample in stereo:
            wav_file.writeframes(struct.pack('<h', sample[0]))
            wav_file.writeframes(struct.pack('<h', sample[1]))

    print(f"Zapisano {filename}")

# Dźwięk ruchu węża (niski, krótki)
create_sound("move.wav", 150, 0.1, volume=0.2)

# Dźwięk zjadania jedzenia (wyższy, dłuższy)
create_sound("eat.wav", 440, 0.2, volume=0.4)

# Dźwięk śmierci (opadający ton)
def create_death_sound():
    duration = 0.5
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)

    # Opadająca częstotliwość
    freq_start = 880
    freq_end = 110
    freq = np.linspace(freq_start, freq_end, len(t))

    # Generowanie dźwięku z opadającą częstotliwością
    note = np.sin(2 * np.pi * freq * t) * 0.5

    # Zastosowanie fade-out
    fade_samples = int(SAMPLE_RATE * 0.2)
    fade_curve = np.linspace(1.0, 0.0, fade_samples)
    note[-fade_samples:] *= fade_curve

    # Konwersja do formatu 16-bitowego
    audio = (note * 32767).astype(np.int16)

    # Konwersja do stereo (2 kanały)
    stereo = np.column_stack((audio, audio))  # Duplikacja mono do stereo

    # Zapisanie jako plik WAV
    file_path = os.path.join(sounds_path, "death.wav")

    # Zapisanie jako plik WAV ręcznie
    with wave.open(file_path, 'w') as wav_file:
        # Ustawienie parametrów pliku WAV
        wav_file.setnchannels(2)  # Stereo
        wav_file.setsampwidth(2)  # 2 bajty na próbkę (16-bit)
        wav_file.setframerate(SAMPLE_RATE)

        # Konwersja tablicy NumPy do bajtów
        for sample in stereo:
            wav_file.writeframes(struct.pack('<h', sample[0]))
            wav_file.writeframes(struct.pack('<h', sample[1]))

    print(f"Zapisano death.wav")

create_death_sound()

print("Wszystkie dźwięki zostały wygenerowane!")
