from flask_test_app import db


class BaseDB(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    