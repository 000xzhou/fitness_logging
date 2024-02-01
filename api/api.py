from flask import Blueprint, render_template, session, redirect, url_for

api_bp = Blueprint('api_bp', __name__,
    template_folder='templates',)