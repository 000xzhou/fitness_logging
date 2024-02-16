from flask import Blueprint, render_template, session, redirect
from models import User, WorkoutPlan, ExerciseLog
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
    return render_template('dashboard.html',user=user, workout = today_workout)

# sub items inside main 
@dashboard_bp.route('/recent_workouts/')
def recent_workouts():
    log = (
        ExerciseLog.query
          .join(User)
          .filter(User.email == session['user'])
          .filter(ExerciseLog.date_logged >= datetime.now().date()  - timedelta(days=1))
          .group_by(ExerciseLog.plan_id, ExerciseLog.id)
          .order_by(ExerciseLog.date_logged.desc())
    )
    
    groups = {}
    date = {}
    for e in log:
        if e.plan_id not in groups:
            groups[e.plan_id] = []
            date[e.plan_id] = e.date_logged.date()
        groups[e.plan_id].append(e)
        
    today = datetime.now().date()
    # print(f"{groups=}")
    # print(f"{date=}")
    return render_template('dashboard/recent_workouts.html', log=groups, dates=date, today=today)
    
@dashboard_bp.route('/graphOfProgress')
def graphOfProgress():
    return render_template('dashboard/graphOfProgress.html')
    
@dashboard_bp.route('/chartofOveralls')
def chartofOveralls():
    return render_template('dashboard/chartofOveralls.html')

