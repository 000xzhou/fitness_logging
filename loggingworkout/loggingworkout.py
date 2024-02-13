from flask import Blueprint, render_template, request
from models import WorkoutPlan

logging_workout_bp = Blueprint('logging_workout_bp', __name__,
    template_folder='templates', static_folder='static')

@logging_workout_bp.route('/', methods=['GET', 'POST'])
def logging_main_page():
    # in logging workout page. after pressing start to start workout
    return render_template("base.html")

@logging_workout_bp.route('/<plan_id>', methods=['GET', 'POST'])
def logging_exercise(plan_id):
    # get WorkoutPlan (plan_id) then get all the ExerciseInPlan in it... one at a time
    plan = WorkoutPlan.query.get_or_404(plan_id)
    return render_template("loggingworkout/workoutpage.html", plan = plan)

@logging_workout_bp.route('/add', methods=['GET', 'POST'])
def add_exerciselog():
    # in logging workout page. add finish workout in db
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # user_id = db.Column(db.Text, db.ForeignKey('users.email'))
    # exercise_name = db.Column(db.Text, unique=True, nullable=False)
    # sets = db.Column(db.Integer, nullable=True)
    # repetitions = db.Column(db.Integer, nullable=True)
    # weight = db.Column(db.Integer, nullable=True)
    # cardio = db.Column(db.Integer, nullable=True)
    # notes = db.Column(db.Text, nullable=True)
    # date_logged = db.Column(db.DateTime)) => the date they picked need ot change that in model. required
    return render_template("base.html")