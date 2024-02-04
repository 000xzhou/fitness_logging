from flask import Blueprint, render_template, session, redirect
from models import User

dashboard_bp = Blueprint('dashboard_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='/dash')

# main 
@dashboard_bp.route('/')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    user = User.query.get_or_404(session['user'])
    return render_template('dashboard.html',user=user)

# sub items inside main 
@dashboard_bp.route('/recent_workouts/')
# @dashboard_bp.route('/dashboard/recent_workouts/<workout_id>')
def recent_workouts():
    return render_template('dashboard/recent_workouts.html')
    
@dashboard_bp.route('/graphOfProgress')
def graphOfProgress():
    return render_template('dashboard/graphOfProgress.html')
    
@dashboard_bp.route('/chartofOveralls')
def chartofOveralls():
    return render_template('dashboard/chartofOveralls.html')