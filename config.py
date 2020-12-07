class BaseConfig:
    FLASK_APP="run.py"
    FLASK_ENV="development"
    ENV=FLASK_ENV
    SECRET_KEY="AcUvfymBT0snYw"
    DEBUG=True
    TESTING=False

class TestingConfig(BaseConfig):
    TESTING = True