from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

from app.db.session import get_db_session
from app.helpers.http_status_code import HTTP_200_OK
from app.models.user import UserModel

auth_me_bp = Blueprint('me', __name__)

session = get_db_session()


@auth_me_bp.route('/me', methods=['GET'])
@jwt_required()
def me_view():
    """Endpoint que retorna os dados do usuário logado"""

    user_id = get_jwt_identity()

    user = session.query(UserModel).filter_by(id=user_id).first()

    return jsonify({'username': user.username, 'email': user.email}), HTTP_200_OK


@auth_me_bp.route('/me/refresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh_user_token_view():
    """Endpoint que retorna um novo token de acesso"""

    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)

    return jsonify({'access_token': access_token}), HTTP_200_OK


