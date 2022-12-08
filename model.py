

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
