from flask import Blueprint, render_template, redirect, url_for, jsonify, request
import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ['NINJA_API_KEY']

exercises_bp = Blueprint('exercises_bp', __name__,
    template_folder='templates', static_folder='static')

@exercises_bp.route('/search')
def search_overall():
# filter exerices if no filter(/all) display all exercises
    api_url = 'https://api.api-ninjas.com/v1/exercises'
    parameters = {
        "X-Api-Key" : api_key,
        }
    optional_params = {
        "name" : request.args.get('name', default='', type=str),
        "type" : request.args.get('type', default='', type=str),
        "muscle" : request.args.get('muscle', default='', type=str),
        "difficulty" : request.args.get('difficulty', default='', type=str)
    }
    # filter params 
    parameters.update({key: value for key, value in optional_params.items() if value})
        
    try:
        response = requests.get(api_url, params=parameters)
        if response.status_code == 200:
            data = response.json()
            # return jsonify(data)
            return render_template('exercises/exercises.html', data=data)
        else:
            return jsonify({'error': 'Failed to fetch data from the API'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    











# Below is me trying this api but I can't find the muscle endpoint to filter by muscle. It was hard to find anything. So i switch 

# @exercises_bp.route('/exercisecategory')
# def exercisecategory():
#     api_url = 'https://wger.de/api/v2/exercisecategory/'
#     try:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             data = response.json()
#             results = data.get('results', [])
#             # print(results)
#             # session["category"] = results
#             return jsonify(data)
#         else:
#             return jsonify({'error': 'Failed to fetch data from the API'}), response.status_code
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
# @exercises_bp.route('/equipment')
# def equipment():
#     api_url = 'https://wger.de/api/v2/equipment/'
#     try:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             data = response.json()
#             results = data.get('results', [])
#             # print(results)
#             # session["equipment"] = results
#             return jsonify(data)
#         else:
#             return jsonify({'error': 'Failed to fetch data from the API'}), response.status_code
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
 