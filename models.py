from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime, timezone
from dataclasses import dataclass
import jwt
from time import time
import os

bcrypt = Bcrypt()
db = SQLAlchemy()

@dataclass
class User(db.Model):
    __tablename__ = "users"

    email = db.Column(db.Text, unique=True, primary_key=True)
    password = db.Column(db.Text, nullable=False)
    reminders = db.Column(db.Boolean, default=False)
    weightunit = db.Column(db.Text, default='metric')
    
    @classmethod
    def is_authenticated(cls, email, password):
        """Validate that user exists & password is correct.
        Return user if valid; else return False.
        """
        u = User.query.filter_by(email=email).first()
        if not u:
            return "User does not exist" 
        if bcrypt.check_password_hash(u.password, password):
            return u
        else:
            return "Wrong password"
        
    @classmethod
    def register(cls, email, password):
        """Register user w/hashed password & return user."""
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        return cls(email=email, password=hashed_utf8)
    
    def get_reset_token(self, expires=500):
        return jwt.encode({'reset_password': self.email,
                           'exp':    time() + expires},
                           key=os.getenv('SECRET_KEY'))
    def verify_reset_token(token):
        try:
            email = jwt.decode(token,
                        key=os.getenv('SECRET_KEY'),
                       algorithms=["HS256"])['reset_password']
        except Exception as e:
            print(e)
            return
        return User.query.filter_by(email=email).first()
    
    @classmethod
    def reset_password(cls, user_id, new_password):
        user = cls.query.get(user_id) 
        if user:
            hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8') 
            user.password = hashed_password 
            db.session.commit() 
            return True
        return False
    
    workoutplans = db.relationship('WorkoutPlan', backref='user')
    workoutsessions = db.relationship('Workoutsession', backref='user')
    
@dataclass
class WorkoutPlan(db.Model):
# name of folder for the exerice 
    __tablename__ = "workoutplans"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Text, db.ForeignKey('users.email'))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    repeat = db.Column(db.Text, default=None)
    # is_weekly = db.Column(db.Boolean, default=False)
    mon = db.Column(db.Boolean, default=False)
    tue = db.Column(db.Boolean, default=False)
    wed = db.Column(db.Boolean, default=False)
    thur = db.Column(db.Boolean, default=False)
    fri = db.Column(db.Boolean, default=False)
    sat = db.Column(db.Boolean, default=False)
    sun = db.Column(db.Boolean, default=False)
    date = db.Column(db.Date, nullable=True)
    exerciseinplans = db.relationship('ExerciseInPlan', backref='workoutplan')
    
        
@dataclass
class ExerciseInPlan(db.Model):
# exericed details in the workoutplan
    __tablename__ = "exerciseinplans"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('workoutplans.id'))
    exercise_id = db.Column(db.Integer, nullable=False)
    exercise_name = db.Column(db.Text, nullable=False)
    sets = db.Column(db.Integer, nullable=True)
    repetitions = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    cardio = db.Column(db.Integer, nullable=True)
    
    
    
@dataclass
class Workoutsession(db.Model):
    __tablename__ = "workoutsessions"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # plan_id = db.Column(db.Integer, db.ForeignKey('workoutplans.id'), nullable=True)
    user_id = db.Column(db.Text, db.ForeignKey('users.email'))
    date_logged = db.Column(db.DateTime, nullable=False)
    # duration in sec 
    duration = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    # exercise_name = db.Column(db.Text, nullable=False)
    # exercise_id = db.Column(db.Integer, nullable=False)
    # workout_id = db.Column(db.Integer, db.ForeignKey('workoutsessions.id'))
    # log_id = db.Column(db.Integer, db.ForeignKey('exerciselogs.id'))
    
    name = db.relationship('ExerciseName', backref='exercisenames')
    
@dataclass
class ExerciseName(db.Model):
    __tablename__ = "exercisenames"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exercise_name = db.Column(db.Text, nullable=False)
    exercise_id = db.Column(db.Integer, nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workoutsessions.id'))
#     log_id = db.Column(db.Integer, db.ForeignKey('exerciselogs.id'))
    log = db.relationship('ExerciseLog', backref='exerciselogs')
    name = db.relationship('Workoutsession', backref='workoutsessions')
    

@dataclass
class ExerciseLog(db.Model):
# log for exericise + date + amount   (added after finish working out 1 exerice) 
    __tablename__ = "exerciselogs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    set_num = db.Column(db.Integer, nullable=True)
    repetitions = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    cardio = db.Column(db.Integer, nullable=True)
    cardio_time = db.Column(db.Integer, nullable=True)
    # exercise_id = db.Column(db.Integer, nullable=False)
    # workout_id = db.Column(db.Integer, db.ForeignKey('workoutsessions.id'))
    exercise_name_id = db.Column(db.Integer, db.ForeignKey('exercisenames.id'))
    
    # date_logged = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    # exercise_name = db.Column(db.Text, nullable=False)
    # workout_id = db.Column(db.Integer, db.ForeignKey('exerciseinplans.id'))
    # plan_id = db.Column(db.Integer, db.ForeignKey('workoutplans.id'))
    
    # names = db.relationship('ExerciseName', backref='exerciselog')
    
    
