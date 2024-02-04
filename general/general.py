from flask import Blueprint, render_template, redirect, session, url_for

general_bp = Blueprint('general_bp', __name__,
    template_folder='templates',)

@general_bp.route('/')
def index():
    if 'user' in session:
        return redirect(url_for("dashboard_bp.dashboard"))
    return render_template("general/index.html")
    