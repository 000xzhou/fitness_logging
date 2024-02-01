from flask import Blueprint, render_template, session, redirect, url_for

exercises_bp = Blueprint('exercises_bp', __name__,
    template_folder='templates',)