from flask_test_app import create_app
from config import TestingConfig

app = create_app(config='config.TestingConfig')
print(f"--> {app.config['TESTING']}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
