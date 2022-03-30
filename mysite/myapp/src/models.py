#from django.db import models
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()



class Driver(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email_address = db.Column(db.String, unique=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    driver = db.relationship("driver", backref='Drivers')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username: str, password: str, email_address: str):
            self.username = username
            self.password = password
            self.email_address = email_address




    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email address': self.email_address
        }


    def Drivers():
        title = "Drivers List"

        if request.method == "POST":
            driver_name = request.form['name']
            new_driver = Drivers(name=driver_name)

            try:
                db.session.add(new_driver)
                db.session.commit()
                return redirect('/Drivers')
            except:
                return "There was an error adding the Driver"
        else:
            Drivers = Drivers.query.order_by(Drivers.date_created)
            return render_template(title=title)

class Cars(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    license = db.Column(db.String(1), nullable=False)
    year = db.Column(db.Integer)
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'))
    car = db.relationship("Car", backref='Cars')
    race = db.relationship("Races", backref=db.backref("Races", uselist=False))

    def __init__(self, license: str, year: int, make: str, model: str):
            self.license = license
            self.year = year
            self.make = make
            self.model = model

    def serialize(self):
        return {
            'id': self.id,
            'license': self.license,
            'year': self.year,
            'make': self.make,
            'model': self.model
        }

class Races(db.Model):
    __tablename__ = 'races'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    starting_position = db.Column(db.Integer, unique=True, nullable=False)
    ending_position = db.Column(db.Integer, unique=True, nullable=False)
    qualifying_time = db.Column(db.Integer)
    average_lap_times = db.Column(db.Integer, nullable=False)
    best_lap_time = db.Column(db.Integer, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    car = db.relationship("Car", backref='Cars')

    def __init__(self, starting_position: int, ending_position: int, qualifying_time: int, average_lap_times: int, best_lap_time: int):
             self.starting_position = starting_position
             self.ending_position = ending_position
             self.qualifying_time = qualifying_time
             self.average_lap_times = average_lap_times
             self.best_lap_time = best_lap_time

    def serialize(self):
        return {
            'id': self.id,
            'starting position': self.starting_position,
            'ending position': self.ending_position,
            'qualifying time': self.qualifying_time,
            'average lap times': self.average_lap_times,
            'best lap time': self.best_lap_time
        }

race_table = db.Table(
    'starting_position',
    db.Column(
        'car_id', db.Integer,
        db.ForeignKey('cars.id'),
        primary_key=True
    ),

    db.Column(
        'driver_id', db.Integer,
        db.ForeignKey('drivers.id'),
        primary_key=True
    ),
)

class Incident(db.Model):
    __tablename__ = 'incident'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cars_involved = db.Column(db.Integer, nullable=False)
    number_of_incidents = db.Column(db.Integer, nullable=False)
    races_id = db.Column('race_id', db.Integer, db.ForeignKey('races.id'), nullable=False)
    race = db.relationship("Races", backref=db.backref("Races", uselist=False))

    def __init__(self, cars_involved: int, number_of_incidents: int, race_id):
            self.cars_involved = cars_involved
            self.number_of_incidents = number_of_incidents


    def serialize(self):
        return {
            'id': self.id,
            'cars involved': self.cars_involved,
            'number of incidents': self.number_of_incidents,
        }

