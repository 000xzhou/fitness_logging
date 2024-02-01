from flask import Blueprint

auth_blueprint = Blueprint('auth_blueprint', __name__,
    template_folder='templates',)
# app.register_blueprint(auth_blueprint)

@auth_blueprint.route('/auth')
def auth():
    return "This is an auth route"