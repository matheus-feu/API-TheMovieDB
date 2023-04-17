import requests
from flask import jsonify

from app.helpers.http_status_code import HTTP_200_OK
from config import Config


def get_movies_populars_controller():
    """Função que irá realizar a consulta de todos os filmes populares"""

    movies = []

    popular_url = f"{Config.URL}movie/popular?api_key={Config.API_KEY}&language=pt-BR&page=2"
    movies_data = requests.get(popular_url).json()

    for movie in movies_data['results']:
        movie_data = {
            'id': movie['id'],
            'title': movie['title'],
            'overview': movie['overview'],
            'popularity': movie['popularity'],
            'release_date': movie['release_date'],
            'vote_average': movie['vote_average'],
            'vote_count': movie['vote_count'],
        }

        movies.append(movie_data)

    return jsonify({'Popular Movies': movies}), HTTP_200_OK
