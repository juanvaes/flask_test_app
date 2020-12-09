from flask_test_app.dbmodels import BookDB


def test_create_book_object():
    """
    GIVEN a Library Model
    WHEN a new library is created
    THEN check the name of the library
    """
    title = 'Cien años de soledad'
    author = 'Gabriel Garcia Marquez'
    book = BookDB(title=title, author=author)
    assert book.title == title
    assert book.author == author
    expected = {'title': title, 'author': author}
    assert book.json() == expected

