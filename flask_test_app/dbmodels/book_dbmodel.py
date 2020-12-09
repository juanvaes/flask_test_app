from flask_test_app.dbmodels.base_dbmodel import BaseDB, db

class BookDB(BaseDB):
    __tablename__ = 'books'

    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)

    library_id = db.Column(db.Integer, db.ForeignKey('libraries.id'))
    library = db.relationship('LibraryDB')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserDB', backref=db.backref('books'))

    def __init__(self, title, author, library_id=None):
        self.title = title
        self.author = author
        self.library_id = library_id

    def json(self):
        return {'title': self.title, 'author': self.author}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()