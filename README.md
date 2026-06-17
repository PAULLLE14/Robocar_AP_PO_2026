# Robocar – Team Foucault

Autonomer Linienfolger auf Basis eines Raspberry Pi. Drei Infrarotsensoren erkennen die Spur, ein PCA9685 steuert vier DC-Motoren über PWM.

Projekt im Rahmen von Programmieren 1 – DHBW Heidenheim, Kurs TMT2025A.

---

## Hardware

| Komponente | Details |
|---|---|
| Raspberry Pi | Steuerrechner, I²C-Bus |
| PCA9685 | PWM-Treiber, I²C-Adresse `0x40` |
| 4× DC-Motor | Allradantrieb, je zwei Kanäle pro Motor |
| 3× IR-Liniensensor | Digital, GPIO-Pins: links 23, mitte 15, rechts 14 |

---

## Projektstruktur

```
src/
├── main.py          Einstiegspunkt
├── control.py       Fahrentscheidung (Algorithmus)
├── motors.py        Motoransteuerung über PCA9685
├── sensors.py       Sensorwerte lesen
├── config.py        config.json laden
└── config.json      Geschwindigkeiten und Sensor-Pins
```

---

## Geschwindigkeiten anpassen

Alle Werte liegen in `src/config.json`:

```json
{
    "speeds": {
        "forward": 25,
        "turn": 20
    },
    "sensor_pins": {
        "left": 23,
        "middle": 15,
        "right": 14
    }
}
```

`forward` ist die Geschwindigkeit geradeaus, `turn` die Drehgeschwindigkeit in Kurven (0–100).

---

## Installation

I²C aktivieren (nach jedem Neustart):

```bash
sudo modprobe i2c-dev
```

Dauerhaft aktivieren:

```bash
echo "i2c-dev" | sudo tee -a /etc/modules
```

Abhängigkeiten installieren:

```bash
pip3 install -r requirements.txt --break-system-packages
```

---

## Start

```bash
cd src
sudo python3 main.py
```

Mit `Strg+C` beenden – die Motoren stoppen automatisch.

Das Fahrzeug stoppt auch, wenn alle drei Sensoren gleichzeitig schwarz sehen (Anheben des Roboters).

---

## Algorithmus

Der Roboter liest in jeder Schleifenrunde die drei Sensoren und entscheidet:

- Mittlerer Sensor aktiv → geradeaus
- Linker Sensor aktiv → nach links drehen
- Rechter Sensor aktiv → nach rechts drehen
- Alle drei schwarz → Stopp (Roboter angehoben)
