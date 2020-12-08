from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config='config.BaseConfig'):
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    with app.app_context():
        # Registerinb blueprints
        from .main import main
        app.register_blueprint(main.main_bp)

        # Initialize db and create table
        db.create_all()
    
    return app
