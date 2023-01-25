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

    favorites = db.relationship("Favorite", back_populates="user")


    def __repr__(self):
        return f"<User user_id={self.user_id} user_name={self.user_name} email={self.user_email}>"



class Sneaker(db.Model):
    """A sneaker."""

    __tablename__ = "sneakers"

    sneaker_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sneaker_name = db.Column(db.String)
    sneaker_brand = db.Column(db.String)
    sneaker_price = db.Column(db.Numeric(7, 2))
    sneaker_description = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    sneaker_img_path = db.Column(db.String)

    favorites = db.relationship("Favorite", back_populates="sneaker")


    def __repr__(self):
        return f"<Sneaker sneaker_id={self.sneaker_id} sneaker_name={self.sneaker_name} release_date={self.release_date} sneaker_img_path={self.sneaker_img_path}>"


class Favorite(db.Model):
    """A user's favorites"""

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sneaker_id = db.Column(db.Integer, db.ForeignKey("sneakers.sneaker_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", back_populates="favorites")
    sneaker = db.relationship("Sneaker", back_populates="favorites")


    def __repr__(self):
        return f"<Favorite favorite_id={self.favorite_id}, sneaker_id={self.sneaker_id}>"


def connect_to_db(flask_app, db_uri="postgresql:///sneakers", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("DB is online!")



if __name__ == "__main__":
    from server import app

    connect_to_db(app)
