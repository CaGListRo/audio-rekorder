Audio Recorder Script
Dieses Python-Skript ermöglicht es, den Audioausgang eines Computers aufzunehmen, z.B. um das Audio aufzunehmen, das über Lautsprecher oder Kopfhörer abgespielt wird. Das Skript verwendet die pyaudio-Bibliothek und speichert die Aufnahme als WAV-Datei.

Voraussetzungen
Bevor du das Skript ausführst, stelle sicher, dass die folgenden Bibliotheken installiert sind:

- pyaudio
- wave

Du kannst diese Bibliotheken mit pip installieren:
pip install pyaudio

Verwendung

1. Ausführen des Skripts
   Führe das Skript aus, indem du in der Kommandozeile den folgenden Befehl eingibst:
   python main.py

2. Auswahl des Aufnahmegeräts
   Nach dem Start des Skripts werden alle verfügbaren Aufnahmegeräte angezeigt, die mehr als 0 Kanäle unterstützen. Wähle das gewünschte Gerät aus, indem du die entsprechende Nummer eingibst und Enter drückst.

3. Start und Stopp der Aufnahme
   Die Aufnahme startet automatisch, sobald das Skript ausgeführt wird.
   Um die Aufnahme zu stoppen, drücke Enter.

4. Ergebnis
   Das aufgenommene Audio wird in einer Datei namens output.wav im selben Verzeichnis gespeichert, in dem sich das Skript befindet.

Wichtige Hinweise
Geräteauswahl: Falls kein geeignetes Gerät verfügbar ist, z.B. um den Systemaudio aufzuzeichnen, kann es notwendig sein, ein virtuelles Audiogerät wie "Stereo Mix" (unter Windows) oder Software wie "Virtual Audio Cable" zu verwenden.

Fehlermeldungen: Wenn eine Fehlermeldung bezüglich der Anzahl der Kanäle auftritt, stelle sicher, dass du ein Gerät auswählst, das die angegebene Anzahl von Kanälen unterstützt (in der Regel 2 für Stereo).

Anpassungen: Du kannst die Einstellungen wie Abtastrate (RATE), Chunk-Größe (CHUNK), und Dateiname (OUTPUT_FILE) im Skript nach deinen Bedürfnissen anpassen.

Lizenz
Dieses Skript steht unter der MIT-Lizenz.
