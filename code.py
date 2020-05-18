import time  # Import the Time library


# from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

class DistanceSensor:

    def __init__(self):
        self.d = 10

    def increase_distance(self, x):
        self.d += x

    def decrease_distance(self, x):
        self.d -= x

    @property
    def distance(self):
        return self.d / 100


sensor = DistanceSensor()


class CamJamKitRobot:

    def __init__(self):

        self.x = 0
        self.y = 0
        self.bearing = 0
        self.move_in_progress = False
        self.v = (0, 0)

    def forward(self):
        self.move_in_progress = True
        while self.move_in_progress:
            self.x = self.x + 1
            print("Moving forward")
            sensor.decrease_distance(1)
            self.move_in_progress = False

    def backward(self):
        self.x = self.x - 1
        sensor.increase_distance(1)
        print("Moving backwards")

    def right(self):
        self.y = self.y + 1
        self.bearing += 90
        print("moving right")

    def left(self):
        self.y = self.y - 1
        self.bearing -= 90
        print("Moving left")

    def stop(self):
        self.move_in_progress = False
        print("Robot stopped")

    def show_movement(self):
        if self.v[0] > 0:
            print("left motor is going forwards with speed {}".format(self.v[0]))
        elif self.v[0] < 0:
            print("left motor is going backwards with speed {}".format(self.v[0]))
        else:
            print("left motor is not moving")

        if self.v[1] > 0:
            print("right motor is going forwards with speed {}".format(self.v[1]))
        elif self.v[1] < 0:
            print("right motor is going backwards with speed {}".format(self.v[1]))
        else:
            print("right motor is not moving")

    @property
    def value(self):
        print("Motor value: ", self.v)

        return self.v

    @value.setter
    def value(self, v):
        self.v = v
        self.show_movement()


# Return True if the ultrasonic sensor sees an obstacle
def isnearobstacle(localhownear):
    distance = sensor.distance * 100

    print("IsNearObstacle: " + str(distance))
    if distance < localhownear:
        return True
    else:
        return False
