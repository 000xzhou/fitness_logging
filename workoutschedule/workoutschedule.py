from flask import Blueprint, render_template, request, session, redirect, url_for,jsonify
import json
from models import WorkoutPlan, db

workout_schedule_bp = Blueprint('workout_schedule_bp', __name__,
    template_folder='templates', static_folder='static', static_url_path='/schedule')

@workout_schedule_bp.route('/calendar', methods=['GET', 'POST'])
def user_calendar():
    # show full calendar with the workouts and abilty to edit
    return render_template("calendar.html")

@workout_schedule_bp.route('/', methods=['GET', 'POST'])
def user_schedule():
    # show full schedule with the workouts and abilty to edit
    schedules = WorkoutPlan.query.all()

    return render_template("schedule.html", schedules=schedules)

@workout_schedule_bp.route('/add_schedule', methods=['POST'])
def add_schedule():
    if 'user' not in session:
        return redirect(url_for('auth_bp.login'))
    
    data = json.loads(request.data)
    name = data.get('name')
    description = data.get('description')
    new_plan = WorkoutPlan(name=name, description=description, user_id = session['user'])
    db.session.add(new_plan)
    db.session.commit() 
    return render_template("workoutplan/add_schedule.html", schedule=new_plan)

@workout_schedule_bp.route('/delete_schedule', methods=['POST'])
def delete_schedule():
    if 'user' not in session:
        return redirect(url_for('auth_bp.login'))
    
    data = json.loads(request.data)
    id = data.get('id')
    plan = WorkoutPlan.query.get_or_404(id)
    db.session.delete(plan)
    db.session.commit()
    return jsonify({'message': 'Schedule deleted successfully'})


@workout_schedule_bp.route('/add_exercise', methods=['GET', 'POST'])
def add_exercise():
    # will popup a searchbar to search exercise to add (from calendar page) after pressing add button
    name = request.args.get('name', default='', type=str)
    return "Adding"

@workout_schedule_bp.route('/delete_exercise', methods=['POST'])
def delete_exercise():
    # will popup a searchbar to search exercise to delete (from calendar page) after pressing delete button
    return "deleted"

@workout_schedule_bp.route('today/<user_email>', methods=['GET', 'POST'])
def user_today_schedule(user_email):
    # return exerises for today (show up on dashboard)
    return render_template("today.html")