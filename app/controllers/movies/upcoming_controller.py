import re

import requests
from flask import jsonify

from app import HTTP_400_BAD_REQUEST
from app.helpers.http_status_code import HTTP_200_OK
from config import Config


def get_upcoming_movie_controller(region):
    """Controller que irá pegar a lista de filmes em cartaz"""

    upcoming_movies = []

    if not region:
        return jsonify({'error': 'Missing parameters'}), HTTP_400_BAD_REQUEST

    if not re.match(r'^[A-Z]{2}$', region):
        return jsonify({'error': 'Invalid region format'}), HTTP_400_BAD_REQUEST

    url_upcoming = f"{Config.URL}movie/upcoming?api_key={Config.API_KEY}&language=pt-BR&region={region}"
    upcoming_data = requests.get(url_upcoming).json()

    for movie in upcoming_data['results']:
        upcoming_data = {
            'title': movie['title'],
            'release_date': movie['release_date'],
            'popularity': movie['popularity'],
        }
        upcoming_movies.append(upcoming_data)

    return jsonify({'Upcoming Movies': upcoming_movies}), HTTP_200_OK
