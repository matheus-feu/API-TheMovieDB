from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from app.helpers.http_status_code import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST
from config import Config


def create_app():
    """Create a Flask application using the app factory pattern."""
    app = Flask(__name__)

    """Load configuration"""
    app.config.from_object(Config)

    """JWT configuration"""
    JWTManager(app)

    """Register blueprints"""
    from app.views.auth.me_view import auth_me_bp
    app.register_blueprint(auth_me_bp, url_prefix='/api/v1/user', tags=['auth'])

    from app.views.auth.login_view import login_bp
    app.register_blueprint(login_bp, url_prefix='/api/v1/user', tags=['auth'])

    from app.views.auth.signup_view import register_bp
    app.register_blueprint(register_bp, url_prefix='/api/v1/user', tags=['auth'])

    from app.views.movies.trending_view import trending_bp
    app.register_blueprint(trending_bp, url_prefix='/api/v1/movies', tags=['movies'])

    from app.views.movies.populars_view import populars_bp
    app.register_blueprint(populars_bp, url_prefix='/api/v1/movies', tags=['movies'])

    from app.views.movies.top_rated_view import top_rate_bp
    app.register_blueprint(top_rate_bp, url_prefix='/api/v1/movies', tags=['movies'])

    from app.views.movies.upcoming_view import upcoming_bp
    app.register_blueprint(upcoming_bp, url_prefix='/api/v1/movies', tags=['movies'])

    @app.errorhandler(HTTP_404_NOT_FOUND)
    def error_not_found(error):
        """Verifica se as rotas """
        return jsonify({'error': 'Not found'}), HTTP_404_NOT_FOUND

    @app.errorhandler(HTTP_400_BAD_REQUEST)
    def error_bad_request(error):
        return jsonify({
            'error': 'Bad Request'}), HTTP_400_BAD_REQUEST

    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def error_internal_server(error):
        return jsonify({'error': 'Internal Server Error'}), HTTP_500_INTERNAL_SERVER_ERROR

    return app
