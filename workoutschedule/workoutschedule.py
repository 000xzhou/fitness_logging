from flask import Blueprint, render_template

workout_schedule_bp = Blueprint('workout_schedule_bp', __name__,
    template_folder='templates', static_folder='static')

@workout_schedule_bp.route('<user_email>')
def dashboard(user_email):
    return 