from flask_test_app import db
from flask_test_app.dbmodels.base_dbmodel import BaseDB

class UserDB(BaseDB):
    __tablename__ = 'users'

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    #books field from BookDB backref

    def __init__(self, name, email, password, books=None):
        self.name = name
        self.email = email
        self.password = password
        if books:
            self.books = books

    def save(self):
        db.session.add(self)
        db.session.commit()