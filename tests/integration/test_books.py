import json

from flask_test_app import create_app

def test_get_book_id_1(client, init_db):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/books/1'  is requested (GET)
    THEN check that the response is valid
    """
    response = client.get('/books/1')
    expected = {'book': {'title': 'Harry Potter', 'author': 'J.K. Rowling'}}
    assert response.status_code == 200
    assert response.json == expected

def test_create_book(client, init_db):
    lib_id = 2
    response = client.get(f'/libraries/{lib_id}')
    assert response.status_code == 200
    lib = response.json
    response = client.post('/books', data=dict(
        title='El coronel no tiene quien le escriba',
        author='Gabriel Garcia Marquez',
        library_id=lib_id
        )
    )
    expected = {'book_id': 4}
    assert response.status_code == 200
    assert response.json == expected
