from flask import jsonify, request

from flask_test_app import db
from flask_test_app.main.main import main_bp
from flask_test_app.dbmodels import BookDB, LibraryDB, UserDB


@main_bp.route('/register', methods=['POST'])
def register_user():
    data = request.form
    user = UserDB(name=data['name'], email=data['email'], password=data['password'])
    user.save()
    return jsonify({'user_id': user.id})


@main_bp.route('/login', methods=['POST'])
def login_user():
    data = request.form
    user = UserDB.query.filter_by(email=data['email']).first()
    if not user:
        return jsonify({'token': 'User not found'})
    return jsonify({'token': 'User logged in'})


@main_bp.route('/books', methods=['GET'])
def get_books():
    books = BookDB.query.all()
    return jsonify({'books': [b.json() for b in books]})

@main_bp.route('/books', methods=['POST'])
def create_books():
    data = request.form
    lib_id = data.get('library_id', None)
    title = data.get('title', None)
    author = data.get('author', None)
    if lib_id:
        lib_id = int(lib_id)
    b = BookDB(title=title, author=author, library_id=lib_id)
    db.session.add(b)
    db.session.commit()
    return jsonify({'book_id': b.id})

@main_bp.route('/books/<int:book_id>', methods=['GET', 'PUT'])
def get_item_book(book_id):
    book = BookDB.query.filter_by(id=book_id).first()
    return jsonify({'book': book.json() if book else None })

@main_bp.route('/libraries', methods=['GET'])
def get_libraries():
    libraries = LibraryDB.query.all()
    return jsonify({'libraries': [l.json() for l in libraries]})

@main_bp.route('/libraries', methods=['POST'])
def create_library():
    data = request.form
    name = data.get('name', None)
    l = LibraryDB(name=name)
    db.session.add(l)
    db.session.commit()
    return jsonify({'library_id': l.id})

@main_bp.route('/libraries/<int:lib_id>', methods=['GET', 'PUT'])
def get_item_library(lib_id):
    library = LibraryDB.query.filter_by(id=lib_id).first()
    return jsonify({'library': library.json() if library else None })

