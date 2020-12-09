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
def new_user(client, init_db):
    name = "Tony Stark"
    email = 'tony@stark.com'
    password = "123456"
    response = client.post('/register', data=dict(
        name=name,
        email=email,
        password=password
    ))
    assert response.status_code == 200
    assert response.json['user_id'] == 1
    user = UserDB.query.filter_by(email=email).first()
    assert user.email == email
    assert user.name == name
    assert user.password == password
    yield user

@pytest.fixture(scope='function')
def login_user(client, new_user):
    response = client.post('/login', data=dict(
        email=new_user.email,
        password=new_user.password
    ))
    assert response.status_code == 200
    assert response.json == {'token': 'User logged in'}
    yield new_user