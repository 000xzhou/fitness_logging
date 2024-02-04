from flask import Blueprint, render_template, request

workout_schedule_bp = Blueprint('workout_schedule_bp', __name__,
    template_folder='templates', static_folder='static')

@workout_schedule_bp.route('<user_email>', methods=['GET', 'POST'])
def user_schedule(user_email):
    # show full caluder with the workouts and abilty to edit
    return render_template("schedule.html")

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