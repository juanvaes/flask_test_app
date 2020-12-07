from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    with app.app_context():
        db.init_app(app)

        from .main import main
        app.register_blueprint(main.main_bp)
    
    return app
