import flask, time
from flask import Flask, redirect, render_template, url_for, make_response, request
app = Flask(__name__)
app.config["SECRET_KEY"] = "thisissupposedtobesecret!"

from gpiozero import CamJamKitRobot, DistanceSensor

pinTrigger = 17
pinEcho = 18
distanceToStop = 0.2
leftms = 0.3
rightms = 0.35
robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinEcho,trigger=pinTrigger)


@app.route("/main", methods=["GET","POST"])
def mainPage():
    return render_template("control.html")

@app.route("/")
def start():
    return render_template("control.html")

@app.route("/robot/go/right")
def robotGoRight():
    global robot
    while True:
        if sensor.distance >= distanceToStop:
            robot.value = (leftms, -rightms)
        else:
            robot.stop()
            break
        time.sleep(0.1)
    if request.method == "GET":
        return redirect("/main")
    else:
        return 200

@app.route("/robot/go/left")
def robotGoLeft():
    global robot
    while True:
        if sensor.distance >= distanceToStop:
            robot.value = (-leftms, rightms)
        else:
            robot.stop()
            break
        time.sleep(0.1)
    if request.method == "GET":
        return redirect("/main")
    else:
        return 200

@app.route("/robot/go/forward", methods=["GET", "POST"])
def robotGoForward():
    global robot
    while True:
        if sensor.distance >= distanceToStop:
            robot.value = (leftms, rightms)
        else:
            robot.stop()
            break
        time.sleep(0.1)
    if request.method == "GET":
        return redirect("/main")
    else:
        return 200

@app.route("/robot/go/backward")
def robotGobackward():
    global robot
    while True:
        if sensor.distance >= distanceToStop:
            robot.value = (-leftms, -rightms)
        else:
            robot.stop()
            break
        time.sleep(0.1)
    if request.method == "GET":
        return redirect("/main")
    else:
        return 200

@app.route("/robot/go/stop")
def robotGoStop():
    global robot
    robot.stop()
    time.sleep(0.1)
    
    if request.method == "GET":
        return redirect("/main")
    else:
        return 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")
"""

import threading
import time

def doSomething():
    print("Hello")


t1 = threading.Thread(target=doSomething)
t2 = threading.Thread(target=doSomething)

t1.start()
t2.start()
"""
