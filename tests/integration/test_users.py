import pytest

from flask_test_app import db
from flask_test_app.dbmodels import UserDB, BookDB

def test_create_user_and_must_exist_in_database(init_db):
    """
    GIVEN an UserDB model
    WHEN a new user is created
    THEN the new user must exist in database and its name should be equal to the one provided by the input
    """
    user_name = "Juan Camilo Valencia"
    user = UserDB(name=user_name)
    user.save()
    assert bool(user.id)
    user = UserDB.query.filter_by(name=user_name).first()
    assert user is not None
    assert user.name == user_name

def test_list_user_books_empty(new_user):
    """
    GIVEN an user
    WHEN user's book are requested
    THEN there should be an empty list
    """
    user = new_user
    user_books = user.books
    assert isinstance(user_books, list)
    assert not bool(user_books)

def test_associate_books_to_user(new_user):
    """
    GIVEN an user
    WHEN we associate some books to an user
    THEN we should be able to list those books from the user
    
    """
    user = new_user
    user_name = user.name

    books = BookDB.query.all()
    user.books = books[:1]
    db.session.add(user)
    db.session.commit()

    user = UserDB.query.filter_by(name=user_name).first()
    assert user is not None
    assert len(user.books) == 2




