from flask import jsonify, request

from flask_test_app import db
from flask_test_app.main.main import main_bp
from flask_test_app.dbmodels import BookDB, LibraryDB

@main_bp.route('/books', methods=['GET'])
def get_books():
    books = BookDB.query.all()
    return jsonify({'books': [b.json() for b in books]})

@main_bp.route('/books', methods=['POST'])
def create_books():
    lib_id = request.args.get('lib_id', None)
    title = request.args.get('title', None)
    author = request.args.get('author', None)
    if lib_id:
        lib_id = int(lib_id)
    b = BookDB(title=title, author=author, library_id=lib_id)
    db.session.add(b)
    db.session.commit()
    return jsonify({'book_id': b.id})

@main_bp.route('/books/<int:book_id>', methods=['GET', 'PUT'])
def get_item_book(book_id):
    book = BookDB.query.filter_by(id=book_id).first()
    return jsonify({'id': book.json() if book else None })

@main_bp.route('/libraries', methods=['GET'])
def get_libraries():
    libraries = LibraryDB.query.all()
    return jsonify({'libraries': [l.json() for l in libraries]})

@main_bp.route('/libraries', methods=['POST'])
def create_library():
    name = request.args.get('name', None)
    l = LibraryDB(name=name)
    db.session.add(l)
    db.session.commit()
    return jsonify({'library_id': l.id})

@main_bp.route('/libraries/<int:lib_id>', methods=['GET', 'PUT'])
def get_item_library(lib_id):
    library = LibraryDB.query.filter_by(id=lib_id).first()
    return jsonify({'id': library.json() if library else None })

