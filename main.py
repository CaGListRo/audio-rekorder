import pyaudio
import threading
import wave
from typing import Final, TypeVar

Audio = TypeVar("Audio")

def list_devices(p: pyaudio.PyAudio) -> list[tuple[int, str]]:
    """
    Listet alle Aufnahmegeräte auf, die mehr als 0 Kanäle unterstützen.
    Args:
    p (pyaudio.PyAudio): Das PyAudio-Objekt.
    """
    print("Verfügbare Aufnahmegeräte (nur mit > 0 Kanälen):")
    valid_devices: list[tuple[int, str]] = []
    for i in range(p.get_device_count()):
        info: dict[int | float] = p.get_device_info_by_index(i)
        if info['maxInputChannels'] > 0:
            valid_devices.append((len(valid_devices) + 1, i, info['name'], info['maxInputChannels']))
            print(f"Index {len(valid_devices)}: {info['name']} (Kanäle: {info['maxInputChannels']})")
    return valid_devices

def record_audio(device_index: int, channels: int) -> None:
    """
    Zeichnet Audio vom ausgewählten Gerät auf.
    Args:
    device_index (int): Der Index des Geräts.
    channels (int): Die Anzahl der Kanäle.
    """
    global recording

    # PyAudio-Instanz erstellen
    p: pyaudio.PyAudio = pyaudio.PyAudio()

    # Aufzeichnungs-Stream starten
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=RATE,
                    input=True,
                    input_device_index=device_index,
                    frames_per_buffer=CHUNK)

    print("Aufnahme startet...")

    frames: list[Audio] = []

    # Aufnahmeprozess
    while recording:
        data = stream.read(CHUNK)
        frames.append(data)


    print("Aufnahme beendet.")

    # Stream stoppen und schließen
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Frames in eine Datei schreiben
    with wave.open(OUTPUT_FILE, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio wurde in '{OUTPUT_FILE}' gespeichert.")

if __name__ == "__main__":
    # Einstellungen
    CHUNK: Final[int] = 1024
    FORMAT: Final[int] = pyaudio.paInt16
    RATE: Final[int] = 44100
    OUTPUT_FILE: Final[str] = "output.wav"

    # PyAudio-Instanz erstellen
    p: pyaudio.PyAudio = pyaudio.PyAudio()

    # Liste der verfügbaren Geräte
    valid_devices: list[tuple[int, str]] | None = list_devices(p)

    # Überprüfen, ob gültige Geräte verfügbar sind
    if not valid_devices:
        print("Keine gültigen Aufnahmegeräte mit mehr als 0 Kanälen gefunden.")
    else:
        # Auswahl des Geräts durch den Benutzer
        user_choice: int = int(input("Gib den Index des gewünschten Aufnahmegeräts ein: "))
        selected_device: int = valid_devices[user_choice - 1]
        device_index: int = selected_device[1]
        channels: int = selected_device[3]

        # Globale Variable zum Steuern der Aufnahme
        recording: bool = True

        # Aufnahme in einem separaten Thread starten
        recording_thread: threading.Thread = threading.Thread(target=record_audio, args=(device_index, channels))
        recording_thread.start()

        # Auf Eingabe warten, um die Aufnahme zu stoppen
        input("Drücke Enter, um die Aufnahme zu stoppen...\n")
        recording = False

        # Sicherstellen, dass der Thread beendet wird
        recording_thread.join()

    print("Das Skript wurde beendet.")
