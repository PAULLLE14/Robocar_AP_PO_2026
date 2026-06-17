import logging

from config import config
from gpiozero import LineSensor

log = logging.getLogger(__name__)

PIN_LEFT = config["sensor_pins"]["left"]
PIN_MIDDLE = config["sensor_pins"]["middle"]
PIN_RIGHT = config["sensor_pins"]["right"]

sensor_left = LineSensor(PIN_LEFT)
sensor_middle = LineSensor(PIN_MIDDLE)
sensor_right = LineSensor(PIN_RIGHT)


def read_sensors():
    left = sensor_left.value
    middle = sensor_middle.value
    right = sensor_right.value
    return left, middle, right
