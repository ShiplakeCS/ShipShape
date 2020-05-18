import flask
from flask import Flask, redirect, render_template, url_for, make_response
app = Flask(__name__)
app.config["SECRET_KEY"] = "thisissupposedtobesecret!"

import code

robot = code.CamJamKitRobot()

@app.route("/main", methods=["GET","POST"])
def mainPage():
    return render_template("control.html")

@app.route("/")
def start():
    return "test"

@app.route("/robot/go/right")
def robotGoRight():
    global robot
    robot.right()
    return redirect("/main")

@app.route("/robot/go/left")
def robotGoLeft():
    global robot
    robot.left()
    return redirect("/main")

@app.route("/robot/go/forward")
def robotGoForward():
    global robot
    robot.forward()
    return redirect("/main")

@app.route("/robot/go/backward")
def robotGobackward():
    global robot
    robot.backward()
    return redirect("/main")

@app.route("/robot/go/stop")
def robotGoStop():
    global robot
    robot.stop()
    return redirect("/main")

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