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


@app.route("/drag")
def drag():
    return render_template("drag.html")

@app.route("/main", methods=["GET","POST"])
def mainPage():
    return render_template("control.html")

@app.route("/")
def start():
    return render_template("control.html")

@app.route("/robot/go/right", methods=["GET", "POST"])
def robotGoRight():
    global robot

    robot.value = (leftms, -rightms)
    time.sleep(1)
    robot.stop()
    if request.method == "GET":
        return redirect("/main")
    else:
        return "200"

@app.route("/robot/go/left", methods=["GET", "POST"])
def robotGoLeft():
    global robot
    robot.value = (-leftms, rightms)
    time.sleep(1)
    robot.stop()
    if request.method == "GET":
        return redirect("/main")
    else:
        return "200"

@app.route("/robot/go/forward", methods=["GET", "POST"])
def robotGoForward():
    global robot
    robot.value = (leftms, rightms)
    #time.sleep(1)
    #robot.stop()
    if request.method == "GET":
        return redirect("/main")
    else:
        return "200"

@app.route("/robot/go/backwards", methods=["GET", "POST"])
def robotGobackward():
    global robot
    robot.value = (-leftms, -rightms)
    time.sleep(1)
    robot.stop()
    if request.method == "GET":
        return redirect("/main")
    else:
        return "200"

@app.route("/robot/go/stop", methods=["GET", "POST"])
def robotGoStop():
    global robot
    robot.stop()
    #time.sleep(0.1)
    
    if request.method == "GET":
        return redirect("/main")
    else:
        return "200"

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
