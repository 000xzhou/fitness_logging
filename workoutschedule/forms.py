# add-schedule

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired

# day_choices = [('mon','Monday'), ('tue','Tuesday')]

class ScheduleForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    is_weekly = BooleanField('Repeat Weekly')
    mon = BooleanField('Monday')
    tue = BooleanField('Tuesday')
    wed = BooleanField('Wednesday')
    thur = BooleanField('Thursday')
    fri = BooleanField('Friday')
    sat = BooleanField('Saturday')
    sun = BooleanField('Sunday')
