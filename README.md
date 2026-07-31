# Luftmessdaten

Eine mobile Luftmessstation auf dem Raspberry Pi — und eines meiner ersten Projekte.

Der eigentliche Auslöser war nicht die Luft, sondern der **SPI-Bus**: Ich wollte ihn verstehen
und nicht nur nachlesen. Dafür brauchte es eine Anwendung, in der wirklich mehrere Geräte am
selben Bus hängen, und eine Messstation mit drei Sensoren war dafür naheliegend. Ein
Batteriepack macht die Station mobil, die Werte landen live auf einem Dashboard im Internet.

---

## Was gemessen wird

| Sensor | Anbindung | Misst |
|---|---|---|
| BME280 | SPI (CS auf D13) | Temperatur, Luftfeuchtigkeit, Luftdruck |
| MCP3008 → VOC-Sensor | SPI (CS auf D25), Kanal 0 | Flüchtige organische Verbindungen |
| MCP3008 → LDR | SPI (CS auf D25) | Helligkeit |
| SDS011 | serielle Schnittstelle, `/dev/ttyUSB0` | Feinstaub PM2.5 und PM10 |
| Raspberry Pi | intern | CPU-Temperatur |
| OpenWeather API | Internet | Temperatur und Luftfeuchtigkeit als Vergleichswert |

Die drei SPI-Geräte teilen sich Takt, MOSI und MISO (D21, D20, D19) und werden über
unterschiedliche Chip-Select-Leitungen angesprochen — genau das, was ich am Bus verstehen wollte.

Der SDS011 spricht kein SPI, sondern ein eigenes Binärprotokoll über USB-Seriell. Die
OpenWeather-Daten kommen dazu, damit sich die eigenen Messwerte mit der offiziellen
Wetterstation vergleichen lassen.

---

## Wohin die Daten gehen

`ADAFRUIT_IO.py` ist das Hauptprogramm. Es liest alle Werte der Reihe nach aus und schickt
sie alle 40 Sekunden an zehn Feeds bei **Adafruit IO**, wo sie als Live-Diagramme dargestellt
werden:

```
cputemperature      smalparticelmatter    bigparticelmatter
ldrsensor           vocsensor
bme280temperature   bme280humidity        bme280pressure
apihumidity         apitemperature
```

---

## Dateien

```
ADAFRUIT_IO.py     Hauptprogramm, sendet alle Werte an Adafruit IO
BME280.py          Temperatur, Feuchtigkeit, Druck über SPI
MCP3008_VOC.py     VOC-Sensor am Analog-Digital-Wandler
MCP3008_LDR.py     Helligkeitssensor am selben Wandler
SDS011_PM.py       Feinstaubwerte PM2.5 und PM10
__init__.py        Treiber für den SDS011
weather.py         Wetterdaten von der OpenWeather API
cpu_temperature.py CPU-Temperatur des Raspberry Pi
SPI_all_values.py  kleines Testskript, gibt alle SPI-Werte im Terminal aus
```

Zum Ausprobieren ohne Cloud reicht `SPI_all_values.py` — das Skript liest die SPI-Sensoren
im Sekundentakt und schreibt sie ins Terminal.

---

## Voraussetzungen

```
adafruit-circuitpython-bme280
adafruit-circuitpython-mcp3xxx
adafruit-blinka
adafruit-io
gpiozero
pyserial
requests
```

## Konfiguration

In `ADAFRUIT_IO.py` müssen Benutzername und Key für Adafruit IO eingetragen werden, in
`weather.py` ein eigener OpenWeather-API-Key. Beide gehören **nicht** ins Repository —
besser über Umgebungsvariablen oder eine lokale, in `.gitignore` eingetragene Datei laden.

---

*Ein frühes Projekt, und man sieht es dem Code an. Ich habe ihn trotzdem so gelassen, wie er
damals entstanden ist — er hat getan, was er sollte, und der SPI-Bus sitzt seitdem.*
