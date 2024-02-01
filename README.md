# fitness_logging

slogan - we will remember so you don't have to

using as reference:
https://realpython.com/flask-blueprint/
https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

## Prograss

1. User Authentication:
   - [x] User registration and login. <sub>Note: should I add google login?</sub>
   - [ ] Password recovery/reset functionality.
2. Dashboard:
   - [ ] Personalized dashboard for each user.
   - [ ] Overview of recent workouts and achievements.
   - [ ] Progress tracking charts or graphs.
3. Exercise Library:
   - [ ] Browse and search functionality for a comprehensive exercise database.
   - [ ] Filter exercises by muscle group, equipment, or difficulty level.
   - [ ] Detailed exercise descriptions, including proper form and tips. <sub>I will use w.e there is </sub>
4. Workout Logging:
   - [ ] Log individual exercises with sets, repetitions, and weights.
   - [ ] Log duration and intensity for cardio workouts.
   - [ ] Option to add notes or comments for each exercise.
   - [ ] Timer during workout
5. Custom Workouts:
   - [ ] Create and save custom workout plans.
   - [ ] Select exercises from the library to include in custom workouts.
   - [ ] Specify sets, repetitions, and rest intervals.
6. Routine Tracking:
   - [ ] Track recurring workout routines. <sub>Not sure what this means</sub>
   - [ ] Set reminders for upcoming workouts.
   - [ ] View a calendar with scheduled workouts.
7. Social Features:
   - [ ] Share completed workouts or achievements.
8. Workout History:
   - [ ] Access a complete history of logged workouts.

## add-ons for flask that I might or might not use

### WTForms-Alchemy

- from wtforms_alchemy import ModelForm
- from models import Pet

### Flask-Login

- from flask_login import login_user, logout_user, login_required

### Flask-Mail

- from flask_mail import Message
- send reminder email or password reset

### Flask-Restless

- makes restless routes base on your model
