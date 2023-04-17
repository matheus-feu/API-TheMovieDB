from flask import jsonify, request
from flask_jwt_extended import create_refresh_token, create_access_token
from werkzeug.security import check_password_hash

from app.db.session import get_db_session
from app.helpers.http_status_code import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from app.models.user import UserModel

session = get_db_session()


def login_user_controller(email, password):
    """Função que faz a autenticação do usuário"""

    data = request.get_json()
    missing_fields = []
    example = {}

    if not data.get('email'):
        missing_fields.append('email')
        example['email'] = 'seu.email@gmail.com'
    if not data.get('password'):
        missing_fields.append('password')
        example['password'] = 'suasenha'
    if missing_fields:
        return jsonify({'error': f'Campos obrigatórios não informados: {", ".join(missing_fields)}',
                        'example': example}), HTTP_400_BAD_REQUEST

    user = session.query(UserModel).filter_by(email=email).first()

    if user:
        is_password_correct = check_password_hash(user.password, password)

        if is_password_correct:
            response_data = {
                'username': user.username,
                'email': user.email,
                'refresh': create_refresh_token(identity=user.id),
                'access': create_access_token(identity=user.id)
            }

            return jsonify(response_data), HTTP_200_OK

    return jsonify({'error': 'Incorrect authentication credentials'}), HTTP_401_UNAUTHORIZED
