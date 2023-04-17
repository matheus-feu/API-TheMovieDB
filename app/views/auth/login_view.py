from flask import Blueprint, request

from app.controllers.auth.login_controller import login_user_controller

login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/login', methods=['POST'])
def login_user_view():
    """Endpoint que faz a autenticação do usuário"""
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    return login_user_controller(email, password)
