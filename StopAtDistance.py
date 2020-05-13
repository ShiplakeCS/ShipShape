# Written by Sam Wright

import time
from gpiozero import DistanceSensor
from gpiozero import CamJamKitRobot

pinTrigger = 17
pinEcho = 18
distanceToStop = 0.5
robot = CamJamKitRobot()

sensor = DistanceSensor(echo=pinEcho,trigger=pinTrigger)

x = 0
    
try:
    while True:
        print("Distance:",sensor.distance)
        if sensor.distance >= distanceToStop:
            robot.forward()
            print("{}: forward".format(x))
            x+=1
        else:
            robot.stop()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("finished")

