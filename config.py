import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    FLASK_APP="run.py"
    FLASK_ENV="development"
    ENV=FLASK_ENV
    SECRET_KEY= os.environ.get('SECRET_KEY')
    DEBUG=True
    TESTING=False

    #SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = False