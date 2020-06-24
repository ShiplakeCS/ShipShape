import flask, time
from flask import Flask, redirect, render_template, url_for, make_response, request, session
app = Flask(__name__)
app.config["SECRET_KEY"] = "thisissupposedtobesecret!"

from gpiozero import CamJamKitRobot, DistanceSensor

pinTrigger = 17
pinEcho = 18
distanceToStop = 0.2
leftms = 0.6
rightms = 0.6
robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinEcho,trigger=pinTrigger)

@app.route("/drag")
def drag():
    if 'power' not in session:
        session['power'] = 0.5
    return render_template("drag.html")

@app.route("/main", methods=["GET","POST"])
def mainPage():
    return render_template("control.html")

@app.route("/")
def start():
    if 'power' not in session:
        session['power'] = 0.5
    return render_template("drag.html")

@app.route("/robot/go/right", methods=["GET", "POST"])
def robotGoRight():
    global robot, leftms, rightms
    robotPowerLevel = session['power']
    print("Right - power: " + str(session['power']))
    robot.value = (leftms * robotPowerLevel, -rightms * robotPowerLevel)

    if request.method == "GET":
        return redirect("/main")
    else:
        return "200"

@app.route("/robot/go/left", methods=["GET", "POST"])
def robotGoLeft():
    global robot, leftms, rightms
    robotPowerLevel = session['power']
    print("Left - power: " + str(session['power']))
    robot.value = (-leftms * robotPowerLevel, rightms * robotPowerLevel)

    if request.method == "GET":
        return redirect("/main")
    else:
        return "200"

@app.route("/robot/go/forward", methods=["GET", "POST"])
def robotGoForward():
    global robot,leftms, rightms
    print("Forward - power: " + str(session['power']))
    robotPowerLevel = session['power']
    robot.value = (leftms*robotPowerLevel, rightms*robotPowerLevel)

    if request.method == "GET":
        return redirect("/main")
    else:
        return "200"

@app.route("/robot/go/backwards", methods=["GET", "POST"])
def robotGoBackward():
    global robot, leftms, rightms
    robotPowerLevel = session['power']
    print("Backwards - power: " + str(session['power']))
    robot.value = (-leftms*robotPowerLevel, -rightms*robotPowerLevel)

    if request.method == "GET":
        return redirect("/main")
    else:
        return "200"


@app.route("/robot/set/power/<level>", methods=["GET", "POST"])
def setRobotPower(level):
    print(level)
    if level == "high":
        session['power'] = 1

    if level == "medium":
        session['power'] = 0.5

    if level == "low":
        session['power'] = 0.25
    
    return str(session['power'])


@app.route("/robot/go/stop", methods=["GET", "POST"])
def robotGoStop():
    global robot
    robot.stop()
    print("Received instruction to STOP")
    #time.sleep(0.1)
    
    if request.method == "GET":
        return redirect("/main")
    else:
        return "200"
        
        
@app.route("/data/distance", methods=['POST', 'GET'])
def getDistance():
    global sensor
    return str(sensor.distance * 100)
    

@app.route("/data/power", methods=['POST', 'GET'])
def getPower():
    return str(session['power'])


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
