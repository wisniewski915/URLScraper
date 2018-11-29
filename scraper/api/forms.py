from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class HomeForm(FlaskForm):
	submit = SubmitField('Scrape Site')

#class HistoryForm(FlaskForm):
#	submit = SubmitField('New Entry')
