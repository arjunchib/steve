import RPi.GPIO as GPIO
import sys
import tty
import termios


class Motor:
    'Class to drive each motor'

    def __init__(self, enable, forward, backward):
        self.enable = enable
        self.forward = forward
        self.backward = backward
        self.setup()

    def setup(self):
        GPIO.setup(self.enable, GPIO.OUT)
        GPIO.setup(self.forward, GPIO.OUT)
        GPIO.setup(self.backward, GPIO.OUT)
        self.pwm = GPIO.PWM(self.enable, 1000)

    def rotateForward(self, speed=100):
        self.pwm.start(100)
        speed = Motor.limitSpeed(speed)
        self.pwm.ChangeDutyCycle(speed)
        GPIO.output(self.forward, 1)
        GPIO.output(self.backward, 0)

    def rotateBackward(self, speed=100):
        speed = Motor.limitSpeed(speed)
        self.pwm.ChangeDutyCycle(speed)
        GPIO.output(self.forward, 0)
        GPIO.output(self.backward, 1)

    def rotate(self, velocity=100):
        if velocity > 0:
            self.rotateForward(velocity)
        elif velocity < 0:
            self.rotateBackward(velocity)
        else:
            self.stop()

    def stop(self):
        self.pwm.ChangeDutyCycle(0)
        GPIO.output(self.forward, 0)
        GPIO.output(self.backward, 0)

    @staticmethod
    def limitSpeed(speed):
        if speed < 0:
            speed = 0
        elif speed > 100:
            speed = 100
        return speed
