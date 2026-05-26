import board
from adafruit_pca9685 import PCA9685
import time
import logging
import RPi.GPIO as GPIO

log = logging.getLogger(__name__)

i2c = board.I2C()

pca = PCA9685(i2c)

current_speed_front_left = 0
current_speed_front_right = 0
current_speed_rear_left = 0
current_speed_front_right = 0

SENSOR_LEFT   = 23
SENSOR_MIDDLE = 15
SENSOR_RIGHT  = 14

def init ():
    log.info("initialize the PWM module")
    pca.frequency = 50
    pca.channels[0].duty_cycle = 0
    pca.channels[1].duty_cycle = 0
    pca.channels[2].duty_cycle = 0
    pca.channels[3].duty_cycle = 0
    pca.channels[4].duty_cycle = 0
    pca.channels[5].duty_cycle = 0
    pca.channels[6].duty_cycle = 0
    pca.channels[7].duty_cycle = 0

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_LEFT,   GPIO.IN)
    GPIO.setup(SENSOR_MIDDLE, GPIO.IN)
    GPIO.setup(SENSOR_RIGHT,  GPIO.IN)

    pass

def stop_all():
    pca.frequency = 50
    pca.channels[0].duty_cycle = 0
    pca.channels[1].duty_cycle = 0
    pca.channels[2].duty_cycle = 0
    pca.channels[3].duty_cycle = 0
    pca.channels[4].duty_cycle = 0
    pca.channels[5].duty_cycle = 0
    pca.channels[6].duty_cycle = 0
    pca.channels[7].duty_cycle = 0
    current_speed_front_left = 0
    current_speed_front_right = 0
    current_speed_rear_left = 0
    current_speed_front_right = 0

def front_left(speed=0):
    if 0 > abs(speed) > 100:
        log.error(f"speed {speed} outside of range 0-100")
        return

    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_front_left = speed

    if speed >= 0:
        pca.channels[0].duty_cycle = 0
        pca.channels[1].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[0].duty_cycle = motor_speed
        pca.channels[1].duty_cycle = 0


def rear_left(speed=0):
    if 0 > abs(speed) > 100:
        log.error(f"speed {speed} outside of range 0-100")
        return

    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_rear_left = speed

    if speed >= 0:
        pca.channels[3].duty_cycle = 0
        pca.channels[2].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[3].duty_cycle = motor_speed
        pca.channels[2].duty_cycle = 0


def rear_right(speed=0):
    if 0 > abs(speed) > 100:
        log.error(f"speed {speed} outside of range 0-100")
        return

    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_rear_right = speed

    if speed >= 0:
        pca.channels[4].duty_cycle = 0
        pca.channels[5].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[4].duty_cycle = motor_speed
        pca.channels[5].duty_cycle = 0


def front_right(speed=0):
    if 0 > abs(speed) > 100:
        log.error(f"speed {speed} outside of range 0-100")
        return

    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_front_right = speed

    if speed >= 0:
        pca.channels[7].duty_cycle = 0
        pca.channels[6].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[7].duty_cycle = motor_speed
        pca.channels[6].duty_cycle = 0

def read_sensors():
    left   = GPIO.input(SENSOR_LEFT)
    middle = GPIO.input(SENSOR_MIDDLE)
    right  = GPIO.input(SENSOR_RIGHT)
    return left, middle, right

def drive():
    left, middle, right = read_sensors()

    if middle == 1:
        front_left(50)
        rear_left(50)
        front_right(50)
        rear_right(50)
    elif middle ==0:
        front_left(0)
        rear_left(0)
        front_right(0)
        rear_right(0)

init()

start = time.time()
while time.time() - start < 4:
    drive()

stop_all()
