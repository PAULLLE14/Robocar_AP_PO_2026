import board
from adafruit_pca9685 import PCA9685
import time
import logging
from gpiozero import LineSensor

log = logging.getLogger(__name__)
i2c = board.I2C()
pca = PCA9685(i2c)

current_speed_front_left = 0
current_speed_front_right = 0
current_speed_rear_left = 0
current_speed_front_right = 0

sensor_left   = LineSensor(23)
sensor_middle = LineSensor(15)
sensor_right  = LineSensor(14)

def init():
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
    left   = sensor_left.value
    middle = sensor_middle.value
    right  = sensor_right.value
    return left, middle, right

def drive_forward():
    front_left(20)
    rear_left(20)
    front_right(20)
    rear_right(20)

def turn_left():
    front_left(20)
    rear_left(20)
    front_right(-25)
    rear_right(-25)

def turn_right():
    front_left(-25)
    rear_left(-25)
    front_right(20)
    rear_right(20)

def drive():
    left, middle, right = read_sensors()
    if middle == 1:
        drive_forward()
    elif left == 1:
        turn_left()
    elif right == 1:
        turn_right()

init()
start = time.time()
while time.time() - start < 60:
    drive()
stop_all()
