from app import app
from flask import render_template, redirect, request, url_for, flash, session    

@app.route('/')
@app.route('/index')
def index():
    return 'Welcome to Nothingness'

@app.route('/login')
def login():
    return render_template("auth/login.html")

@app.route('/register')
def register():
    return render_template("auth/register.html")