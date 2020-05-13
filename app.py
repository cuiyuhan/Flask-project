# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: yc3757
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/hello")
def hello():
    return render_template("index.html")

#static route
@app.route("/1006")
def exercise():
    return "1006 homepage"

#static route
@app.route("/")
def index():
    return render_template("main.html")

#static route
@app.route("/assignments")
def assignments():
    return render_template("assignment.html")

#static route
@app.route("/classes")
def classes():
    return "classes page"

#start the server
if __name__ == "__main__":
    app.run()
