# https://github.com/dpallot/simple-websocket-server
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import RPi.GPIO as GPIO
import sys
import tty
import termios
import time
from vehicle import Vehicle
from motor import Motor
import atexit
import json


def exit_handler():
    print 'Please hold on server is stopping...'
    GPIO.cleanup()

atexit.register(exit_handler)

GPIO.setmode(GPIO.BCM)
motor1 = Motor(13, 26, 16)  # Forward Left
motor2 = Motor(17, 27, 22)  # Forward Right
motor3 = Motor(12, 6, 5)    # Rear Left
motor4 = Motor(25, 24, 23)  # Rear Right
steve = Vehicle(motor1, motor2, motor3, motor4)


class SimpleEcho(WebSocket):

    def handleMessage(self):
        try:
            message = self.data[2:]
            data = json.loads(message)
            leftVelocity = data[1]['left']
            rightVelocity = data[1]['right']
            print(leftVelocity, rightVelocity)
            motor1.rotate(leftVelocity)
            motor3.rotate(leftVelocity)
            motor2.rotate(rightVelocity)
            motor4.rotate(rightVelocity)
        except Exception, e:
            print 'Exception occurred!'
            print str(e)
            sys.exit()

    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'
        steve.stop()

server = SimpleWebSocketServer('', 8006, SimpleEcho)
server.serveforever()
