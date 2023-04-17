from flask import jsonify, request
from flask_restx import Resource
from werkzeug.security import generate_password_hash

from app.db.session import get_db_session
from app.helpers.http_status_code import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_409_CONFLICT
from app.models.user import UserModel

session = get_db_session()


def register_user_controller(email, username, password):
    """Autentica o usuário e cria o usuário no banco de dados"""

    data = request.get_json()
    missing_fields = []
    example = {}

    if not data.get('email'):
        missing_fields.append('email')
        example['email'] = 'seu.email@gmail.com'
    if not data.get('username'):
        missing_fields.append('username')
        example['username'] = 'seuusername'
    if not data.get('password'):
        missing_fields.append('password')
        example['password'] = 'suasenha'
    if missing_fields:
        return jsonify({'error': f'Campos obrigatórios não informados: {", ".join(missing_fields)}',
                        'example': example}), HTTP_400_BAD_REQUEST
    if len(password) < 8:
        return jsonify({'error': 'A senha deve conter pelo menos 8 caracteres'}), HTTP_400_BAD_REQUEST

    if len(username) < 4:
        return jsonify({'error': 'O nome de usuário deve conter pelo menos 4 caracteres'}), HTTP_400_BAD_REQUEST

    if not username.isalnum() or " " in username:
        return jsonify({'error': 'O nome de usuário deve conter apenas letras e números'}), HTTP_400_BAD_REQUEST

    email_validation = session.query(UserModel).filter_by(email=email).first()
    if email_validation:
        return jsonify({'error': 'Usuário já existe'}), HTTP_409_CONFLICT

    username_validation = session.query(UserModel).filter_by(username=username).first()
    if username_validation:
        return jsonify({'error': 'Usuário já existe'}), HTTP_409_CONFLICT

    psw_hash = generate_password_hash(password)

    new_user = UserModel(email=email, username=username, password=psw_hash)
    session.add(new_user)
    session.commit()

    return jsonify({'message': 'Usuário criado com sucesso',
                    'user': {'username': username, 'email': email}}), HTTP_201_CREATED
