from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime, timezone

bcrypt = Bcrypt()
db = SQLAlchemy()
    
class User(db.Model):
    __tablename__ = "users"

    email = db.Column(db.Text, unique=True, primary_key=True)
    password = db.Column(db.Text, nullable=False)
    reminders = db.Column(db.Boolean, default=False)
    # weightunit = db.Column(db.Text, default='metric')
    
    def __init__(self, email, password):
        # , reminders, weightunit
        self.email = email
        self.password = password
        # self.reminders = reminders
        # self.weightunit = weightunit
    
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
    
    
class ExerciseLog(db.Model):
# log for exericise + date + amount   (added after finish working out 1 exerice) 
    __tablename__ = "exerciseLogs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Text, db.ForeignKey('users.email'))
    exercise_id = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=True)
    repetitions = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    cardio = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    date_logged = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    weightunit = db.Column(db.Text, default='metric')
    
    def __init__(self, id, user_id, exercise_id):
        # , sets, repetitions, weight, cardio, notes, date_logged, weightunit
        self.id = id
        self.user_id = user_id
        self.exercise_id = exercise_id
        # self.sets = sets
        # self.repetitions = repetitions
        # self.weight = weight
        # self.cardio = cardio
        # self.notes = notes
        # self.date_logged = date_logged
        # weightunit = weightunit
        
        
class WorkoutPlan(db.Model):
# name of folder for the exerice 
    __tablename__ = "workoutplans"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Text, db.ForeignKey('users.email'))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_weekly = db.Column(db.Text, default=False)
    mon = db.Column(db.Text, default=False)
    tue = db.Column(db.Text, default=False)
    wed = db.Column(db.Text, default=False)
    thur = db.Column(db.Text, default=False)
    fri = db.Column(db.Text, default=False)
    sat = db.Column(db.Text, default=False)
    sun = db.Column(db.Text, default=False)
    
    def __init__(self, name, description, user_id, is_weekly, mon, tue,wed, thur, fri,sat,sun):
        # id, created_at
        # self.id = id
        self.name = name
        self.description = description
        self.user_id = user_id
        # self.created_at = created_at
        self.is_weekly = is_weekly
        self.mon = mon
        self.tue = tue
        self.wed = wed
        self.thur = thur
        self.fri = fri
        self.sat = sat
        self.sun = sun
    
    exerciseinplans = db.relationship('ExerciseInPlan', backref='workoutplan')
        

class ExerciseInPlan(db.Model):
# exericed details in the workoutplan
    __tablename__ = "exerciseinplans"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('workoutplans.id'))
    exercise_id = db.Column(db.Integer, nullable=False)
    exercise_name = db.Column(db.Text, nullable=False)

    def __init__(self, plan_id, exercise_id, exercise_name):
        # self.id = id
        self.plan_id = plan_id
        self.exercise_id = exercise_id
        self.exercise_name = exercise_name
        
        
class Workoutsession(db.Model):
    # might not use. I will come back to this after getting everything else
    __tablename__ = "workoutsessions"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)