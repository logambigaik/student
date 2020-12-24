import os
from flask import Flask
from flask_sqlalchemy import *

db=SQLAlchemy()

class Airlines(db.Model):
    __tablename__="airline"
    id=db.Column(db.Integer,primary_key=True)
    origin=db.Column(db.String,nullable=False)
    destination=db.Column(db.String,nullable=False)
    duration=db.Column(db.Integer,nullable=False)
    passenger=db.relationship("Customers",backref="airlines",lazy=True)  #Class relation

    def add_customer(self,name):
        p=Customers(name=name,flight_id=self.id)
        db.session.add(p)
        db.session.commit()

class Customers(db.Model):
    __tablename__="customer"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    flight_id =db.Column(db.Integer,db.ForeignKey("airline.id"),nullable=False)
