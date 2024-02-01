from flask import Blueprint, render_template, session, redirect, url_for
from auth.forms import LoginForm, RegisterForm
from models import db, User
from sqlalchemy.exc import IntegrityError


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
        email = form.email.data
        password = form.password.data
        new_user = User.register(email, password)
        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            # Add an error message to the form
            form.email.errors.append('email is taken, please login or pick another')
            return render_template("auth/register.html", form=form)

        session['user'] = new_user.email
        return "you login"
        # return redirect(url_for('index'))

    return render_template("auth/register.html", form=form)