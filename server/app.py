import uuid
import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
#andhitest
MOVIES = [
    {
        'id': uuid.uuid4().hex,
        'week': '',
        'title': 'Burning',
        'director': 'Jack Harlow',
        'shanRating': '5',
        'cheRating': '4',
        'andhiRating': '6',
        'avgRating': '4'
    },
    {
        'id': uuid.uuid4().hex,
        'week': '',
        'title': 'Pav Bhaji',
        'director': 'Christopher Nolan',
        'shanRating': '5',
        'cheRating': '4',
        'andhiRating': '6',
        'avgRating': '4'
    }
]

# configuration
# DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def remove_movie(movie_id):
    for movie in MOVIES:
        if movie['id'] == movie_id:
            MOVIES.remove(movie)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/movies', methods=['GET', 'POST'])
def all_movies():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        MOVIES.append({
            'id': uuid.uuid4().hex,
            'week': post_data.get('week'),
            'title': post_data.get('title'),
            'director': post_data.get('director'),
            'shanRating': post_data.get('shanRating'),
            'cheRating': post_data.get('cheRating'),
            'andhiRating': post_data.get('andhiRating'),
            'avgRating': post_data.get('avgRating')
        })
        response_object['message'] = 'Movie added!'
    else:
        response_object['movies'] = MOVIES
    return jsonify(response_object)


@app.route('/movies/<movie_id>', methods=['PUT', 'DELETE'])
def single_movie(movie_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_movie(movie_id)
        MOVIES.append({
            'id': uuid.uuid4().hex,
            'week': post_data.get('week'),
            'title': post_data.get('title'),
            'director': post_data.get('director'),
            'shanRating': post_data.get('shanRating'),
            'cheRating': post_data.get('cheRating'),
            'andhiRating': post_data.get('andhiRating'),
            'avgRating': post_data.get('avgRating')
        })
        response_object['message'] = 'Movie updated!'
    if request.method == 'DELETE':
        remove_movie(movie_id)
        response_object['message'] = 'Movie removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()