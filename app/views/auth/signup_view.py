from flask import Blueprint, request

from app.controllers.auth.signup_controller import register_user_controller

register_bp = Blueprint('register', __name__)


@register_bp.route('/register', methods=['POST'])
def register_user_view():
    """Endpoint para registrar um usuário"""

    email = request.json.get('email')
    username = request.json.get('username')
    password = request.json.get('password')

    return register_user_controller(email, username, password)
