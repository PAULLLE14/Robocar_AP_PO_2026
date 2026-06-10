import logging
import time
import motors
import sensors

log = logging.getLogger(__name__)

def drive_backward():
    motors.set_front_left_speed(-20)
    motors.set_rear_left_speed(-20)
    motors.set_front_right_speed(-20)
    motors.set_rear_right_speed(-20)

def drive_forward():
    motors.set_front_left_speed(20)
    motors.set_rear_left_speed(20)
    motors.set_front_right_speed(20)
    motors.set_rear_right_speed(20)


def turn_left():
    motors.set_front_left_speed(25)
    motors.set_rear_left_speed(25)
    motors.set_front_right_speed(-25)
    motors.set_rear_right_speed(-25)


def turn_right():
    motors.set_front_left_speed(-25)
    motors.set_rear_left_speed(-25)
    motors.set_front_right_speed(25)
    motors.set_rear_right_speed(25)


def turn_180():
    motors.set_front_left_speed(25)
    motors.set_rear_left_speed(25)
    motors.set_front_right_speed(-25)
    motors.set_rear_right_speed(-25)


no_line_since = None


def drive():
    global no_line_since
    left, middle, right = sensors.read_sensors()

    if left == 1 and middle == 1 and right == 1:
        motors.stop_all()
        no_line_since = None
    elif left == 0 and middle == 0 and right == 0:
        if no_line_since is None:
            no_line_since = time.time()
        elif time.time() - no_line_since > 1:
            motors.stop_all()
            turn_180()
            no_line_since = None
    else:
        no_line_since = None
        if middle == 1:
            drive_forward()
        elif left == 1:
            turn_left()
        elif right == 1:
            turn_right()
