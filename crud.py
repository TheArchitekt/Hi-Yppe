
from model import db, User, Brand, Sneaker, Favorite, connect_to_db, flash


def new_user(user_email, user_password):
    """Creates a new user."""

    user = User(user_email=user_email, user_password=user_password)

    return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
