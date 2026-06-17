import logging

import control
import motors

logging.basicConfig(level=logging.INFO)

motors.init()

input("Bereit. Enter drücken zum Starten...")

try:
    while True:
        control.drive()
except KeyboardInterrupt:
    motors.stop_all()
