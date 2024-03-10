from flask import Blueprint, render_template, request, session, redirect, url_for,jsonify
from models import WorkoutPlan, db,ExerciseInPlan
from workoutschedule.forms import ScheduleForm
from sqlalchemy import desc
import calendar
import datetime


workout_schedule_bp = Blueprint('workout_schedule_bp', __name__,
    template_folder='templates', static_folder='static', static_url_path='/schedule')


def generate_calendar(year, month, events):
    calendar_data = []
    cal = calendar.Calendar(calendar.SUNDAY)
    for week in cal.monthdatescalendar(year, month):
        week_data = []
        for day in week:
            day_events = events.get(day, [])
            week_data.append({'date': day, 'events': day_events})
        calendar_data.append(week_data)
    return calendar_data

@workout_schedule_bp.route('/calendar', methods=['GET', 'POST'])
def user_calendar():
    events = {
    datetime.date(2024, 3, 14): ["Event 1", "Event 2"],
    datetime.date(2024, 3, 22): ["Event 3"],
    }

    today = datetime.date.today()
    calendar_data = generate_calendar(today.year, today.month, events)

    return render_template("calendar.html", calendar_data=calendar_data)

# =========================== START add edit delete details schedule START ============================================
@workout_schedule_bp.route('/', methods=['GET', 'POST'])
def user_schedule():
    """ Gives user a list of their schedule."""
    if 'user' not in session:
        return redirect(url_for('auth_bp.login'))
    
    schedules = WorkoutPlan.query.filter_by(user_id=session['user']).order_by(desc(WorkoutPlan.created_at)).all()

    return render_template("schedule.html", schedules=schedules)

@workout_schedule_bp.route('/add_schedule', methods=['GET', 'POST'])
def add_schedule():
    """ Let user add a schedule."""
    if 'user' not in session:
        return redirect(url_for('auth_bp.login'))
    
    if request.method == 'GET':
        return render_template("workoutplan/add_schedule_form.html")
    
    new_plan = WorkoutPlan(**request.json['formData'], user_id=session['user'])
    db.session.add(new_plan)
    db.session.commit() 
    return render_template("workoutplan/add_schedule.html", schedule=new_plan)

@workout_schedule_bp.route('/edit_schedule/<id>', methods=['GET', 'PATCH'])
def edit_schedule(id):
    """ Let user edit a schedule."""
    if 'user' not in session:
        return redirect(url_for('auth_bp.login'))
    
    schedule = WorkoutPlan.query.get_or_404(id)    
        
    if request.method == 'GET':
        return render_template("workoutplan/edit_schedule_form.html", schedule=schedule)
    
    data = request.json['formData']
    schedule.name = data["name"]
    schedule.description = data['description']
    schedule.repeat = data['repeat']
    schedule.date = data['date']
    schedule.mon = data['mon']
    schedule.tue = data['tue']
    schedule.wed = data['wed']
    schedule.thur = data['thur']
    schedule.fri = data['fri']
    schedule.sat = data['sat']
    schedule.sun = data['sun']
    db.session.commit() 
    return render_template("workoutplan/edit_schedule.html", schedule=schedule)

@workout_schedule_bp.route('/delete_schedule', methods=['POST'])
def delete_schedule():
    """ Let user delete a schedule."""
    if 'user' not in session:
        return redirect(url_for('auth_bp.login'))
    
    id = request.json["id"]
    plan = WorkoutPlan.query.get_or_404(id)
    db.session.delete(plan)
    db.session.commit()
    return jsonify({'message': 'Schedule deleted successfully'})


@workout_schedule_bp.route('/<id>', methods=['GET', 'POST'])
def schedule_detail(id):
    """ Gives user a deatil of their schedule."""
    if 'user' not in session:
        return redirect(url_for('auth_bp.login'))
    
    schedule = WorkoutPlan.query.get_or_404(id)
    if schedule.user_id != session['user']:
        return redirect(url_for('dashboard_bp.dashboard'))
    return render_template("schedule_details.html", schedule=schedule)

# =========================== END add edit delete details schedule END ============================================



@workout_schedule_bp.route('today/<user_email>', methods=['GET', 'POST'])
def user_today_schedule(user_email):
    # return exerises for today (show up on dashboard)
    return render_template("today.html")


@workout_schedule_bp.route('addExericeToSchedule', methods=['GET', 'POST'])
def addExericeToSchedule():
    plan_id = request.json['workoutPlanId']
    name = request.json['name']
    exercise_id = request.json['exercise_id']
    new_exercise = ExerciseInPlan(plan_id=plan_id, 
                                  exercise_id=exercise_id, 
                                  exercise_name=name,
                                  sets = 3,
                                  repetitions = 3,
                                  weight = 10
                                  )
    db.session.add(new_exercise)
    db.session.commit()
    return jsonify({'message': f'Workout plan {new_exercise.id} status added successfully'})



@workout_schedule_bp.route('removeExericeToSchedule', methods=['GET', 'POST'])
def removeExericeToSchedule():
    id = request.json['exerciseInPlanId']
    exercise_to_delete = ExerciseInPlan.query.get(id)
    db.session.delete(exercise_to_delete)
    db.session.commit()
    return jsonify({'message': 'Workout plan status remove successfully'})

@workout_schedule_bp.route('checkInSchedule', methods=['GET', 'POST'])
def checkInSchedule():
    planid = request.json['planid']
    exericename = request.json['exericename']
    existing_entry = ExerciseInPlan.query.filter_by(exercise_name=exericename, plan_id=planid).first()
    if existing_entry:
        return jsonify({'success': True, 'message': f'{existing_entry.id}'})
    else:
        return jsonify({'success': False})