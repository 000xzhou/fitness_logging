from flask import Blueprint, render_template, request

workout_schedule_bp = Blueprint('workout_schedule_bp', __name__,
    template_folder='templates', static_folder='static')

@workout_schedule_bp.route('<user_email>', methods=['GET', 'POST'])
def dashboard(user_email):
    name = request.args.get('name', default='', type=str)
    return render_template("schedule.html")