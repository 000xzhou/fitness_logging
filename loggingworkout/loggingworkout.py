from flask import Blueprint, render_template, request, session
from models import WorkoutPlan, ExerciseLog, db, Workoutsession, ExerciseName
import json
from datetime import datetime


logging_workout_bp = Blueprint('logging_workout_bp', __name__,
    template_folder='templates', static_folder='static')

@logging_workout_bp.route('/<plan_id>', methods=['GET', 'POST'])
def workout_page(plan_id):
    plan = WorkoutPlan.query.get_or_404(plan_id)
    # if "workoutSession" not in session: 
        # expiration_time = datetime.now().replace(hour=23, minute=59, second=59)
        # session till they leave the page.

        # session.permanent_session_lifetime = expiration_time - datetime.now()
        
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
    exercise_id = data.get("workout-id")
    cardio_time = data.get("cardio_timer")

    # if they press the big save button
    # need to array though each exercise
    workoutsession = Workoutsession(
                    user_id = session['user'],
                    date_logged=datetime.now(),
                    exercise_name=exercise_name, 
                    exercise_id=exercise_id,
                    )
    
    db.session.add(workoutsession)
    db.session.commit()
    # log for each exercise 
    log = ExerciseLog( 
                    set_num=set_num, 
                    repetitions=repetitions,
                    weight=weight, 
                    cardio=cardio, 
                    cardio_time = cardio_time,
                    )
    db.session.add(log)
    db.session.commit()
        
    return log.id

@logging_workout_bp.route('/editlogworkout', methods=['GET', 'POST'])
def editlogworkout():
    
    log = ExerciseLog.query.get_or_404()
    
    data = json.loads(request.data.decode('utf-8'))
    log.repetitions = data.get('repetitions')
    log.weight = data.get('weight')
    log.cardio = data.get('cardio')
    log.cardio_time = data.get("cardio_timer")
    db.session.commit()
    return "Workout edited"