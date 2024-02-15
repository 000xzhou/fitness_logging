from flask import Blueprint, render_template, request, session
from models import WorkoutPlan, ExerciseLog, db
import json

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
    data = json.loads(request.data.decode('utf-8'))
    set_num = data.get('set')
    repetitions = data.get('repetitions')
    weight = data.get('weight')
    cardio = data.get('cardio')
    exercise_name = data.get("name")
    workout_id = data.get("workout-id")
    plan_id = data.get("plan-id")
    log = ExerciseLog(user_id = session['user'], 
                      set_num=set_num, 
                      repetitions=repetitions,
                      weight=weight, 
                      cardio=cardio, 
                      exercise_name=exercise_name, 
                      workout_id=workout_id,
                      plan_id=plan_id)
    
    db.session.add(log)
    db.session.commit()
    return "Workout logged"