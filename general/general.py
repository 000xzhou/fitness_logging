from flask import Blueprint, render_template, redirect, session, url_for
from models import User
from general.forms import UserForm


general_bp = Blueprint('general_bp', __name__,
    template_folder='templates',)

@general_bp.route('/')
def index():
    if 'user' in session:
        return redirect(url_for("dashboard_bp.dashboard", user_email=session['user']))
    return render_template("general/index.html")
    
@general_bp.route('/settings')
def settings():
    if 'user' not in session:
        return redirect("/")
    user = User.query.get_or_404(session['user'])
    form = UserForm(obj = user)
    if form.validate_on_submit():
        return render_template("general/settings.html")
    return render_template("general/settings.html", form=form)