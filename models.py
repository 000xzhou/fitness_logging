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
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    @classmethod
    def authenticate(cls, username, password):
        """Validate that user exists & password is correct.
        Return user if valid; else return False.
        """
        u = User.query.filter_by(username=username).first()
        if not u:
            return None, "User does not exist" 
        if bcrypt.check_password_hash(u.password, password):
            return u, None
        else:
            return None, "Wrong password"