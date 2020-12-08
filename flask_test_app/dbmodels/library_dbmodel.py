from flask_test_app import db
from flask_test_app.dbmodels.base_dbmodel import BaseDB

class LibraryDB(BaseDB):
    __tablename__ = 'libraries'

    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('BookDB', lazy='dynamic')

    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {
            'name': self.name,
            'books': [item.json() for item in self.books.all()]
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()