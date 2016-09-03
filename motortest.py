import RPi.GPIO as GPIO
import sys, tty, termios, time
import math

GPIO.setmode(GPIO.BCM)
enable   = 17
forward  = 27
backward = 22

GPIO.setup(enable, GPIO.OUT)
GPIO.setup(forward, GPIO.OUT)
GPIO.setup(backward, GPIO.OUT)
pwm = GPIO.PWM(enable, 1000)
# backward_pwm = GPIO.PWM(backward, 1000)
pwm.start(100)
# backward_pwm.start(100)

counter = 0

try:
    while counter < 9000000:
        pwm.ChangeDutyCycle(100)
        GPIO.output(forward, 1)
        GPIO.output(backward, 0)
        counter += 1
    print "Target reached: %d" % counter

except KeyboardInterrupt:
    print "\n", counter

except:
    print "Other error or exception occurred!"

finally:
    GPIO.cleanup()
    sys.exit()
