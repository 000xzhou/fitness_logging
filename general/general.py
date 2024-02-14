from flask import Blueprint, render_template, redirect, session, url_for, request
from models import User, db
from general.forms import UserForm


general_bp = Blueprint('general_bp', __name__,
    template_folder='templates',)

@general_bp.route('/')
def index():
    if 'user' in session:
        return redirect(url_for("dashboard_bp.dashboard", user_email=session['user']))
    return render_template("general/index.html")
    
@general_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    if 'user' not in session:
        return redirect("/")

    user = User.query.get_or_404(session['user'])
    form = UserForm(obj = user)
    
    if form.validate_on_submit():
        user.email = form.email.data
        user.reminder = form.reminder.data
        user.weightunit = form.weightunit.data
        db.session.commit()
        return render_template("general/settings.html", form=form)
    
    return render_template("general/settings.html", form=form)