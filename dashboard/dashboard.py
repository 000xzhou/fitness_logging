from flask import Blueprint, render_template, session, redirect
from models import User, WorkoutPlan, Workoutsession, db, ExerciseName, ExerciseLog
from sqlalchemy import or_
from datetime import datetime, timedelta
import json

dashboard_bp = Blueprint('dashboard_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='/dash')

# main 
@dashboard_bp.route('/')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    
    user = User.query.get_or_404(session['user'])
    
    today = datetime.now().weekday()
    
    day_to_attr = {
    0: WorkoutPlan.mon,
    1: WorkoutPlan.tue,
    2: WorkoutPlan.wed,
    3: WorkoutPlan.thur,
    4: WorkoutPlan.fri,
    5: WorkoutPlan.sat,
    6: WorkoutPlan.sun
    }
    today_workout = (
        WorkoutPlan.query
        .filter(WorkoutPlan.user_id == session['user'])
        .filter(
            or_(
                (WorkoutPlan.repeat == "weekly") & (day_to_attr[today] == True),  # Weekly plans scheduled for today
                (WorkoutPlan.repeat != "weekly") & (WorkoutPlan.date == datetime.now().date()),  # Non-weekly plans scheduled for today
            )
        )
        .first()
    )
    return render_template('dashboard.html',user=user, workout = today_workout)

# sub items inside main 
@dashboard_bp.route('/recent_workouts/')
def recent_workouts():
    log = (db.session.query(Workoutsession)
           .filter(Workoutsession.user_id == session['user'])
           .order_by(Workoutsession.date_logged.desc())
           .first()
           )

    today = datetime.now().date()

    return render_template('dashboard/recent_workouts.html',  today=today, log=log)

@dashboard_bp.route('/recent_workouts/all')
def all_recent_workouts():
    log = (db.session.query(Workoutsession)
           .filter(Workoutsession.user_id == session['user'])
           .order_by(Workoutsession.date_logged.desc())
           .all()
           )

    today = datetime.now().date()

    return render_template('dashboard/all_recent_workouts.html',  today=today, log=log)
    
@dashboard_bp.route('/graphOfProgress')
def graphOfProgress():
    return render_template('dashboard/graphOfProgress.html')

@dashboard_bp.route('/graphOfProgress/data')
def graphOfProgress_data():
    data = (db.session.query(ExerciseName)
           .filter(Workoutsession.user_id == session['user'])
           .all()
           )
    
    formatted_data = {}

    for entry in data:
        exercise_name = entry.exercise_name
        date_logged = entry.name.date_logged.date().isoformat()
        max_weight = max(details.weight or details.cardio for details in entry.log)
        # name : {date: weight} try this 
        # formatted_data[date_logged] = [exercise_name, max_weight]
        if exercise_name not in formatted_data:
            formatted_data[exercise_name] = {}
        if date_logged not in formatted_data[exercise_name]:
            formatted_data[exercise_name][date_logged] = max_weight
        else:
            formatted_data[exercise_name][date_logged] = max(max_weight, formatted_data[exercise_name][date_logged])
        # print(formatted_data)
    return json.dumps(formatted_data)


@dashboard_bp.route('/chartofOveralls')
def chartofOveralls():
    return render_template('dashboard/chartofOveralls.html')

@dashboard_bp.route('/chartofOveralls/data')
def chartofOveralls_data():
    log = (db.session.query(Workoutsession)
           .filter(Workoutsession.user_id == session['user'])
           .all()
           )
    overalls = {}
    
    for names in log:
        for name in names.name:
            if name.exercise_name in overalls:
                overalls[name.exercise_name] += 1
            else:
                overalls[name.exercise_name] = 1

    return json.dumps(overalls)
