# Written by Sam Wright

import time 
from gpiozero import DistanceSensor
from gpiozero import CamJamKitRobot

pinTrigger = 17
pinEcho = 18
distanceToStop = 0.05
robot = CamJamKitRobot()

sensor = DistanceSensor(echo=pinEcho,trigger=pinTrigger)

try:
    while True:
        print("Distance:",sensor.distance)
        robot.forward()
        if sensor.distance <= distanceToStop:
            robot.stop()
            break
except KeyboardInterrupt:
    print("finished")
