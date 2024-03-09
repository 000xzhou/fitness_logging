from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from auth.forms import LoginForm, RegisterForm, PasswordReset, NewPassword
from models import db, User
from sqlalchemy.exc import IntegrityError
from flask_mail import Mail, Message
import os


auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates', static_folder='static')

mail = Mail()

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
        session['weightunit'] = user.weightunit
        return redirect(url_for("dashboard_bp.dashboard"))
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
        session['weightunit'] = new_user.weightunit
        return redirect(url_for("dashboard_bp.dashboard"))

    return render_template("auth/register.html", form=form)

@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user', None)
    return redirect("/")
    
@auth_bp.route('/resetpassword', methods=['GET', 'POST'])
def resetPassword():
    form = PasswordReset()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        token = User.get_reset_token(user)
        msg = Message()
        msg.subject = "Reset your password"
        msg.sender = os.getenv('MAIL_USERNAME')
        msg.recipients = [form.email.data]
        msg.html = render_template('auth/reset_email.html',
                                    User=form.email.data, 
                                    token=token)
        mail.send(msg)

        return render_template('auth/checkYourEmail.html')
    return render_template('auth/forgot_password.html', form=form, action="/resetpassword")

    
@auth_bp.route('/newpassword/<token>', methods=['GET', 'POST'])
def newPassword(token):
    form = NewPassword()
    if form.validate_on_submit():
        email = token
        new_password = form.password.data
        if User.reset_password(email, new_password):
            session['user'] = email
            flash('Your password has been updated!', 'success')
            return redirect(url_for("dashboard_bp.dashboard"))
        else:
            flash('Unable to update your password.', 'danger')
            return redirect("/")
        
    user = User.verify_reset_token(token)
    return render_template('auth/forgot_password.html', form=form, user_email=user.email, action=f'/newpassword/{user.email}')
