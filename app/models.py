from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class User(db.Model):
    __tablename__ = "users"

    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)