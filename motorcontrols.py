import RPi.GPIO as GPIO
import sys, tty, termios, time
import math

GPIO.setmode(GPIO.BCM)
motor1_1 = 17
motor1_2 = 22
motor2_1 = 23
motor2_2 = 4
p1 = 18
GPIO.setup(motor1_1, GPIO.OUT)
GPIO.setup(motor1_2, GPIO.OUT)
GPIO.setup(motor2_1, GPIO.OUT)
GPIO.setup(motor2_2, GPIO.OUT)
GPIO.setup(p1, GPIO.OUT)
pwm = GPIO.PWM(p1, 1000)
pwm.start(100)
GPIO.output(p1, 1)
cycle = 0


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while(True):
    char = getch()
    if(char == "w"):
        pwm.ChangeDutyCycle(100)
        GPIO.output(motor1_1, 1)
        GPIO.output(motor1_2, 0)
        GPIO.output(motor2_1, 1)
        GPIO.output(motor2_2, 0)
    if(char == "s"):
        pwm.ChangeDutyCycle(100)
        GPIO.output(motor1_1, 0)
        GPIO.output(motor1_2, 1)
        GPIO.output(motor2_1, 0)
        GPIO.output(motor2_2, 1)
    if(char == "a"):
        pwm.ChangeDutyCycle(100)
        GPIO.output(motor1_1, 1)
        GPIO.output(motor1_2, 0)
        GPIO.output(motor2_1, 0)
        GPIO.output(motor2_2, 1)
    if(char == "d"):
        pwm.ChangeDutyCycle(100)
        GPIO.output(motor1_1, 0)
        GPIO.output(motor1_2, 1)
        GPIO.output(motor2_1, 1)
        GPIO.output(motor2_2, 0)
    if(char == "p"):
        pwm.ChangeDutyCycle(0)
        GPIO.output(motor1_1, 0)
        GPIO.output(motor1_2, 0)
        GPIO.output(motor2_1, 0)
        GPIO.output(motor2_2, 0)
    if(char == "x"):
        GPIO.cleanup()
        print "Terminated."
        sys.exit()
