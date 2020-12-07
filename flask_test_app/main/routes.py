from flask import jsonify
from flask_test_app.main.main import main_bp

@main_bp.route('/')
def index():
    return jsonify({'hello': 'from blueprint'})