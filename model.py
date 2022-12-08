

class User(db.Model):
    """A user."""


    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_email = db.Column(db.String, unique=True)
    user_password = db.Column(db.String)
    user_name = db.Column(db.String)

    def __repr__(self):
        return f"<User user_id={self.user_id} user_name={user_name} email={self.user_email}>"
