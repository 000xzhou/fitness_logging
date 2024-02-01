from flask import Blueprint, render_template, session, redirect, url_for

general_bp = Blueprint('general_bp', __name__,
    template_folder='templates',)