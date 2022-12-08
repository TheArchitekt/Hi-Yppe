from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""


    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_email = db.Column(db.String, unique=True)
    user_password = db.Column(db.String)
    user_name = db.Column(db.String)

    def __repr__(self):
        return f"<User user_id={self.user_id} user_name={user_name} email={self.user_email}>"


class Brand(db.Model):
    """A brand."""

    __tablename__ = "brands"

    brand_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    brand_name = db.Column(db.String)

    def __repr__(self):
        return f"<Brand brand_id={self.brand_id}, brand_name={self.brand_name}>"


class Sneaker(db.Model):
    """A sneaker."""

    __tablename__ = "sneakers"

    sneaker_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sneaker_name = db.Column(db.String)
    sneaker_price = db.Column(Numeric(7, 2))
    sneaker_description = db.Column(db.Text)
    release_date = db.Column(db.DateTime, db.Index('ix_sneakers_release_date', 'release_date'))
    sneaker_img_path = db.Column(db.String)

    def __repr__(self):
        return f"<Sneaker sneaker_id={self.sneaker_id} sneaker_name={self.sneaker_name} release_date={self.release_date}>"


class Favorite(db.Model):
    """A user's favorites"""

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sneaker_id = db.Column(db.Integer, db.ForeignKey("sneakers.sneaker_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    def __repr__(self):
        return f"<Favorite favorite_id={self.favorite_id}>"


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
