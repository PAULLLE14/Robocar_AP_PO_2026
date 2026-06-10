import board
import logging
from adafruit_pca9685 import PCA9685

log = logging.getLogger(__name__)

i2c = board.I2C()
pca = PCA9685(i2c)

current_speed = {
    "front_left": 0,
    "front_right": 0,
    "rear_left": 0,
    "rear_right": 0
}


def init():
    log.info("initialize the PWM module")
    pca.frequency = 50
    for channel in range(8):
        pca.channels[channel].duty_cycle = 0


def stop_all():
    for channel in range(8):
        pca.channels[channel].duty_cycle = 0
    for key in current_speed:
        current_speed[key] = 0


def set_motor_speed(channel_forward, channel_backward, speed):
    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    if speed >= 0:
        pca.channels[channel_forward].duty_cycle = 0
        pca.channels[channel_backward].duty_cycle = motor_speed
    else:
        pca.channels[channel_forward].duty_cycle = motor_speed
        pca.channels[channel_backward].duty_cycle = 0


def set_front_left_speed(speed=0):
    if not (0 <= abs(speed) <= 100):
        log.error(f"speed {speed} outside of range 0-100")
        return
    current_speed["front_left"] = speed
    set_motor_speed(0, 1, speed)


def set_rear_left_speed(speed=0):
    if not (0 <= abs(speed) <= 100):
        log.error(f"speed {speed} outside of range 0-100")
        return
    current_speed["rear_left"] = speed
    set_motor_speed(3, 2, speed)


def set_rear_right_speed(speed=0):
    if not (0 <= abs(speed) <= 100):
        log.error(f"speed {speed} outside of range 0-100")
        return
    current_speed["rear_right"] = speed
    set_motor_speed(4, 5, speed)


def set_front_right_speed(speed=0):
    if not (0 <= abs(speed) <= 100):
        log.error(f"speed {speed} outside of range 0-100")
        return
    current_speed["front_right"] = speed
    set_motor_speed(7, 6, speed)
