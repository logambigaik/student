import datetime

from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    names=['Archu','Loga','Ganesh']
    now=datetime.datetime.now()
    new_year=now.month == 1 and now.day == 1
    #return render_template("index.html",new_year=new_year,names=names)
    return render_template("index.html",names=names)
