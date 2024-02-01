from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from auth import auth

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# from models import Result

@app.route('/')
def index():
    return "This is an example app" 

app.register_blueprint(auth.auth_blueprint)

if __name__ == "__main__":
    app.run(debug=True)