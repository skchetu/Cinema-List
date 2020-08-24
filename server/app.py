import os
import uuid
import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# get the folder where this file runs
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DATABASE = 'filminfo.db'
DEBUG = True
SECRET_KEY = 'bsaucehere'
USERNAME = 'bsauce'
PASSWORD = 'bottomtext'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

import models

def remove_movie(id):
    print(id)
    try:
        db.session.query(models.FilmInfo).filter_by(film_id=id).delete()
        db.session.commit()
        return True
    except Exception as e:
        err = repr(e)
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
        new_entry = models.FilmInfo(
            post_data.get('week'),
            post_data.get('title'),
            post_data.get('director'),
            post_data.get('shanRating'),
            post_data.get('cheRating'),
            post_data.get('andhiRating'),
            post_data.get('avgRating')
        )
        db.session.add(new_entry)
        db.session.commit()
        response_object['message'] = 'Movie added!'
    else:
        movies = []
        films = db.session.query(models.FilmInfo)
        for f in films:
            fd = f.__dict__
            del fd['_sa_instance_state']
            movies.append(fd)
            
        response_object['movies'] = movies
    return jsonify(response_object)


@app.route('/movies/<movie_id>', methods=['PUT', 'DELETE'])
def single_movie(movie_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_movie(movie_id)
        new_entry = models.FilmInfo(
            post_data.get('week'),
            post_data.get('title'),
            post_data.get('director'),
            post_data.get('shanRating'),
            post_data.get('cheRating'),
            post_data.get('andhiRating'),
            post_data.get('avgRating')
        )
        db.session.add(new_entry)
        db.session.commit()
        response_object['message'] = 'Movie updated!'
    if request.method == 'DELETE':
        remove_movie(movie_id)
        response_object['message'] = 'Movie removed!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()