from gpiozero import CamJamKitRobot
import time

robot = CamJamKitRobot()

leftms = 0.5
rightms = 0.5

robot.value = (leftms, rightms)

time.sleep(5)

robot.stop()