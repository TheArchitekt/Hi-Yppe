from flask import Flask, render_template, request, session, redirect, flash
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "bluezagwa"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def home():
    """Homepage where users login or create an account"""

    return render_template("home.html")


@app.route("/users", methods=["POST"])
def create_account():
    """Creates a user account"""

    user_email = request.form.get("user_email")
    user_password = request.form.get("user_password")
    user_name = request.form.get("user_name")

    user = crud.get_user_email(user_email)

    if user:
        flash("An account exists with that email.")
    else:
        user = crud.new_user(user_email, user_password, user_name)
        db.session.add(user)
        db.session.commit()
        flash("Account created! You can now log in.")

    return redirect("/")

@app.route("/dashboard")
def dashboard():
    """Database Dashboard"""

    sneakers = crud.get_sneakers()


    return render_template("dashboard.html", sneakers=sneakers)

@app.route("/dashboard/<sneaker_id>")
def sneaker_page(sneaker_id):
    """Shows a specific sneaker's page"""

    sneaker = crud.get_sneaker_by_id(sneaker_id)

    return render_template("sneaker_page.html", sneaker=sneaker)

@app.route("/login", methods=["POST"])
def login_session():
    """Log into the session"""

    user_email = request.form.get("user_email")
    user_password = request.form.get("user_password")
    user_name = request.form.get("user_name")

    user = crud.get_user_email(user_email)

    if not user or user.user_password != user_password:
        flash("Your email or password is incorrect.")
    else:
        session["member_name"] = user.user_name
        flash(f"Welcome, {user.user_name}!")
        return redirect("/dashboard")

    return redirect("/")

@app.route("/users")
def all_users():
    """List of all users"""
    users = crud.get_users()

    return render_template("users.html", users=users)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
