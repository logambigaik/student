from flask import Flask, render_template,request
from flask import jsonify
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql+psycopg2://postgres:19821983@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)


'''@app.route("/home")

def index():
    flights=Airlines.query.all()
    return render_template("index.html",flights=flights)

'''
@app.route("/book",methods=["POST"])
def book():
    """ Book a Flight """
    #Get form information

    name=request.form.get("name")

    try:
        flight_id = int(request.form.get("flight_id"))
    except Error:
        return render_template("error.html",message='Invalid Flight number')

    #Make sure the flight exists
    flight=Airlines.query.get(flight_id)
    if flight is None:
        return render_template("error.html",message='No such flight exists')

    #Add passenger.
    passenger=Customers(name=name,flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    return render_template("success.html")

@app.route("/")
def flights():
    """ List all the flights """
    flights=Airlines.query.all()
    return render_template("flights.html",flights=flights)

@app.route("/flights/<int:flight_id>")

def flight(flight_id):
    """ List details about a single flight """

    #Make sure flight exists
    flight=Airlines.query.get(flight_id)

    if flight is None:
        return render_template("error.html",message="No such flight exist")

    #Get all passenger
    passengers=flight.passenger   #Not required sql for selecting the passenger from tableinstead refering the class relation
    return render_template("flight.html",flight=flight,passengers=passengers)

@app.route("/api/flights/<int:flight_id>")

def flight_api(flight_id):
    """ List details about a single flight """

    #Make sure flight exists
    flight=Airlines.query.get(flight_id)

    if flight is None:
        return jsonify({"error":"Invalid flight_id"}),422

    #Get all passenger
    passengers=flight.passenger   #Not required sql for selecting the passenger from tableinstead refering the class relation
    names=[]
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify({
                    "origin" : flight.origin,
                    "destination" : flight.destination,
                    "duration" : flight.duration,
                    "passengers" : names
                    })
