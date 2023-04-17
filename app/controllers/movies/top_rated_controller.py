import requests
from flask import jsonify

from app.helpers.http_status_code import HTTP_200_OK
from config import Config


def get_top_rated_movies_controller():
    """Função responsável por pegar os filmes mais bem avaliados"""

    top_rated_movies = []

    top_rated_url = f"{Config.URL}/movie/top_rated?api_key={Config.API_KEY}&language=pt-BR&page=1"
    top_movies = requests.get(top_rated_url).json()

    for movie in top_movies['results']:
        top_movies_data = {
            'id': movie['id'],
            'title': movie['title'],
            'popularity': movie['popularity'],
            'overview': movie['overview'],
            'poster_path': movie['poster_path'],
            'release_date': movie['release_date'],
            'vote_average': movie['vote_average'],
            'vote_count': movie['vote_count'],
        }
        top_rated_movies.append(top_movies_data)

    return jsonify({'Top Rated Movies': top_rated_movies}), HTTP_200_OK
