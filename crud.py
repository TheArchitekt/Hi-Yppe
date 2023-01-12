
from model import db, User, Sneaker, Favorite, connect_to_db


def new_user(user_email, user_password, user_name):
    """Creates a new user."""

    user = User(user_email=user_email, user_password=user_password, user_name=user_name)

    return user


def get_users():
    """Gets all users"""

    return User.query.all()

def get_user_email(user_email):
    """Retrieves a user's email."""

    return User.query.filter(User.user_email == user_email).first()


def get_user_by_id(user_id):
    """Retrieves a user by primary key"""

    return User.query.get(user_id)

def new_sneaker(sneaker_name, sneaker_brand, sneaker_price, sneaker_description, release_date, sneaker_img_path):
    """Creates a new sneaker"""
    sneaker = Sneaker(sneaker_name=sneaker_name, sneaker_brand=sneaker_brand,
                     sneaker_price=sneaker_price, sneaker_description=sneaker_description,
                     release_date=release_date, sneaker_img_path=sneaker_img_path)
    return sneaker

def get_sneakers():
    """Retrieves all sneakers."""

    return Sneaker.query.all()

def get_sneaker_by_id(sneaker_id):
    """Retrieves a sneaker by primary key."""

    return Sneaker.query.get(sneaker_id)


def new_favorite(user, sneaker):
    """Creates a new favorite sneaker for the user."""
    favorite = Favorite(user=user, sneaker=sneaker)

    return favorite





if __name__ == '__main__':
    from server import app
    connect_to_db(app)
