#!/usr/bin/python3
'''
author: alex_irungu
technical interview: Dviz: edmunds.
'''
from flask_wtf import FlaskForm

from wtforms import IntegerField,StringField,SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
	#-.user input zip.
	zip = StringField('Enter Zip',validators=[DataRequired()])
	#-.user input radius.
	radius = StringField('Enter Radius',validators=[DataRequired()])
	submit = SubmitField('Submit')