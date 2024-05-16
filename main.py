from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)
status = "off"

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
        print(status)
        return render_template("index.html", state="On")

@app.route('/off', methods=['GET', 'POST'])
def off_page():
    if request.method == 'GET':
        return redirect(url_for("home"))
    else:
        status = "off"
        print(status)
        return render_template("index.html", state="Off")


if __name__=="__main__":
    app.run()