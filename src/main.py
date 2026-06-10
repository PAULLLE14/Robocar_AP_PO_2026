import logging
import time
import motors
import control

logging.basicConfig(level=logging.INFO)

motors.init()

try:
    while True:
        control.drive()
except KeyboardInterrupt:
    motors.stop_all()
