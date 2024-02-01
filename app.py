from flask import Flask
from models import db
from auth import auth

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# with app.app_context():
#     db.create_all()  
@app.route('/')
def index():
    return "This is an example app" 

app.register_blueprint(auth.auth_blueprint)

if __name__ == "__main__":
    app.run(debug=True)