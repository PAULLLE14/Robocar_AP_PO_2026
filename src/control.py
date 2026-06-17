import logging
import motors
import sensors
from config import config

log = logging.getLogger(__name__)

FORWARD_SPEED = config["speeds"]["forward"]
TURN_SPEED    = config["speeds"]["turn"]


def is_lifted(left, middle, right):
    return left == 1 and middle == 1 and right == 1


def drive_forward():
    motors.set_front_left_speed(FORWARD_SPEED)
    motors.set_rear_left_speed(FORWARD_SPEED)
    motors.set_front_right_speed(FORWARD_SPEED)
    motors.set_rear_right_speed(FORWARD_SPEED)


def turn_left():
    motors.set_front_left_speed(TURN_SPEED)
    motors.set_rear_left_speed(TURN_SPEED)
    motors.set_front_right_speed(-TURN_SPEED)
    motors.set_rear_right_speed(-TURN_SPEED)


def turn_right():
    motors.set_front_left_speed(-TURN_SPEED)
    motors.set_rear_left_speed(-TURN_SPEED)
    motors.set_front_right_speed(TURN_SPEED)
    motors.set_rear_right_speed(TURN_SPEED)


def drive():
    left, middle, right = sensors.read_sensors()

    if is_lifted(left, middle, right):
        motors.stop_all()
        return

    if middle == 1:
        drive_forward()
    elif left == 1:
        turn_left()
    elif right == 1:
        turn_right()
