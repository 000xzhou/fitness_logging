from flask import Blueprint, render_template, redirect, url_for, jsonify, request
import requests
from models import ExerciseInPlan, db
import os
from dotenv import load_dotenv
load_dotenv()

exercises_bp = Blueprint('exercises_bp', __name__,
    template_folder='templates', static_folder='static', static_url_path='/exerc')

api_url = os.environ['WGER_BASE_URL']
@exercises_bp.route('/')
def main_page():
    return render_template('exercises.html')

@exercises_bp.route('/filter')
def filter_overall():
# search by filters
    parameters = {
        "limit": 5,
        "offset": 0
        }
    
    equipment = request.args.get('equipment')
    category = request.args.get('muscle')
    if equipment != "all":
        parameters['equipment'] = equipment
    if category != "all":
        parameters['category'] = category
        
    try:
        response = requests.get(api_url + "exercisebaseinfo/", params=parameters)
        if response.status_code == 200:
            data = response.json()
            return render_template('exercises/exerices_info.html', data=data)
        else:
            # return jsonify({'error': 'Failed to fetch data from the API'}), response.status_code
            return render_template('not_found.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@exercises_bp.route('/search')
def search_name():
    # search by name . sadly there is no name option in the exercisebaseinfo 
    parameters = {
        "language": "en",
        "term": request.args.get('term')
        }
    try:
        response = requests.get(api_url + "exercise/search/", params=parameters)
        if response.status_code == 200:
            data = response.json()
            return render_template('exercises/exerices_info_search.html', data=data['suggestions'])
        else:
            # note to self: change below since it can't be both text and json 
            return jsonify({'error': 'Failed to fetch data from the API'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@exercises_bp.route('/muscles')
def muscle_list():
    try:
        response = requests.get(api_url + 'exercisecategory')
        if response.status_code == 200:
            data = response.json()
            return render_template('exercises/muscles.html', data = data['results'])
        else:
            return jsonify({'error': 'Failed to fetch data from the API'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@exercises_bp.route('/equipment')
def equipment_list():
    try:
        response = requests.get(api_url + 'equipment')
        if response.status_code == 200:
            data = response.json()
            return render_template('exercises/equipment.html', data = data['results'])
        else:
            return jsonify({'error': 'Failed to fetch data from the API'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# =========================== START add edit delete exercise START ============================================

@exercises_bp.route('/add_exercise', methods=['POST'])
def add_exercise():
    # adding default value to the exerices they added in 
    
    new_exercise = ExerciseInPlan(plan_id=request.json['plan_id'], 
                                  exercise_id=request.json['exercise_id'], 
                                  exercise_name=request.json['exercise_name'],
                                  sets = request.json.get('sets'),
                                  cardio = request.json.get('cardio'),
                                  repetitions = request.json.get('rep'),
                                  weight = request.json.get('weight')
                                  )
    db.session.add(new_exercise)
    db.session.commit()

    return render_template('exercises/add_exercise.html', exercise = new_exercise)

@exercises_bp.route('/delete_exercise', methods=['DELETE'])
def delete_exercise():
    id = request.json['id']
    exercise = ExerciseInPlan.query.get_or_404(id)
    db.session.delete(exercise)
    db.session.commit()
    return jsonify({'message': 'Schedule deleted successfully'})