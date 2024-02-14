from flask import Blueprint, render_template, request, session
from models import WorkoutPlan

logging_workout_bp = Blueprint('logging_workout_bp', __name__,
    template_folder='templates', static_folder='static')

@logging_workout_bp.route('/<plan_id>', methods=['GET', 'POST'])
def workout_page(plan_id):
    plan = WorkoutPlan.query.get_or_404(plan_id)
    return render_template("loggingworkout/workoutpage.html", plan = plan)

@logging_workout_bp.route('/addsets', methods=['POST'])
def add_sets():
    num = request.json.get('num')
    set_type = request.json.get('set_type')
    set_num = int(num) + 1
    weight = request.json.get('weightInput')
    cardio = request.json.get('cardioInput')
    repetitions = request.json.get('repetitionsInput')
    return render_template("loggingworkout/addSet.html", set_num = set_num, set_type = set_type, weight=weight, cardio=cardio, reps = repetitions)
    
    
@logging_workout_bp.route('/logworkout', methods=['GET', 'POST'])
def logworkout():
    # in logging workout page. add finish workout in db
    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # user_id = db.Column(db.Text, db.ForeignKey('users.email'))
    # exercise_name = db.Column(db.Text, unique=True, nullable=False)
    # set_num = db.Column(db.Integer, nullable=True)
    # repetitions = db.Column(db.Integer, nullable=True)
    # weight = db.Column(db.Integer, nullable=True)
    # cardio = db.Column(db.Integer, nullable=True)
    # notes = db.Column(db.Text, nullable=True)
    # date_logged = db.Column(db.DateTime)) => the date they picked need ot change that in model. required   
    # exercise_name = db.Column(db.Text, nullable=False)
    # workout_id = db.Column(db.Integer, db.ForeignKey('exerciseinplans.id'))
    return render_template("base.html")