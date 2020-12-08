from flask import jsonify, request
from flask_test_app.main.main import main_bp

from flask_test_app.dbmodels import BookDB, LibraryDB

@main_bp.route('/books', methods=['GET'])
def get_books():
    books = BookDB.query.all()
    return jsonify({'books': [b.json() for b in books]})

@main_bp.route('/books', methods=['POST'])
def create_books():
    return jsonify({'books': ['book1', 'book2']})

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
    data = request.form
    return jsonify({'library': ['library1', 'library1']})

@main_bp.route('/libraries/<int:lib_id>', methods=['GET', 'PUT'])
def get_item_library(lib_id):
    library = LibraryDB.query.filter_by(id=lib_id).first()
    return jsonify({'id': library.json() if library else None })

