from flask import Blueprint, render_template
from auth.forms import LoginForm, RegisterForm
from models import User


auth_blueprint = Blueprint('auth_blueprint', __name__,
    template_folder='templates',)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "login"
    return render_template("auth/login.html", form=form)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return "reg"
    return render_template("auth/register.html", form=form)