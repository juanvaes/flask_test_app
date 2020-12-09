from flask_test_app import db
from flask_test_app.dbmodels.base_dbmodel import BaseDB

class UserDB(BaseDB):
    __tablename__ = 'users'

    name = db.Column(db.String(100), nullable=False)

    #books field from BookDB backref

    def __init__(self, name, books=None):
        self.name = name
        if books:
            self.books = books

    def save(self):
        db.session.add(self)
        db.session.commit()