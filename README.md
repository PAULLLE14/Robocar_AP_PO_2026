## Robocar – Linienverfolgung

Autonomer Linienfolger auf Basis eines Raspberry Pi. Ein PCA9685 steuert über vier DC-Motoren das Fahrzeug, drei Infrarot-Liniensensoren erkennen den Streckenverlauf.

Das Projekt entstand im Rahmen der Vorlesung *Programmieren 1* an der DHBW Heidenheim.

## Hardware

| Komponente | Beschreibung |
|---|---|
| Raspberry Pi | Steuerrechner, kommuniziert per I²C |
| PCA9685 | PWM-Treiber für die Motoren (I²C-Adresse `0x40`) |
| 4× DC-Motor | Allradantrieb, je zwei PWM-Kanäle pro Motor |
| 3× Liniensensor | Infrarot, digital (links / mitte / rechts) |

## Aufbau des Projekts

| Datei | Aufgabe |
|---|---|
| `main.py` | Einstiegspunkt, wählt den Algorithmus und hält die Hauptschleife |
| `config.py` | Lädt die Einstellungen aus `config.json` |
| `config.json` | Alle einstellbaren Werte (Pins, Kanäle, Geschwindigkeiten) |
| `sensors.py` | Liest die drei Liniensensoren aus |
| `motors.py` | Setzt die Geschwindigkeit der vier Motoren |
| `control_pid.py` | Linienverfolgung mit proportionaler Regelung |
| `control_pingpong.py` | Einfache regelbasierte Linienverfolgung |

## Algorithmus auswählen

In `config.json` steuert das Feld `algorithm`, welche Strategie gefahren wird:

```json
{
    "algorithm": "pid"
}
```

Mögliche Werte:

- `"pid"` – proportionale Regelung, fährt auf Geraden schneller und in Kurven langsamer
- `"pingpong"` – einfache Wenn-Dann-Logik, lenkt mit fester Geschwindigkeit

## Werte anpassen

Alle Parameter liegen in `config.json` und können ohne Eingriff in den Code verändert werden.

Für die proportionale Regelung (`control_pid.py`):

| Wert | Bedeutung |
|---|---|
| `steering_gain` | Lenkstärke – höher lenkt aggressiver |
| `base_speed` | Grundgeschwindigkeit auf gerader Linie |
| `min_speed` | Mindestgeschwindigkeit in engen Kurven |
| `speed_reduction_per_error` | wie stark in Kurven abgebremst wird |

Für die regelbasierte Strategie (`control_pingpong.py`):

| Wert | Bedeutung |
|---|---|
| `forward_speed` | Geschwindigkeit geradeaus |
| `turn_speed` | Geschwindigkeit beim Lenken |

## Installation

Voraussetzung ist ein aktivierter I²C-Bus auf dem Raspberry Pi.

```bash
sudo modprobe i2c-dev
pip3 install -r requirements.txt --break-system-packages
```

## Start

```bash
cd src
sudo python3 main.py
```

Das Fahrzeug stoppt, sobald alle drei Sensoren gleichzeitig die Linie erkennen – also wenn es angehoben wird. Mit `Strg + C` wird das Programm beendet und die Motoren werden ausgeschaltet.
