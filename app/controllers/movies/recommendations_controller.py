import requests
from flask import jsonify

from app.helpers.http_status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST
from config import Config


def get_recommendations_controller(movie_id):
    """Controller que irá pegar a lista de filmes recomendados"""

    recommendations = []

    if not movie_id:
        return jsonify({'error': 'Missing parameters'}), HTTP_400_BAD_REQUEST

    url_recommendations = f"{Config.URL}movie/{movie_id}/recommendations?api_key={Config.API_KEY}&language=en-US&page=1"
    recommendations_data = requests.get(url_recommendations).json()

    for movie in recommendations_data['results']:
        recommendations_data = {
            'title': movie['title'],
            'release_date': movie['release_date'],
            'popularity': movie['popularity'],
        }
        recommendations.append(recommendations_data)

    if not recommendations:
        return jsonify({'error': 'No recommendations found'}), HTTP_400_BAD_REQUEST

    return jsonify({'results': recommendations}), HTTP_200_OK
