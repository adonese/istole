import googlemaps
from datetime import datetime
from flask import Flask, render_template, url_for, flash, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from forms import SubmitForm
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

csrf = CSRFProtect()
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = '\x91\xb0*=\xd2Z\xa4\xca<\x9e\xb2F\xbfj\x11'
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

@app.route('/', methods=["POST", "GET"])
def index():
    form = SubmitForm()
    print(form.validate())
    print(form.lat.data)
    print(form.long.data)
    print(form.accuracy.data)

    print(form.short_describtion.data)
    print(form.submit.data)

    print(form.long_describtion.data)
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
        flash("Thank you so much for your response. Would you prefer a pepsi, or coca cola? Minicare is not allowed though.")
    else:
        print("Where to fuck i fucked up.")
        for error in form.errors.items():
            flash(error)

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
    
