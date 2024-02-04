from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import InputRequired, Email

class UserForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    reminder = BooleanField('Email Reminder')
    weightunit = SelectField('Weight Unit', choices=[('metric', 'Metric'), ('imperial', 'Imperial')])
    submit = SubmitField('Save')
    