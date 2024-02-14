from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime, timezone
from dataclasses import dataclass

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
    
    workoutplans = db.relationship('WorkoutPlan', backref='user')
    exerciseLogs = db.relationship('ExerciseLog', backref='user')
    
@dataclass
class ExerciseLog(db.Model):
# log for exericise + date + amount   (added after finish working out 1 exerice) 
    __tablename__ = "exerciseLogs"
    #! everything will be in metric 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Text, db.ForeignKey('users.email'))
    exercise_id = db.Column(db.Integer, nullable=False)
    set_num = db.Column(db.Integer, nullable=True)
    repetitions = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    cardio = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    date_logged = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    exercise_name = db.Column(db.Text, nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('exerciseinplans.id'))
    plan_id = db.Column(db.Integer, db.ForeignKey('workoutplans.id'))
    
    
        
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
    
# class Workoutsession(db.Model):
#     __tablename__ = "workoutsessions"
    
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     plan_id = db.Column(db.Integer, db.ForeignKey('workoutplans.id'))
#     date = db.Column(db.DateTime, nullable=False)