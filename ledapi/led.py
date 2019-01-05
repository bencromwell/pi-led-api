import RPi.GPIO as GPIO
import time


def setup(led_pin):
    # setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)


def blink_led(led_pin, num_times=1, seconds_on=1):
    i = 1
    while i <= num_times:
        # led on
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(seconds_on)
        # led off
        GPIO.output(led_pin, GPIO.LOW)


def tear_down():
    GPIO.cleanup()


def go(led_pin, num_times, seconds_on):
    setup(led_pin)
    blink_led(led_pin, num_times=num_times, seconds_on=seconds_on)
    tear_down()


if __name__ == '__main__':
    go(18, 5, 2)
