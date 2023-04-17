import requests
from flask import jsonify

from app.helpers.http_status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST
from config import Config


def trending_movies_controller(media_type, time_window):
    """Função que irá realizar a requisição para a API do The Movie Database"""

    valid_types = ['all', 'movie', 'tv', 'person']
    if media_type not in valid_types:
        return jsonify({'error': 'Invalid media'}), HTTP_400_BAD_REQUEST

    valid_time_windows = ['day', 'week']
    if time_window not in valid_time_windows:
        return jsonify({'error': 'Invalid time window'}), HTTP_400_BAD_REQUEST

    try:
        url = f"{Config.URL}trending/{media_type}/{time_window}?api_key={Config.API_KEY}&language=pt-BR"
        trending = requests.get(url).json()
        return jsonify(trending), HTTP_200_OK
    except Exception as error:
        return jsonify({'error': f'Error when searching for trends: {error}'}), HTTP_400_BAD_REQUEST
