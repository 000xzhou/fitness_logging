from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='/dash')

# main 
@dashboard_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')

# sub items inside main 
@dashboard_bp.route('/dashboard/recent_workouts/')
# @dashboard_bp.route('/dashboard/recent_workouts/<workout_id>')
def recent_workouts():
    return render_template('dashboard/recent_workouts.html')
    
@dashboard_bp.route('/dashboard/graphOfProgress')
def graphOfProgress():
    return render_template('dashboard/graphOfProgress.html')
    
@dashboard_bp.route('/dashboard/chartofOveralls')
def chartofOveralls():
    return render_template('dashboard/chartofOveralls.html')