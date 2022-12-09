from flask import Flask, render_template, request, session, redirect
from model import connect_to_db, db


app = Flask(__name__)


@app.route("/")
def home():
    """Homepage where users login or create an account"""

    return render_template("home.html")


@app.route("/account", methods=["POST"])
def create_account():
    """Creates a user account"""

    user_email = request.form.get("user_email")
    user_password = request.form.get("user_password")

    user = crud.get_user_email(user_email)

    if user:
        flash("An account exists with that email.")
    else:
        user = crud.new_user(user_email, user_password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! You can now log in.")

    return redirect("/")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
