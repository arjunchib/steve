from motor import Motor


class Vehicle:
    'Class with that controls vehicle motors'

    def __init__(self, leftFrontMotor, rightFrontMotor,
                 leftRearMotor, rightRearMotor):
        self.motor1 = leftFrontMotor
        self.motor2 = rightFrontMotor
        self.motor3 = leftRearMotor
        self.motor4 = rightRearMotor

    def moveForward(self, speed=100):
        self.motor1.rotateForward(speed)
        self.motor2.rotateForward(speed)
        self.motor3.rotateForward(speed)
        self.motor4.rotateForward(speed)

    def moveBackward(self, speed=100):
        self.motor1.rotateBackward(speed)
        self.motor2.rotateBackward(speed)
        self.motor3.rotateBackward(speed)
        self.motor4.rotateBackward(speed)

    def move(self, velocity=100):
        self.motor1.rotate(velocity)
        self.motor2.rotate(velocity)
        self.motor3.rotate(velocity)
        self.motor4.rotate(velocity)

    def turnLeft(self, speed=100):
        self.motor1.rotateBackward(speed)
        self.motor2.rotateForward(speed)
        self.motor3.rotateBackward(speed)
        self.motor4.rotateForward(speed)

    def turnRight(self, speed=100):
        self.motor1.rotateForward(speed)
        self.motor2.rotateBackward(speed)
        self.motor3.rotateForward(speed)
        self.motor4.rotateBackward(speed)

    def turn(self, velocity=100):
        if velocity > 0:
            self.turnLeft(velocity)
        elif velocity < 0:
            self.turnRight(velocity)
        else:
            self.stop()

    def stop(self):
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
