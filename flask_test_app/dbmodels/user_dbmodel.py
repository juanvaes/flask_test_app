from flask_test_app import db
from flask_test_app.dbmodels.base_dbmodel import BaseDB

class UserDB(BaseDB):
    __tablename__ = 'users'

    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name
        self.books = []

    def save(self):
        db.session.add(self)
        db.session.commit()