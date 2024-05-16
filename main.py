from flask import Flask, render_template, request, redirect, url_for
import time import sleep
from machine import Pin

app = Flask(__name__)
status = "off"
pin = Pin(25, Pin.OUT)

print(status)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/on', methods=['GET', 'POST'])
def on_page():
    if request.method == 'GET':
        
        return redirect(url_for("home"))
    else:
        status = "on"
        pin.toggle()
        print(status)
        return render_template("index.html", state="On")

@app.route('/off', methods=['GET', 'POST'])
def off_page():
    if request.method == 'GET':
        return redirect(url_for("home"))
    else:
        status = "off"
        pin.off()
        print(status)
        return render_template("index.html", state="Off")


if __name__=="__main__":
    app.run()