import logging
import motors
import sensors

log = logging.getLogger(__name__)


def drive_forward():
    motors.set_front_left_speed(20)
    motors.set_rear_left_speed(20)
    motors.set_front_right_speed(20)
    motors.set_rear_right_speed(20)


def turn_left():
    motors.set_front_left_speed(20)
    motors.set_rear_left_speed(20)
    motors.set_front_right_speed(-25)
    motors.set_rear_right_speed(-25)


def turn_right():
    motors.set_front_left_speed(-25)
    motors.set_rear_left_speed(-25)
    motors.set_front_right_speed(20)
    motors.set_rear_right_speed(20)


def drive():
    left, middle, right = sensors.read_sensors()
    if middle == 1:
        drive_forward()
    elif left == 1:
        turn_left()
    elif right == 1:
        turn_right()
    else:
        motors.stop_all()
