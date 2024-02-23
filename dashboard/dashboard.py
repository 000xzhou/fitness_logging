from flask import Blueprint, render_template, session, redirect
from models import User, WorkoutPlan, Workoutsession, ExerciseLog
from sqlalchemy import or_
from datetime import datetime, timedelta

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
    return render_template('dashboard.html',user=user)

# sub items inside main 
@dashboard_bp.route('/recent_workouts/')
def recent_workouts():
    # log = (
    #     Workoutsession.query
    #       .join(User)
    #       .filter(User.email == session['user'])
    #       .order_by(Workoutsession.date_logged.desc())
    #       .all()
    # )
    
    # names = (
    #     Workoutsession.query
    #       .join(User)
    #       .join(ExerciseLog)
    #       .filter(User.email == session['user'])
    #       .group_by(ExerciseLog.exercise_name, Workoutsession.id)
    #       .order_by(Workoutsession.date_logged.desc())
    #       .all()
    # )

    today = datetime.now().date()
    # print(f"{groups=}")
    # print(f"{date=}")
    return render_template('dashboard/recent_workouts.html',  today=today)
    
@dashboard_bp.route('/graphOfProgress')
def graphOfProgress():
    return render_template('dashboard/graphOfProgress.html')
    
@dashboard_bp.route('/chartofOveralls')
def chartofOveralls():
    return render_template('dashboard/chartofOveralls.html')

