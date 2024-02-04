from flask import Flask
from models import db
from auth import auth
from general import general
from dashboard import dashboard
from exercises import exercises
from workoutschedule import workoutschedule

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()  

app.register_blueprint(auth.auth_bp)
app.register_blueprint(general.general_bp)
app.register_blueprint(dashboard.dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(exercises.exercises_bp, url_prefix='/exercises')
app.register_blueprint(workoutschedule.workout_schedule_bp, url_prefix='/schedule')

if __name__ == "__main__":
    app.run(debug=True)