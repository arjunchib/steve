import RPi.GPIO as GPIO
import sys
import tty
import termios
import time
from vehicle import Vehicle
from motor import Motor
import socket

GPIO.setmode(GPIO.BCM)
motor1 = Motor(13, 26, 16)  # Forward Left
motor2 = Motor(17, 27, 22)  # Forward Right
motor3 = Motor(12, 6, 5)    # Rear Left
motor4 = Motor(25, 24, 23)  # Rear Right
steve = Vehicle(motor1, motor2, motor3, motor4)

s = socket.socket()
host = socket.gethostname()
port = 69420
s.bind((host, port))

# message: "10 20"
s.listen(5)
while True:
    c, addr = s.accept()
    while True:
        message = s.recv(128)
        print(message)
        if message == "STOP":
            break
        leftVelocity, rightVelocity = parse(message)
        motor1.rotate(leftVelocity)
        motor3.rotate(leftVelocity)
        motor2.rotate(rightVelocity)
        motor4.rotate(rightVelocity)
    c.close()


def parse(message):
    splitInedx = message.find(" ", 0)
    leftVelocity = int(message.substring(0, splitInedx))
    rightVelocity = int(message.substring(splitInedx, len(message)))
    return (leftVelocity, rightVelocity)
