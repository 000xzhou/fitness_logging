# fitness_logging

## Table of Content

- [Prograss](#Prograss)
- [Thoughts](#Thoughts)
- [using as reference](#using-as-reference)

## Prograss

1. User Authentication:
   - [x] User registration and login. <sub>Note: should I add google login?</sub>
   - [ ] Password recovery/reset functionality.
2. Dashboard:
   - [ ] Personalized dashboard for each user.
   - [ ] Overview of recent workouts and achievements.
   - [ ] Progress tracking charts or graphs.
3. Exercise Library:
   - [x] Browse and search functionality for a comprehensive exercise database. (only on schedule page atm)
   - [x] Filter exercises by muscle group, equipment, or difficulty level.
   - [x] Detailed exercise descriptions, including proper form and tips. <sub>I will use w.e there is </sub>
4. Workout Logging:
   - [ ] Log individual exercises with sets, repetitions, and weights.
   - [ ] Log duration and intensity for cardio workouts.
   - [ ] Option to add notes or comments for each exercise.
   - [ ] Timer during workout
5. Custom Workouts:
   - [x] Create and save custom workout plans.
   - [x] Select exercises from the library to include in custom workouts.
   - [ ] Specify sets, repetitions, and rest intervals.
6. Routine Tracking:
   - [ ] Track recurring workout routines. <sub>Not sure what this means</sub>
   - [ ] Set reminders for upcoming workouts.
   - [ ] View a calendar with scheduled workouts.
7. Social Features:
   - [ ] Share completed workouts or achievements.
8. Workout History:
   - [ ] Access a complete history of logged workouts.

## Thoughts

dashboard - I really don't want to use js so I try to use flask only. Then I though, why not just return the HTML block I wanted with the classes and everything already included. Then I can just use the div_id.textcontent = the return html I got from the server. Without having to create a bunch of elements and stuff.

db - made everything in db metric. and convert it depending on what unit they on

db - i regret not just downloading [this](https://github.com/yuhonas/free-exercise-db) and make my own db because it's so much better. Also because this api is sloooooooooooooow. Too slow for my taste. I need to remind myself to add a loading thingy after i'm done with 1-5.

custom workouts - I'm debating if I should do the convert before sending to server or do the convert in the server. Now that I think about it. Shouldn't make much of a difference since I'm doing this solo. Also internet says python is slow. So going to leave it in js.

exercise libaray - just notice I forgot to either add page number to get next set of exercises or the keep scrolling and load the next set.

## using as reference:

[Blueprint](https://realpython.com/flask-blueprint/)
[setting up postgres with config](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
