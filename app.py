import googlemaps
from datetime import datetime
from flask import Flask, render_template, url_for, flash, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from forms import SubmitForm
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

import geopy

from geopy.geocoders import Nominatim

csrf = CSRFProtect()
app = Flask(__name__, static_folder="statics")
app.config.from_object(Config)
app.secret_key = "\x91\xb0*=\xd2Z\xa4\xca<\x9e\xb2F\xbfj\x11"
csrf.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    accuracy = db.Column(db.Float, nullable=True)
    class_complaint = db.Column(db.Integer)
    short_describtion = db.Column(db.String(280))
    long_describtion = db.Column(db.String)


gmaps = googlemaps.Client(key="AIzaSyDXQCAC5ShdlDdCacVs5eXKglPzuJNMQ9U")


@app.route("/", methods=["POST", "GET"])
def index():
    form = SubmitForm()
    if request.method == "GET":
        return render_template("index.html", form=form)

    if form.validate_on_submit():
        print(form.validate())
        print("It is working.")
        q = Complaint()
        q.lat = form.lat.data
        q.long = form.long.data
        # q.accuracy = form.accuracy.data
        q.short_describtion = form.short_describtion.data
        q.long_describtion = form.long_describtion.data
        db.session.add(q)
        db.session.commit()
        flash("Thank you so much for your submission!")
        address = get_address(form.lat.data, form.long.data)
    else:
        print("Where to fuck i fucked up.")
        for error in form.errors.items():
            flash(error)

    return render_template("index.html", form=form, address=address)


def get_location(lat: str, long: str) -> geopy.location.Location:
    "A raw structured format for the user submitted reverese location."
    geo = Nominatim(user_agent="istole_website")
    location = geo.reverse(f"{lat}, {long}")
    return location


def get_address(lat: str, long: str) -> str:
    "A str representation for the user's location"
    location = get_location(lat, long)
    return location.address
