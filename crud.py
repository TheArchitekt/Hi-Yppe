
from model import db, User, Brand, Sneaker, Favorite, connect_to_db


def new_user(user_email, user_password):
    """Creates a new user."""

    user = User(user_email=user_email, user_password=user_password)

    return user

def get_user_email(user_email):
    """Retrieves a user's email."""

    return User.query.filter(User.user_email == user_email).first()


def new_brand(brand_name):
    """Creates a new brand."""

    brand = Brand(brand_name=brand_name)

    return brand


def new_sneaker(sneaker_name, sneaker_price, sneaker_description, release_date, sneaker_img_path):
    """Creates a new sneaker"""
    sneaker = Sneaker(sneaker_name=sneaker_name, sneaker_price=sneaker_price,
                     sneaker_description=sneaker_description,
                     release_date=release_date, sneaker_img_path=sneaker_img_path)
    return sneaker


def new_favorite(user, sneaker):
    """Creates a new favorite sneaker for the user."""

    favorite = Favorite(user=user, sneaker=sneaker)

    return favorite


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
