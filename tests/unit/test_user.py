from flask_test_app.dbmodels import UserDB

"""
GIVEN - What are the initial conditions for the tests?
WHEN - What is ocurring that needs to be tested?
THEN - What is the expected response?
"""


def test_create_user():
    """
    GIVEN an UserDB model
    WHEN a new user is created
    THEN the user name field must be equal to the input's user name
    """
    user_name = "Juan Camilo Valencia"
    user = UserDB(name=user_name)
    assert user.name == user_name
