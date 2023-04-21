from flask import Blueprint, request

from app.controllers.movies.recommendations_controller import get_recommendations_controller

recommendations_bp = Blueprint('recommendations', __name__)


@recommendations_bp.route('/recommendations', methods=['GET'])
def get_recommendations_view():
    """Endpoint que irá pegar a lista de filmes recomendados"""

    movie_id = request.args.get('movie_id')

    return get_recommendations_controller(movie_id)
