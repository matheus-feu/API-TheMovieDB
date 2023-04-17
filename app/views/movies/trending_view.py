from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers.movies.trending_controller import trending_movies_controller

trending_bp = Blueprint('auth', __name__)


@trending_bp.route('/trending', methods=['POST'])
@jwt_required()
def trending_movies_view():
    """
    View para pegar as tendências no parâmetro da requisição, filmes do dia e da semana, escolhendo
    o tipo de mídia entre 'all', 'movie', 'tv' e 'person' e escolhe a janela do tempo entre 'day' e 'week'
    """

    request_data = request.get_json()
    media_type = request_data['media_type'].lower()
    time_window = request_data['time_window'].lower()

    return trending_movies_controller(media_type, time_window)
