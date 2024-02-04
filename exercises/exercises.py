from flask import Blueprint, render_template, redirect, url_for, jsonify, request
import requests
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
    category = request.args.get('muscles')
    if equipment != "all":
        parameters['equipment'] = equipment
    if category != "all":
        parameters['category'] = category
        
    try:
        response = requests.get(api_url + "exercisebaseinfo", params=parameters)
        if response.status_code == 200:
            data = response.json()
            # results[1].exercises[0].name
            # exercises[0].id
            # results[0].exercises[0].name
            # let's just get the first exercise for each result

            return render_template('exercises/exerices_info.html', data=data)
        else:
            return jsonify({'error': 'Failed to fetch data from the API'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@exercises_bp.route('/search')
def search_name():
    # search by name . sadly there is no name option in the exercisebaseinfo 
    parameters = {
        "language": "en",
        "term": request.args.get('terms')
        }
    try:
        response = requests.get(api_url + "search", params=parameters)
        if response.status_code == 200:
            data = response.json()
            return render_template('exercises/exerices_info_search.html', data=data)
        else:
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
