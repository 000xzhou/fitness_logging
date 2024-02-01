from flask import Blueprint, render_template, session, redirect, url_for
from auth.forms import LoginForm, RegisterForm
from models import db, User
from sqlalchemy.exc import IntegrityError


auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates', static_folder='static')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = User.is_authenticated(email, password)
        
        if user == "User does not exist":
            form.email.errors.append("User does not exist.")
            return render_template("auth/login.html", form=form)

        if user == "Wrong password":
            form.email.errors.append("Wrong password")
            return render_template("auth/login.html", form=form)
        
        session['user'] = user.email
        return "login"
    return render_template("auth/login.html", form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
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