from gpiozero import CamJamKitRobot
import time

robot = CamJamKitRobot()

leftms = 0.3
rightms = 0.3

robot.value = (leftms, rightms)

time.sleep(3)

robot.stop()