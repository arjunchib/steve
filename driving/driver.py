import RPi.GPIO as GPIO
import sys
import tty
import termios
import time
from vehicle import Vehicle
from motor import Motor

GPIO.setmode(GPIO.BCM)
motor1 = Motor(13, 26, 16)  # Forward Left
motor2 = Motor(17, 27, 22)  # Forward Right
motor3 = Motor(12, 6, 5)    # Rear Left
motor4 = Motor(25, 24, 23)  # Rear Right
steve = Vehicle(motor1, motor2, motor3, motor4)


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

try:
    while True:
        char = getch()
        if(char == "w"):
            steve.moveForward()
        if(char == "s"):
            steve.moveBackward()
        if(char == "a"):
            steve.turnLeft()
        if(char == "d"):
            steve.turnRight()
        if(char == "p"):
            steve.stop()
        if(char == "x"):
            break

except Exception as e:
    print "Exception occurred!"
    print(str(e))

finally:
    GPIO.cleanup()
    sys.exit()
