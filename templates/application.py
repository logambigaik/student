from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
## def index():
##    return render_template("index.html")

def index():
    headline="Breaking News"
    return render_template("index.html",headline=headline)

@app.route("/bye")
def bye():
    headline="GoodBye"
    return render_template("index.html",headline=headline)
