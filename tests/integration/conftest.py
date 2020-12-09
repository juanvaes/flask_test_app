import pytest

from flask_test_app import create_app, db
from flask_test_app.dbmodels import LibraryDB, BookDB, UserDB


libs = [
    {'name': 'Libreria Nacional'},
    {'name': 'Libreria Departamental'}
]

books = [
    {'title': 'Harry Potter', 'author': 'J.K. Rowling', 'library_id': 1},
    {'title': '5AM Club', 'author': 'Robin Sharma', 'library_id': 1},
    {'title': 'Cien años de soledad', 'author': 'Gabriel Garcia Marquez', 'library_id': 2}
]

@pytest.fixture(scope='module')
def client():
    test_app = create_app('config.TestingConfig')
    client = test_app.test_client()
    ctx = test_app.app_context()
    ctx.push()
    yield client
    ctx.pop()


@pytest.fixture(scope='module')
def init_db(client):
    db.create_all()

    yield db
    # I added this line, somehow the session was stuck doing the drop.all()
    db.session.commit()
    db.drop_all()

@pytest.fixture(scope='function')
def create_books_and_libs(init_db):
    # Create libraries
    for l in libs:
        lib = LibraryDB(name=l['name'])
        db.session.add(lib)

    # Create books
    for b in books:
        book = BookDB(title=b['title'], author=b['author'], library_id=b['library_id'])
        db.session.add(book)

    db.session.commit()

    yield 
    

@pytest.fixture(scope='function')
def new_user(init_db):
    # Create User
    user_name = "Tony Stark"
    user = UserDB(name=user_name)
    user.save()
    assert bool(user.id)
    del user
    user = UserDB.query.filter_by(name=user_name).first()
    assert user is not None
    assert user.name == user_name

    yield user
    

