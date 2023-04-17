from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.movies.top_rated_controller import get_top_rated_movies_controller

top_rate_bp = Blueprint('toprated', __name__)


@top_rate_bp.route('/top-rated', methods=['GET'])
@jwt_required()
def get_top_rated_movies_view():
    """Endpoint - GET, pegar os filmes mais bem avaliados"""
    return get_top_rated_movies_controller()
