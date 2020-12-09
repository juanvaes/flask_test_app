from flask_test_app.dbmodels import LibraryDB


def test_create_library_object_with_no_books():
    """
    GIVEN a Library Model
    WHEN a new library is created
    THEN check the name of the library
    """
    lib = LibraryDB(name='Libreria Nacional')
    assert lib.name == 'Libreria Nacional'