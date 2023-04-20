from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers.movies.upcoming_controller import get_upcoming_movie_controller

upcoming_bp = Blueprint('upcoming', __name__)


@upcoming_bp.route('/upcoming', methods=['GET'])
@jwt_required()
def get_upcoming_movie_view():
    """Endpoint que irá pegar a lista de filmes em cartaz"""

    region = request.args.get('region')

    return get_upcoming_movie_controller(region)
