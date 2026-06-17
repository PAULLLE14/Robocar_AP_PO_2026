import logging

import board
from adafruit_pca9685 import PCA9685

log = logging.getLogger(__name__)

i2c = board.I2C()
pca = PCA9685(i2c)

PWM_FREQUENCY = 50
PWM_MAX = 0xFFFF
SPEED_MAX = 100

CHANNEL_FRONT_LEFT_FWD = 0
CHANNEL_FRONT_LEFT_BWD = 1
CHANNEL_REAR_LEFT_FWD = 3
CHANNEL_REAR_LEFT_BWD = 2
CHANNEL_REAR_RIGHT_FWD = 4
CHANNEL_REAR_RIGHT_BWD = 5
CHANNEL_FRONT_RIGHT_FWD = 7
CHANNEL_FRONT_RIGHT_BWD = 6

current_speed = {"front_left": 0, "front_right": 0, "rear_left": 0, "rear_right": 0}


def init():
    log.info("initialize the PWM module")
    pca.frequency = PWM_FREQUENCY
    for channel in range(8):
        pca.channels[channel].duty_cycle = 0


def stop_all():
    for channel in range(8):
        pca.channels[channel].duty_cycle = 0
    for key in current_speed:
        current_speed[key] = 0


def is_speed_valid(speed):
    return 0 <= abs(speed) <= SPEED_MAX


def set_motor_speed(channel_forward, channel_backward, speed):
    duty_cycle = int((abs(speed) * PWM_MAX) / SPEED_MAX)
    if speed >= 0:
        pca.channels[channel_forward].duty_cycle = 0
        pca.channels[channel_backward].duty_cycle = duty_cycle
    else:
        pca.channels[channel_forward].duty_cycle = duty_cycle
        pca.channels[channel_backward].duty_cycle = 0


def set_front_left_speed(speed=0):
    if not is_speed_valid(speed):
        log.error(f"speed {speed} outside of range 0-100")
        return
    current_speed["front_left"] = speed
    set_motor_speed(CHANNEL_FRONT_LEFT_FWD, CHANNEL_FRONT_LEFT_BWD, speed)


def set_rear_left_speed(speed=0):
    if not is_speed_valid(speed):
        log.error(f"speed {speed} outside of range 0-100")
        return
    current_speed["rear_left"] = speed
    set_motor_speed(CHANNEL_REAR_LEFT_FWD, CHANNEL_REAR_LEFT_BWD, speed)


def set_rear_right_speed(speed=0):
    if not is_speed_valid(speed):
        log.error(f"speed {speed} outside of range 0-100")
        return
    current_speed["rear_right"] = speed
    set_motor_speed(CHANNEL_REAR_RIGHT_FWD, CHANNEL_REAR_RIGHT_BWD, speed)


def set_front_right_speed(speed=0):
    if not is_speed_valid(speed):
        log.error(f"speed {speed} outside of range 0-100")
        return
    current_speed["front_right"] = speed
    set_motor_speed(CHANNEL_FRONT_RIGHT_FWD, CHANNEL_FRONT_RIGHT_BWD, speed)
