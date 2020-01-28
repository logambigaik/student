from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/loga")
def loga():
    return "Hello, Loga!"
