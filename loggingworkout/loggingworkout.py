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
    set_values = data['setValues']
    exercise_id = data['exerciseId']
    duration = data['duration']
    notes = data.get('notes')
    workoutsession_params = {
        'user_id': session['user'],
        'date_logged': datetime.now(),
        'duration': duration
    }
    # add notes if there is notes 
    if notes:
        workoutsession_params['notes'] = notes
        
    workoutsession = Workoutsession(**workoutsession_params)
    db.session.add(workoutsession)
    db.session.commit()
    
    for exercise_name, value in set_values.items():
        name = ExerciseName(
                exercise_name = exercise_name, 
                exercise_id = exercise_id[exercise_name],
                workout_id = workoutsession.id
        )
        db.session.add(name)
        db.session.commit()
    
        for set, v in value.items():
            (repsTimer, repsTimer_value), (weightCardio,weightCardio_value) = v.items()
            if repsTimer == "repetitions":
                log = ExerciseLog(
                    set_num = int(set), 
                    repetitions = int(repsTimer_value),
                    weight = int(weightCardio_value),
                    exercise_name_id = name.id
                )
            else:
                log = ExerciseLog(
                    set_num = int(set), 
                    cardio_time = int(repsTimer_value),
                    cardio = int(weightCardio_value),
                    exercise_name_id = name.id
                )
            db.session.add(log)
            db.session.commit()

    return f'{workoutsession.id}'
