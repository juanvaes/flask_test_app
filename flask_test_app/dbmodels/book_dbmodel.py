from flask_test_app import db
from flask_test_app.dbmodels.base_dbmodel import BaseDB

class BookDB(BaseDB):
    __tablename__ = 'books'

    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)

    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'))
    library = db.relationship('LibraryDB')

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def json(self):
        return {'title': self.title, 'author': self.author}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()