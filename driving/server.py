import RPi.GPIO as GPIO
import sys
import tty
import termios
import time
from vehicle import Vehicle
from motor import Motor
import socket


def parse(message):
    splitInedx = message.find(" ", 0)
    try:
        leftVelocity = int(message[0:splitInedx])
        rightVelocity = int(message[splitInedx:len(message)])
        return (leftVelocity, rightVelocity)
    except ValueError:
        return (0, 0)


GPIO.setmode(GPIO.BCM)
motor1 = Motor(13, 26, 16)  # Forward Left
motor2 = Motor(17, 27, 22)  # Forward Right
motor3 = Motor(12, 6, 5)    # Rear Left
motor4 = Motor(25, 24, 23)  # Rear Right
steve = Vehicle(motor1, motor2, motor3, motor4)

s = socket.socket()
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
# host = socket.gethostname()
host = "143.215.104.197"
port = 8006

try:
    s.bind((host, port))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    GPIO.cleanup()
    sys.exit()

try:
    s.listen(1)
    c, addr = s.accept()
    while True:
        message = c.recv(1024)
        requestMethod = message.split(' ')[0]
        print(requestMethod)
        if "GET" == requestMethod:
            print message
            handshake = "HTTP/1.1 200 OK\n"
            currentDate = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
            handshake += "Date: " + currentDate + "\n"
            handshake += "Server: STEVE-Server\n"
            handshake += "Connection: keep-alive\n\n"
            print "1"
            c.sendall(handshake.encode())
            print "2"
        # if message:
        #     print(message)
        #     if message == "STOP":
        #         break
        #     leftVelocity, rightVelocity = parse(message)
        #     motor1.rotate(leftVelocity)
        #     motor3.rotate(leftVelocity)
        #     motor2.rotate(rightVelocity)
        #     motor4.rotate(rightVelocity)
    c.close()

except Exception, e:
    print "Exception occurred!"
    print str(e)

finally:
    GPIO.cleanup()
    if c:
        c.close()
    if s:
        s.close()
    sys.exit()
