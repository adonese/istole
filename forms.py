from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField, FloatField, SelectMultipleField
from wtforms.validators import InputRequired
from flask_pagedown.fields import PageDownField


class SubmitForm(FlaskForm):
	short_describtion = TextAreaField(label="Short description", validators=[InputRequired()])
	long_describtion = PageDownField(label='Long Description')
	lat = FloatField(label="latitude", validators=[InputRequired()])
	long = FloatField(label="longitude", validators=[InputRequired()])
	accuracy = FloatField(label="accuracy")
	submit = SubmitField()