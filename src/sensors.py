import logging
from gpiozero import LineSensor

log = logging.getLogger(__name__)

sensor_left = LineSensor(23)
sensor_middle = LineSensor(15)
sensor_right = LineSensor(14)


def read_sensors():
    left = sensor_left.value
    middle = sensor_middle.value
    right = sensor_right.value
    return left, middle, right
