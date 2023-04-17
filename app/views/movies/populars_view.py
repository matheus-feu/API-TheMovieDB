from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.movies.populars_controller import get_movies_populars_controller

populars_bp = Blueprint('populars', __name__)


@populars_bp.route('/populars', methods=['GET'])
@jwt_required()
def get_movies_populars_view():
    """Endpoint GET, responsável por abstrair todos os filmes populares"""

    return get_movies_populars_controller()
