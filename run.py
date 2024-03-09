from flask import Flask
from models import db
from auth import auth
from general import general
from dashboard import dashboard
from exercises import exercises
from workoutschedule import workoutschedule
from loggingworkout import loggingworkout
from flask_mail import Mail
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
# w.e username and passowrd for the account I am going to use to send the email
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
mail = Mail(app)


db.init_app(app)
with app.app_context():
    db.create_all()  

app.register_blueprint(auth.auth_bp)
app.register_blueprint(general.general_bp)
app.register_blueprint(dashboard.dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(exercises.exercises_bp, url_prefix='/exercises')
app.register_blueprint(workoutschedule.workout_schedule_bp, url_prefix='/schedule')
app.register_blueprint(loggingworkout.logging_workout_bp, url_prefix='/logging')


if __name__ == "__main__":
    app.run(debug=True)