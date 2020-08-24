import uuid
import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS

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
    }
]

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

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


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

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

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()